# cargo-llvm-cov
Cargo 子命令可轻松使用 LLVM 基于源代码的代码覆盖率。
提供的功能：
* 生成精准的覆盖数据；（行，区域，分支覆盖）
* 支持cargo test、cargo run、cargo nextest，命令行界面兼容cargo。
* 支持 proc-macro，包括 UI 测试的覆盖范围。
* 支持文档测试
* 速度快，因为它不会在 rustc、cargo 和 llvm-tools 之间引入额外的层。