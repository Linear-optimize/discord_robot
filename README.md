# Discord 多功能机器人（Python）

基于 `discord.py` 的异步机器人项目，当前提供 AI 问答、天气查询、翻译、随机图片与基础工具命令，适合学习和二次开发。

## 功能概览

- 🤖 `ask`：调用 OpenAI 进行问答。
- 🌤️ `weather`：查询城市实时天气（高德地理编码 + Tomorrow.io）。
- 🌐 `translate`：调用腾讯云翻译。
- 🖼️ `image` / `draw`：获取随机图片或按关键词取图。
- 🛠️ `ping` / `add`：基础测试与计算命令。
- ⚡ 支持 Hybrid Commands（可作为前缀命令和 `/` 命令使用）。

## 项目结构（当前仓库）

```text
.
├── cogs/
│   ├── ai.py
│   ├── base_use.py
│   ├── translate.py
│   ├── weather.py
│   └── __init__.py
├── main.py
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

> 当前项目**没有** `fun.py`、`bilibili.py`、`video.py` 等文件，文档以仓库实际内容为准。

## 环境要求

- Python 3.10+
- Discord Bot Token
- OpenAI、腾讯云、Tomorrow.io、高德地图等 API Key（按需启用）

## 安装依赖

推荐使用 `uv`（与仓库锁文件一致）：

```bash
uv sync
```

或使用 `pip`：

```bash
pip install -r requirements.txt
```

## 环境变量配置

在项目根目录新建 `.env`：

```env
# Discord
DISCORD_TOKEN=你的Discord机器人Token

# OpenAI
OPENAI_API_KEY=你的OpenAI密钥
BASE_URL=https://api.openai.com/v1
MODEL=gpt-4o-mini

# 腾讯翻译
secretld=你的腾讯SecretId
secretkey=你的腾讯SecretKey

# 天气能力
WEATHER_KEY=你的Tomorrow.io密钥
MAP_KEY=你的高德地图密钥
```

> 变量名按代码实际读取保持大小写一致，尤其是 `secretld`（小写 l+d）。

## 启动项目

```bash
uv run main.py
```

或：

```bash
python main.py
```

启动后可在服务器中使用命令；管理员可用 `!synccommands` 手动同步指令。

## 开发说明

- 所有功能以 `cogs` 模块加载，在 `main.py` 的 `load_cogs()` 中注册。
- HTTP 请求复用 `aiohttp.ClientSession`，避免重复建连。
- 新增命令建议放到新的 Cog 文件中，并在 `load_cogs()` 中追加扩展路径。

## License

请参考仓库根目录 `LICENSE` 文件。
