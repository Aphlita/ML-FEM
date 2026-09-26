# 队员入门指南

这份文档用于让新队员尽快把项目跑起来，并知道下一步怎么参与。

## 1 克隆仓库

如果仓库已经推到 GitHub，建议这样克隆：

```bash
git clone <REPO_URL>
cd a1-13-mlkem-platform
git submodule update --init --recursive
```

注意：`core/mlkem-native` 是子模块。如果不执行 `git submodule update --init --recursive`，核心实现目录会是空的或不完整。

## 2 构建

```bash
./scripts/build.sh
```

如果构建失败，先检查：

- 子模块是否初始化。
- 是否在 Linux 环境下运行。
- C 编译器是否可用。
- Python 是否可用。

## 3 启动平台

```bash
./scripts/start.sh
```

默认监听：

```text
127.0.0.1:8000
```

如果在远程服务器上运行，需要本地做端口转发：

```bash
ssh -p <PORT> -L 8000:127.0.0.1:8000 <USER>@<HOST>
```

然后浏览器打开：

```text
http://127.0.0.1:8000
```

## 4 跑基础测试

```bash
python3 tests/test_basic.py
```

这个测试用于检查三个参数集的基础功能是否正常。

## 5 平台现有接口

目前后端主要接口包括：

- `/api/info`：查看平台信息。
- `/api/keygen`：生成密钥对。
- `/api/encaps`：封装。
- `/api/decaps`：解封装。
- `/api/self-test`：基础自测。
- `/api/vector-test`：公开测试向量验证。
- `/api/timing-detect`：固定 CPU 核短实验计时检测。

## 6 目前不应该提交什么

不要提交：

- `results/` 目录。
- 运行日志。
- 服务 PID。
- 本地环境文件。
- 服务器地址、密码、个人 token。
- 大型临时数据。

## 7 队员接任务的方式

建议每个人选择一个模块：

- 前端同学：优化页面、图表、结果展示、报告导出按钮。
- 后端同学：补样本生成、统计分析、数据保存接口。
- 实验同学：设计样本类别、跑采集、整理数据。
- 文档同学：写复现说明、环境说明、设计报告。

接任务前先看 `docs/MODULES_AND_TASKS.md`。
