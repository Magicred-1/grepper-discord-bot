import discord
from discord.ext import commands

class Default(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.slash_command(
        name="ping",
        description="Pong!"
    )
    async def ping(self, ctx):
        embed=discord.Embed(
                title="Pong!",
                description=f"Bot latency : {round(self.bot.latency * 100, 2)}ms",
                color=discord.Color.green()
            )
        embed.set_thumbnail(url="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGVmMDc4N2Y0Y2VmMWMwNjgxYzFlNmY3ZGI4N2VkYjM3MWZlOGY3YiZjdD1n/aTGwuEFyg6d8c/giphy.gif")
        await ctx.respond(embed=embed)
            
def setup(bot):
    bot.add_cog(Default(bot))