import discord
from discord.ext import commands
from discord import app_commands

EMBED_GIF = "https://i.gifer.com/origin/60/606dc4f509be21ae620b538570dc1417_w200.gif"
FOOTER = "Coded with ❤️ by aron.ww"

class ModerationCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ban(self, ctx):
        embed = discord.Embed(title="BAN", description="Command `ban` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="ban", description="Command `ban` executed.")
    async def slash_ban(self, interaction: discord.Interaction):
        embed = discord.Embed(title="BAN", description="Command `ban` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def kick(self, ctx):
        embed = discord.Embed(title="KICK", description="Command `kick` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="kick", description="Command `kick` executed.")
    async def slash_kick(self, interaction: discord.Interaction):
        embed = discord.Embed(title="KICK", description="Command `kick` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def mute(self, ctx):
        embed = discord.Embed(title="MUTE", description="Command `mute` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="mute", description="Command `mute` executed.")
    async def slash_mute(self, interaction: discord.Interaction):
        embed = discord.Embed(title="MUTE", description="Command `mute` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def unmute(self, ctx):
        embed = discord.Embed(title="UNMUTE", description="Command `unmute` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="unmute", description="Command `unmute` executed.")
    async def slash_unmute(self, interaction: discord.Interaction):
        embed = discord.Embed(title="UNMUTE", description="Command `unmute` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def purge(self, ctx):
        embed = discord.Embed(title="PURGE", description="Command `purge` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="purge", description="Command `purge` executed.")
    async def slash_purge(self, interaction: discord.Interaction):
        embed = discord.Embed(title="PURGE", description="Command `purge` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def purge_bots(self, ctx):
        embed = discord.Embed(title="PURGE_BOTS", description="Command `purge_bots` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="purge_bots", description="Command `purge_bots` executed.")
    async def slash_purge_bots(self, interaction: discord.Interaction):
        embed = discord.Embed(title="PURGE_BOTS", description="Command `purge_bots` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def unban(self, ctx):
        embed = discord.Embed(title="UNBAN", description="Command `unban` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="unban", description="Command `unban` executed.")
    async def slash_unban(self, interaction: discord.Interaction):
        embed = discord.Embed(title="UNBAN", description="Command `unban` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)



async def setup(bot):
    await bot.add_cog(ModerationCommands(bot))
