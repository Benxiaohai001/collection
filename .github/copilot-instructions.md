# Copilot / AI Agent 指南（为此仓库定制）

下面的说明旨在让 AI 编码/编辑代理能快速在此仓库中安全、高效地工作。

1. 项目性质（大局）:
   - 本仓库为个人/团队技术笔记与文档集合（大量 Markdown 文件，中文为主）。
   - 主要主题目录：`AI/`、`cloud/`、`database/`、`programming/`、`OS/`、`Virtual Machine/`、`tool/`、`课程/` 等。修改时请遵循原目录语义。

2. 主要工作类型（可执行动作）：
   - 编辑或新增 Markdown 文档（.md）以补充笔记或更正错字。
   - 在 `tool/` 下可以发现 CI/Jenkins 脚本（例如 `tool/jenkinsfile-tp`、`tool/jenkinsfile-piecloud`），这些是 CI 管线示例，变更需谨慎并说明影响范围。

3. 可参考关键文件（快速入口）：
   - 仓库根 `README.md`：仓库总体说明。
   - 示例笔记：`Virtual Machine/KVM/concept.md`（虚拟化专题），`programming/python/doc/README.md`（Python 学习资源）。
   - CI/构建脚本：`tool/jenkinsfile-*`（包含对 Dockerfile 的引用与构建步骤）。

4. 编辑规范与约定（针对 AI）：
   - 语言：优先保留中文内容与术语；新增英文术语请在括号中注明对应中文（如必要）。
   - 文件格式：保持 Markdown 纯文本（UTF-8）；不要添加或移除 YAML front-matter（仓库中通常不使用）。
   - 命名与路径：遵循现有目录与文件名风格，不要随意改动文件或目录层级，除非用户明确要求重构。
   - 链接：不要更写已存在的相对链接，若更新目标文件，确保相对链接仍然有效。

5. CI / 构建 / 运行说明（可发现的工作流）：
   - 本仓库主要为文档集合，无统一构建系统；但在 `tool/` 中存在 Jenkinsfile 脚本，显示项目会在 CI 中使用 Docker 构建镜像（见 `tool/jenkinsfile-tp` 和 `tool/jenkinsfile-piecloud`）。
   - 若需预览 Markdown，可使用编辑器内预览或常见工具（由用户自行运行）。AI 不要假设有测试套件或标准构建命令，修改前询问用户是否需要运行 CI/构建。

6. 变更与提交策略（代理须遵守）：
   - 小而明确的提交：每次修改只变更相关文件并在提交信息中说明理由（例如：`修正 Virtual Machine/KVM/concept.md 中的术语描述`）。
   - 不要批量重命名或移动大量文件，除非用户授权并提供迁移规则。

7. 可执行示例（当你被要求编辑某主题时）：
   - 修改 `Virtual Machine/KVM/concept.md`：只编辑该文件，保留原中文表述风格，新增段落请使用小标题 `###` 并保持语言一致性。
   - 更新 CI 参考：修改 `tool/jenkinsfile-piecloud` 时，注释说明为什么改动并列出受影响的 Dockerfile 名称。

8. 自动化行为限制（禁止或需确认的操作）：
   - 禁止：在没有明确指示的情况下批量删除或重组目录结构，修改多语言镜像或翻译原文内容。
   - 需确认：对 `tool/jenkinsfile-*` 或任何 CI 相关脚本做改动前，先询问用户并列出变更风险。

9. 查找与引用建议（给 AI 的快速检索提示）：
   - 若查找主题，优先在对应顶级目录搜索（例如想看虚拟化相关，先查 `Virtual Machine/`）。
   - 使用文件名示例作为锚点（例如 `Virtual Machine/KVM/concept.md`、`tool/jenkinsfile-tp`）。

10. 完成变更后的报告格式（AI 应输出给用户的最小报告）：
   - 列出改动文件清单（短路径列表）。
   - 说明为何改动（1-2 行）。
   - 提示任何需要人工验证的后续步骤（例如：运行 CI、检查链接是否失效）。

如果此指南有遗漏或某些目录/文件需要更细的规则，请告诉我想要优先覆盖的部分，我会合并并更新。
