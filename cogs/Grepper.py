from discord.ext import commands
import discord
from discord import Option
import requests
import json

class Grepper(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.slash_command(
        name="grepper",
        description="Grepper command",
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def grepper(
        self, 
        ctx,
        query: Option(str, "The query you want to search using Grepper", required=True),
    ):
        # we get answers from Grepper API based on the user's input
        API_VERSION = 3
        API = f'https://www.codegrepper.com/api/search.php?version={API_VERSION}&q={query}'
        print(API)

        # we get the answers
        response = requests.get(API)

        # we convert the response to json
        query_answers = json.loads(response.text)

        # we create an embed
        embed = discord.Embed(
            title="Grepper Bot",
            description="Here are the answers from Grepper for your query",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url="https://d2441bdvuxbh7t.cloudfront.net/web/images/grepper_and_logo.jpeg")
        embed.add_field(name=f'Query : {query}', value=f'Number of answers (__Max 5__) : {len(query_answers["answers"])}', inline=False)
        if len(query_answers["answers"]) > 0 :
            for i in range(min(5, len(query_answers["answers"]))):
                embed.add_field(name=f'Answer n°{i+1}', value=f':bust_in_silhouette: **Author :** __{query_answers["answers"][i]["fun_name"]}__', inline=True)
                embed.add_field(name=f':thumbsup: Upvotes : {query_answers["answers"][i]["t_upvotes"]}', value=f':thumbsdown: **Downvotes : {query_answers["answers"][i]["t_downvotes"]}** ', inline=True)
                embed.add_field(name=f'**Content : **', value=f'```{query_answers["answers"][i]["answer"]}```', inline=False)
        else:
            embed.add_field(name=f'No answers found for your query : {query}', value=f'Please try again with another query', inline=False)

        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Grepper(bot))