import discord
from discord.ext import commands


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="ping", description="ping命令")
    async def ping(self, ctx):
        await ctx.send("pong")

    @commands.hybrid_command(name="add", description="加法")
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a + b)

    @commands.hybrid_command(
        name="draw", description="动漫图片,num为访问数目,tag为关键词"
    )
    async def draw(self, ctx, num: int, tag: str):
        await ctx.defer()

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
        }

        url = "https://api.lolicon.app/setu/v2"

        params = {"r18": 2, "num": num, "tag": tag}
        session = self.bot.http_session

        async with session.get(url=url, headers=headers, params=params) as response:
            data = await response.json(content_type=None)

        url_images = data["data"]
        for item in url_images:
            url_image = item["urls"]["original"]

            embed = discord.Embed()
            embed.set_image(url=url_image)

            await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="image", description="随机图片"
    )
    async def image(self, ctx):
        await ctx.defer()

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
        }

        params = { "return": "json"}
        url = "https://api.yppp.net/pc.php"
        session = self.bot.http_session
        async with session.get(url=url, headers=headers, params=params) as response:
            data = await response.json(content_type=None)

        url_image = data["acgurl"]

        embed = discord.Embed()
        embed.set_image(url=url_image)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(FunCog(bot))
