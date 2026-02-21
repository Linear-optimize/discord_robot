from discord.ext import commands
from openai import AsyncOpenAI


class AiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="ask", description="问问题")
    async def ask(self, ctx, question: str):
        await ctx.defer()

        client = AsyncOpenAI(
            api_key=self.bot.api_key, base_url=self.bot.base_url
        )
        response = await client.chat.completions.create(
            model=self.bot.model, messages=[{"role": "user", "content": question}]
        )

        answer = response.choices[0].message.content

        await ctx.send(answer)


async def setup(bot):
    await bot.add_cog(AiCog(bot))
