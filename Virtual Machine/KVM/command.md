# virsh
管理VM客户端
## list
* --all
## domifaddr
网络信息
## dumpxml
检查虚拟机配置信息
## console
连接机器
```bash
sudo virsh domifaddr tos4-vm
 Name       MAC address          Protocol     Address
-------------------------------------------------------------------------------
# 连接虚拟机
sudo virsh console tos4-vm
```


# virt-manager 
图形化工具

# qemu-img
qemu模拟器套件中的一个命令行工具，管理操作转换虚拟磁盘镜像文件。
```bash 
sudo qemu-img  create -f qcow2 /var/lib/libvirt/images/tos4.qcow2 50G
# /var/lib/libvirt/images/tos4.qcow2 路径
# -f 指定类型 qcow2 类型
# 50G 大小
sudo qemu-img info /var/lib/libvirt/images/tos4.qcow2
# 展示创建的虚拟磁盘信息
```

# virt-install
```bash 
# 启动一个虚拟机

sudo virt-install     --name tos4-iso-vm-001     --ram 32768     --vcpus 8     --disk path=/var/lib/libvirt/images/tos4-iso-001-disk.qcow2,size=100,format=qcow2,bus=virtio     --location /mnt/data/baker.xue/TencentOS-Server-4.4-20250805.0-aarch64-minimal.iso     --network bridge=virbr0,model=virtio   --console pty,target_type=serial  --extra-args="console=ttyS0,115200n8 serial"


sudo virt-install     --name kylin-v10-sp3     --ram 16384     --vcpus 8     --disk path=/data/kvm/libvirt/images/kylin-iso-v10-sp3-disk.qcow2,size=200,format=qcow2,bus=virtio  --osinfo rhel8.0   --location /mnt/shared_data/baker.xue/Kylin-Server-V10-SP3-2403-Release-20240426-X86_64.iso  --network bridge=virbr0,model=virtio --graphics none  --console pty,target_type=serial --extra-args="console=ttyS0,115200n8 inst.text"



sudo virt-install --name tos4-vm --ram 4096 --vcpu 2 --import --disk path=/var/lib/libvirt/images/TencentOS-Server-GenericCloud-4.4-20250805.0.aarch64.qcow2 --network bridge=virbr0,model=virtio  --graphics spice,listen=0.0.0.0 --noautoconsole

sudo virt-install \
    --name tos4-vm-cloud \
    --ram 4096 --vcpus 2 \
    --disk path=/var/lib/libvirt/images/TencentOS-Server-GenericCloud-4.4-20250805.0.aarch64.qcow2,format=qcow2,bus=virtio \
    --disk path=./cloud-init.iso,device=cdrom \
    --network bridge=virbr0,model=virtio \
    --graphics spice,listen=0.0.0.0 \
    --noautoconsole


sudo virt-install \
    --name tos4-iso-vm \
    --ram 4096 \
    --vcpus 2 \
    --disk path=/var/lib/libvirt/images/tos4-iso-disk.qcow2,size=100,format=qcow2,bus=virtio \
    --location /mnt/data/baker.xue/TencentOS-Server-4.4-20250805.0-aarch64-minimal.iso \
    --network bridge=virbr0,model=virtio \
    --graphics spice,listen=0.0.0.0 \
    --noautoconsole


```