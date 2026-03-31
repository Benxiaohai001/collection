# SOP: Kylin KVM 标准安装流程

## 前置检查

- 确认宿主机可通过 `sudo` 执行 `virsh`、`virt-install`
- 确认 ISO 文件真实存在于宿主机
- 确认目标磁盘路径没有残留无效 qcow2 占位文件
- 确认宿主机目标物理网卡已连上业务网段，例如 `10.24.*`
- 确认本次安装使用 BIOS 还是 UEFI；本文档按 BIOS 方案编写

## 风险预估

- 若使用 libvirt 默认 NAT 网络，虚机不会直接获得 `10.24.*` 地址
- 若安装后不清理安装器残留 XML，虚机会再次进入安装器
- 该麒麟 SP2 ISO 在自动分区场景下可能出现引导装载器安装失败
- **不要依赖安装后通过 guest agent chpasswd 重设密码**，Kylin SP2 上此方式不可靠（返回成功但密码不生效）
- Kickstart 中必须直接指定 `--password`，不要分两步走

## 步骤 1: 核对宿主机资源与网络

```bash
sudo virsh list --all
sudo virsh net-list --all
ip -4 addr show em1
ip route
ls -l /var/lib/libvirt/images/
```

目标:

- ISO 存在
- 宿主机网卡 `em1` 已在 `10.24.*` 网段
- 没有无效旧镜像干扰

## 步骤 2: 准备 Kickstart

关键点:

- 不用自动分区
- 显式创建 `biosboot`、`/boot`、`swap`、`/`
- 安装完成后使用 `poweroff`
- 启用 `sshd` 和 `qemu-guest-agent`


## 步骤 3: 创建虚机并启动安装

```bash
sudo virt-install \
  --name kylin_v10_sp2_001 \
  --memory 32768 \
  --vcpus 16 \
  --cpu host-passthrough \
  --disk path=/var/lib/libvirt/images/kylin_v10_sp2_001.qcow2,size=200,format=qcow2,bus=virtio \
  --disk /var/lib/libvirt/images/Kylin-Server-10-SP2-Release-Build09-20210524-x86_64.iso,device=cdrom,bus=ide \
  --location /var/lib/libvirt/images/Kylin-Server-10-SP2-Release-Build09-20210524-x86_64.iso,kernel=images/pxeboot/vmlinuz,initrd=images/pxeboot/initrd.img \
  --os-variant kylin10.0 \
  --graphics none \
  --console pty,target_type=serial \
  --network direct,source=em1,source_mode=bridge,model=virtio \
  --channel unix,target_type=virtio,name=org.qemu.guest_agent.0 \
  --initrd-inject /tmp/kylin_v10_sp2_001.ks \
  --extra-args 'inst.ks=file:/kylin_v10_sp2_001.ks inst.stage2=hd:LABEL=Kylin-Server-10 inst.repo=hd:LABEL=Kylin-Server-10 console=ttyS0,115200n8 inst.text' \
  --noautoconsole
```

## 步骤 4: 监控安装

- 用户侧观察串口控制台
- 运维侧观察宿主机状态

常用命令:

```bash
sudo virsh domstate kylin_v10_sp2_001
sudo virsh console kylin_v10_sp2_001
sudo tail -n 200 /var/log/libvirt/qemu/kylin_v10_sp2_001.log
```

安装完成标准:

- 虚机按 Kickstart 设定自动 `poweroff`

## 步骤 5: 清理安装器残留配置

安装结束后，必须从 domain XML 中删除:

- `<kernel>`
- `<initrd>`
- `<cmdline>`
- 所有安装 ISO 对应 `cdrom`

然后重新定义并启动虚机，只保留 `<boot dev='hd'/>`

## 步骤 6: 启动系统并获取 IP

优先使用 guest agent:

```bash
sudo virsh domifaddr kylin_v10_sp2_001 --source agent
sudo virsh qemu-agent-command kylin_v10_sp2_001 '{"execute":"guest-network-get-interfaces"}'
```

若 guest agent 未响应，再尝试:

```bash
sudo virsh domifaddr kylin_v10_sp2_001 --source arp
```

## 步骤 7: 交付验证

- 串口出现登录提示符
- 确认来宾系统已获取目标网段地址
- 确认 `gpadmin` 用户存在
- 确认 `sshd` 已启动
- **SSH 和控制台双重登录验证通过才算交付完成**

## 常见故障速查

- `安装源/软件选择报错`: 补齐 `inst.stage2` 和 `inst.repo`
- `引导装载器安装失败`: 改用显式 BIOS 分区，不用自动分区
- `安装完又回到安装器`: 清理 XML 中的安装内核、initrd、cmdline 和 CDROM
- `virsh console 被占用`: 当前连接方先按 `Ctrl+]` 退出
- `chpasswd 设密码成功但登录失败`: 在 Kickstart 中直接指定 `--password`，不要用 guest agent 设密码

