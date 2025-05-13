import discord
from discord.ext import commands
from discord import app_commands

EMBED_GIF = "https://i.gifer.com/origin/60/606dc4f509be21ae620b538570dc1417_w200.gif"
FOOTER = "Coded with ❤️ by aron.ww"

class RpgCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def adventure(self, ctx):
        embed = discord.Embed(title="ADVENTURE", description="Command `adventure` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="adventure", description="Command `adventure` executed.")
    async def slash_adventure(self, interaction: discord.Interaction):
        embed = discord.Embed(title="ADVENTURE", description="Command `adventure` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def hunt(self, ctx):
        embed = discord.Embed(title="HUNT", description="Command `hunt` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="hunt", description="Command `hunt` executed.")
    async def slash_hunt(self, interaction: discord.Interaction):
        embed = discord.Embed(title="HUNT", description="Command `hunt` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def beg(self, ctx):
        embed = discord.Embed(title="BEG", description="Command `beg` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="beg", description="Command `beg` executed.")
    async def slash_beg(self, interaction: discord.Interaction):
        embed = discord.Embed(title="BEG", description="Command `beg` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def balance(self, ctx):
        embed = discord.Embed(title="BALANCE", description="Command `balance` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="balance", description="Command `balance` executed.")
    async def slash_balance(self, interaction: discord.Interaction):
        embed = discord.Embed(title="BALANCE", description="Command `balance` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def deposit(self, ctx):
        embed = discord.Embed(title="DEPOSIT", description="Command `deposit` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="deposit", description="Command `deposit` executed.")
    async def slash_deposit(self, interaction: discord.Interaction):
        embed = discord.Embed(title="DEPOSIT", description="Command `deposit` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def withdraw(self, ctx):
        embed = discord.Embed(title="WITHDRAW", description="Command `withdraw` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="withdraw", description="Command `withdraw` executed.")
    async def slash_withdraw(self, interaction: discord.Interaction):
        embed = discord.Embed(title="WITHDRAW", description="Command `withdraw` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def shop(self, ctx):
        embed = discord.Embed(title="SHOP", description="Command `shop` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="shop", description="Command `shop` executed.")
    async def slash_shop(self, interaction: discord.Interaction):
        embed = discord.Embed(title="SHOP", description="Command `shop` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def buy(self, ctx):
        embed = discord.Embed(title="BUY", description="Command `buy` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="buy", description="Command `buy` executed.")
    async def slash_buy(self, interaction: discord.Interaction):
        embed = discord.Embed(title="BUY", description="Command `buy` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def inventory(self, ctx):
        embed = discord.Embed(title="INVENTORY", description="Command `inventory` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="inventory", description="Command `inventory` executed.")
    async def slash_inventory(self, interaction: discord.Interaction):
        embed = discord.Embed(title="INVENTORY", description="Command `inventory` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def sell(self, ctx):
        embed = discord.Embed(title="SELL", description="Command `sell` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="sell", description="Command `sell` executed.")
    async def slash_sell(self, interaction: discord.Interaction):
        embed = discord.Embed(title="SELL", description="Command `sell` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)



async def setup(bot):
    await bot.add_cog(RpgCommands(bot))
