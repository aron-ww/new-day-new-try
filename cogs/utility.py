import discord
from discord.ext import commands
from discord import app_commands

EMBED_GIF = "https://i.gifer.com/origin/60/606dc4f509be21ae620b538570dc1417_w200.gif"
FOOTER = "Coded with ❤️ by aron.ww"

class UtilityCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title="PING", description="Command `ping` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="ping", description="Command `ping` executed.")
    async def slash_ping(self, interaction: discord.Interaction):
        embed = discord.Embed(title="PING", description="Command `ping` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="HELP", description="Command `help` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="help", description="Command `help` executed.")
    async def slash_help(self, interaction: discord.Interaction):
        embed = discord.Embed(title="HELP", description="Command `help` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def avatar(self, ctx):
        embed = discord.Embed(title="AVATAR", description="Command `avatar` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="avatar", description="Command `avatar` executed.")
    async def slash_avatar(self, interaction: discord.Interaction):
        embed = discord.Embed(title="AVATAR", description="Command `avatar` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def banner(self, ctx):
        embed = discord.Embed(title="BANNER", description="Command `banner` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="banner", description="Command `banner` executed.")
    async def slash_banner(self, interaction: discord.Interaction):
        embed = discord.Embed(title="BANNER", description="Command `banner` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def userinfo(self, ctx):
        embed = discord.Embed(title="USERINFO", description="Command `userinfo` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="userinfo", description="Command `userinfo` executed.")
    async def slash_userinfo(self, interaction: discord.Interaction):
        embed = discord.Embed(title="USERINFO", description="Command `userinfo` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def serverinfo(self, ctx):
        embed = discord.Embed(title="SERVERINFO", description="Command `serverinfo` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="serverinfo", description="Command `serverinfo` executed.")
    async def slash_serverinfo(self, interaction: discord.Interaction):
        embed = discord.Embed(title="SERVERINFO", description="Command `serverinfo` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def uptime(self, ctx):
        embed = discord.Embed(title="UPTIME", description="Command `uptime` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="uptime", description="Command `uptime` executed.")
    async def slash_uptime(self, interaction: discord.Interaction):
        embed = discord.Embed(title="UPTIME", description="Command `uptime` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def remind(self, ctx):
        embed = discord.Embed(title="REMIND", description="Command `remind` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="remind", description="Command `remind` executed.")
    async def slash_remind(self, interaction: discord.Interaction):
        embed = discord.Embed(title="REMIND", description="Command `remind` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def timer(self, ctx):
        embed = discord.Embed(title="TIMER", description="Command `timer` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="timer", description="Command `timer` executed.")
    async def slash_timer(self, interaction: discord.Interaction):
        embed = discord.Embed(title="TIMER", description="Command `timer` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)



async def setup(bot):
    await bot.add_cog(UtilityCommands(bot))
