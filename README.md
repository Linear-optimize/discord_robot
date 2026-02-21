# 一个简单的Discord机器人

## 📂项目结构
```
my_robot
├─ .python-version
├─ cogs
│  ├─ ai.py
│  ├─ bilibili.py
│  ├─ fun.py
│  ├─ translate.py
│  ├─ video.py
│  ├─ weather.py
│  └─ __init__.py
├─ LICENSE
├─ main.py
├─ pyproject.toml
├─ README.md
├─ utils
│  └─ updown_bilibili.py
└─ uv.lock

```

## ✨功能特点
 - ✅ **AI问答** - 接入了**chatgpt**
 - ✅ **天气询问** - 使用OpenWeather的api
 - ✅ **随机图片** - 第三方api
 - ✅ **简单翻译** - tencent翻译api、
 - ✅ **斜杠命令** - 支持支持 Hybrid Commands（同步后可在 Discord 直接输入 `/` 使用）
 

## 📦安装依赖
> pip
```bash
pip install -r requirements.txt
```

> uv
```bash
uv sync
```


## 🚀快速开始
1. 在 **.env** 文件中配置你的 **DISCORD_BOT_TOKEN** ,**OPENAI_API_KEY** **Secretld**和**SecretKey**

2. 运行脚本(推荐uv)
>uv
```bash
uv run main.py
```
>原生python
```bash
python main.py
```
## ⚖️ 技术评估
- **异步驱动**: 全程使用 `aiohttp` 和 `AsyncOpenAI`，保证高并发下机器人不卡顿。
- **模块化设计**: 采用 `Discord Cogs` 架构，功能解耦，支持热加载。
- **高效连接池**: 全局共用一个 `ClientSession`，优化网络资源占用。
- **混合指令**: 完美适配 `Hybrid Commands`，兼顾老玩家习惯与新斜杠体验。

## 🚧改进点
- [ ] 错误处理: 增加全局异常捕获，防止 API 调用失败导致崩溃。
- [ ] 日志系统: 接入 logging 模块，记录指令调用频率与错误堆栈
- [ ] 配置优化: 统一 .env 变量命名规范，增强代码可读性


