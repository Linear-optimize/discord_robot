import discord
from discord.ext import commands

# 建议放在类外面，作为常量，节省资源
WEATHER_MESSAGES = {
    "0": {"label": "未知", "emoji": "❓"},
    "1000": {"label": "晴朗", "emoji": "☀️"},
    "1100": {"label": "大部分晴朗", "emoji": "🌤️"},
    "1101": {"label": "多云", "emoji": "⛅"},
    "1102": {"label": "阴天", "emoji": "☁️"},
    "1001": {"label": "阴天", "emoji": "☁️"},
    "2000": {"label": "有雾", "emoji": "🌫️"},
    "2100": {"label": "轻雾", "emoji": "🌫️"},
    "4000": {"label": "毛毛雨", "emoji": "🌦️"},
    "4001": {"label": "下雨", "emoji": "🌧️"},
    "4200": {"label": "小雨", "emoji": "🌧️"},
    "4201": {"label": "大雨", "emoji": "🌊"},
    "5000": {"label": "下雪", "emoji": "❄️"},
    "5001": {"label": "小雪/飘雪", "emoji": "🌨️"},
    "5100": {"label": "轻雪", "emoji": "🌨️"},
    "5101": {"label": "大雪", "emoji": "🏔️"},
    "6000": {"label": "冻毛毛雨", "emoji": "🥶"},
    "6001": {"label": "冻雨", "emoji": "🧊"},
    "6200": {"label": "轻冻雨", "emoji": "🧊"},
    "6201": {"label": "重冻雨", "emoji": "🧊"},
    "7000": {"label": "冰雹", "emoji": "☄️"},
    "7101": {"label": "重冰雹", "emoji": "💥"},
    "7102": {"label": "轻冰雹", "emoji": "💎"},
    "8000": {"label": "雷暴", "emoji": "⛈️"},
    "1103": {"label": "多云转晴", "emoji": "🌤️"},
    "2101": {"label": "轻雾伴晴", "emoji": "🌫️☀️"},
    "4204": {"label": "阵性毛毛雨", "emoji": "🌦️"},
    "5108": {"label": "雨夹雪", "emoji": "🌨️🌧️"},
    "8001": {"label": "雷阵雨转晴", "emoji": "⛈️☀️"},
}

COLOR_MAP = {
    "1": 0xFFD700,
    "2": 0xBDC3C7,
    "4": 0x3498DB,
    "5": 0xFFFFFF,
    "6": 0x00CED1,
    "7": 0xE0FFFF,
    "8": 0x8E44AD,
}


class WeatherCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="weather", description="询问天气")
    async def weather(self, ctx, city: str):
        await ctx.defer()
        session = self.bot.http_session

        async with session.get(
            "https://restapi.amap.com/v3/geocode/geo",
            params={"address": city, "key": self.bot.map_key},
        ) as response:
            geo = await response.json()

        if not geo.get("geocodes"):
            return await ctx.send(f"❌ 找不到地点: {city}")

        req_str = geo["geocodes"][0]["location"]
        lon, lat = req_str.split(",")

        # 2. 获取天气数据
        async with session.get(
            "https://api.tomorrow.io/v4/weather/forecast",
            params={
                "location": f"{lat},{lon}",
                "fields": "temperature,precipitationProbability,weatherCode",
                "units": "metric",
                "apikey": self.bot.weather_key,
            },
        ) as reqs:
            weather_data = await reqs.json()

        try:
            current_values = weather_data["timelines"]["minutely"][0]["values"]
            temp = current_values.get("temperature", "N/A")
            prob = current_values.get("precipitationProbability", 0)
            code = current_values.get("weatherCode", 1000)

            code_str = str(code)
            base_code = code_str[:4]

            icon_suffix = code_str if len(code_str) >= 5 else f"{code_str}0"
            icon_url = f"https://www.tomorrow.io/v1/static/assets/weather_icons/v2/color/{icon_suffix}.png"

            info = WEATHER_MESSAGES.get(
                base_code, {"label": f"未知({code_str})", "emoji": "🌡️"}
            )
            color = COLOR_MAP.get(base_code[0], 0x2F3136)

            embed = discord.Embed(
                title=f"🌡️ {city} 实时天气报告",
                description=f"当前状态：**{info['label']} {info['emoji']}**",
                color=color,
                timestamp=ctx.message.created_at,
            )
            embed.set_thumbnail(url=icon_url)
            embed.add_field(name="🌡️ 当前温度", value=f"{temp}°C", inline=True)
            embed.add_field(name="💧 降水概率", value=f"{prob}%", inline=True)
            embed.set_footer(
                text="数据来源: Tomorrow.io",
                icon_url="https://www.tomorrow.io/favicon.ico",
            )

            await ctx.send(embed=embed)

        except (KeyError, IndexError) as e:
            await ctx.send(f"❌ 解析天气数据失败。")


async def setup(bot):
    await bot.add_cog(WeatherCog(bot))
