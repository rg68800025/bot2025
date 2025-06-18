# 狙击策略交易机器人 (Sniper Strategy Bot)

这是一个部署在 Railway 云平台、接入 Telegram 推送的智能交易机器人。核心功能包括：

- 自动监控 ETH/BTC/SOL/XRP/FARTCOIN 多币种
- 判断 Wyckoff 结构、关键价区、成交量关系
- 每小时自动运行并将交易信号推送到 Telegram
- 自动记录交易信号并支持每日总结

## 快速开始（Railway）

1. Fork 本仓库至你的 GitHub 账户
2. 登录 [Railway](https://railway.app)，点击 "New Project" → "Deploy from GitHub Repo"
3. 填入你的仓库链接 `https://github.com/rg68800025/sniper-bot`
4. 配置环境变量：

```
BOT_TOKEN=7245337089:AAFhYBcKs_kQPM8RqXoYviCLIHYSdHl-Q9Q
CHAT_ID=7033319405
```

5. 点击部署，等待构建完成。

## 目录结构

- `main.py`: 项目主入口，自动调度策略执行
- `strategy.py`: 狙击策略核心逻辑
- `telegram.py`: Telegram 推送接口
- `requirements.txt`: 项目依赖
