import discord
from discord.ext import commands
from discord import app_commands

EMBED_GIF = "https://i.gifer.com/origin/60/606dc4f509be21ae620b538570dc1417_w200.gif"
FOOTER = "Coded with ❤️ by aron.ww"

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def meme(self, ctx):
        embed = discord.Embed(title="MEME", description="Command `meme` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="meme", description="Command `meme` executed.")
    async def slash_meme(self, interaction: discord.Interaction):
        embed = discord.Embed(title="MEME", description="Command `meme` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def joke(self, ctx):
        embed = discord.Embed(title="JOKE", description="Command `joke` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="joke", description="Command `joke` executed.")
    async def slash_joke(self, interaction: discord.Interaction):
        embed = discord.Embed(title="JOKE", description="Command `joke` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def 8ball(self, ctx):
        embed = discord.Embed(title="8BALL", description="Command `8ball` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="8ball", description="Command `8ball` executed.")
    async def slash_8ball(self, interaction: discord.Interaction):
        embed = discord.Embed(title="8BALL", description="Command `8ball` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def roast(self, ctx):
        embed = discord.Embed(title="ROAST", description="Command `roast` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="roast", description="Command `roast` executed.")
    async def slash_roast(self, interaction: discord.Interaction):
        embed = discord.Embed(title="ROAST", description="Command `roast` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def compliment(self, ctx):
        embed = discord.Embed(title="COMPLIMENT", description="Command `compliment` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="compliment", description="Command `compliment` executed.")
    async def slash_compliment(self, interaction: discord.Interaction):
        embed = discord.Embed(title="COMPLIMENT", description="Command `compliment` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)



async def setup(bot):
    await bot.add_cog(FunCommands(bot))
