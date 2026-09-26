# A1-13 ML-KEM Platform

这是 A1-13 竞赛作品的实验平台仓库。目标是围绕 ML-KEM 解封装实现，完成时间检测、统计分析、定位、防护改造、复测和报告导出。

队员请先看：

```text
docs/TEAM_GUIDE.md
```

## 当前状态

当前是初始平台版本，已经接入：

- ML-KEM-512、ML-KEM-768、ML-KEM-1024
- 基本生成、封装、解封装接口
- 共享值一致性验证
- 公开测试向量验证
- 固定 CPU 核短实验计时检测
- 浏览器操作界面

## 目录结构

```text
backend/          后端 API
frontend/         前端页面
core/             核心实现代码
scripts/          构建和启动脚本
tests/            基础测试
docs/             队员说明文档
results/          本地运行结果，不提交到 Git
```

## 构建

```bash
./scripts/build.sh
```

## 启动

```bash
./scripts/start.sh
```

默认只监听：

```text
127.0.0.1:8000
```

远程服务器运行时，可用端口转发：

```bash
ssh -p <PORT> -L 8000:127.0.0.1:8000 <USER>@<HOST>
```

然后打开：

```text
http://127.0.0.1:8000
```


## 构建短实验计时程序

平台的固定 CPU 核短实验计时检测调用仓库内：

```text
experiments/clangover-poc/
```

首次运行前执行：

```bash
./scripts/build_timing_demo.sh
```

## 基础测试

```bash
python3 tests/test_basic.py
```

## 注意

仓库已经直接包含 `core/mlkem-native` 代码，队员 clone 后不需要再初始化子模块。

不要提交运行日志、服务 PID、服务器地址、密码、个人 token 或大型临时结果。
