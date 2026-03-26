import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import aiohttp

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.base_url = os.getenv("BASE_URL")
bot.api_key = os.getenv("OPENAI_API_KEY")
bot.secretld = os.getenv("secretld")
bot.secretkey = os.getenv("secretkey")
bot.weather_key = os.getenv("WEATHER_KEY")
bot.map_key = os.getenv("MAP_KEY")
bot.model = os.getenv("MODEL")

token = os.getenv("DISCORD_TOKEN")


@bot.command()
@commands.has_permissions(administrator=True)
async def synccommands(ctx):
    await bot.tree.sync(guild=ctx.guild)
    await ctx.send("同步成功")


async def load_cogs():
    cogs = [
        "cogs.base_use",
        "cogs.ai",
        "cogs.translate",
        "cogs.weather",
    ]
    for cog in cogs:
        await bot.load_extension(cog)
        print(f"✅ 成功加载扩展: {cog}")


@bot.event
async def on_ready():
    if not hasattr(bot, "http_session"):
        bot.http_session = aiohttp.ClientSession()
    await load_cogs()

    await bot.tree.sync()

    print(f"{bot.user} 已上线！")


if __name__ == "__main__":
    try:
        bot.run(token)
    except KeyboardInterrupt:
        print("程序已手动停止")
