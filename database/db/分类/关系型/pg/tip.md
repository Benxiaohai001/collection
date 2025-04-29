# 本地安装
# 账号：postgres postgres

切换数据库需要输入用户密码；
# command
\? 显示所有的命令
\c database # 连接某个数据库；
\l  显示所有的db
\d 列出所有的表，视图和序列
# FDW
FDW（Foreign Data Wrapper，外部数据包装器）是 PostgreSQL 中实现 SQL/MED 标准的核心机制，用于在本地数据库中访问和操作外部数据源（如其他数据库、文件、API 等）的数据，使其像本地表一样可查询和管理。其核心目标是通过统一接口实现异构数据的联邦访问与集成，减少数据迁移和冗余存储的成本。