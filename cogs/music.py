import discord
from discord.ext import commands
from discord import app_commands

EMBED_GIF = "https://i.gifer.com/origin/60/606dc4f509be21ae620b538570dc1417_w200.gif"
FOOTER = "Coded with ❤️ by aron.ww"

class MusicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def play(self, ctx):
        embed = discord.Embed(title="PLAY", description="Command `play` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="play", description="Command `play` executed.")
    async def slash_play(self, interaction: discord.Interaction):
        embed = discord.Embed(title="PLAY", description="Command `play` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def pause(self, ctx):
        embed = discord.Embed(title="PAUSE", description="Command `pause` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="pause", description="Command `pause` executed.")
    async def slash_pause(self, interaction: discord.Interaction):
        embed = discord.Embed(title="PAUSE", description="Command `pause` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def resume(self, ctx):
        embed = discord.Embed(title="RESUME", description="Command `resume` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="resume", description="Command `resume` executed.")
    async def slash_resume(self, interaction: discord.Interaction):
        embed = discord.Embed(title="RESUME", description="Command `resume` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def stop(self, ctx):
        embed = discord.Embed(title="STOP", description="Command `stop` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="stop", description="Command `stop` executed.")
    async def slash_stop(self, interaction: discord.Interaction):
        embed = discord.Embed(title="STOP", description="Command `stop` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def queue(self, ctx):
        embed = discord.Embed(title="QUEUE", description="Command `queue` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="queue", description="Command `queue` executed.")
    async def slash_queue(self, interaction: discord.Interaction):
        embed = discord.Embed(title="QUEUE", description="Command `queue` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def skip(self, ctx):
        embed = discord.Embed(title="SKIP", description="Command `skip` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="skip", description="Command `skip` executed.")
    async def slash_skip(self, interaction: discord.Interaction):
        embed = discord.Embed(title="SKIP", description="Command `skip` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def nowplaying(self, ctx):
        embed = discord.Embed(title="NOWPLAYING", description="Command `nowplaying` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="nowplaying", description="Command `nowplaying` executed.")
    async def slash_nowplaying(self, interaction: discord.Interaction):
        embed = discord.Embed(title="NOWPLAYING", description="Command `nowplaying` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def volume(self, ctx):
        embed = discord.Embed(title="VOLUME", description="Command `volume` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="volume", description="Command `volume` executed.")
    async def slash_volume(self, interaction: discord.Interaction):
        embed = discord.Embed(title="VOLUME", description="Command `volume` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def lyrics(self, ctx):
        embed = discord.Embed(title="LYRICS", description="Command `lyrics` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="lyrics", description="Command `lyrics` executed.")
    async def slash_lyrics(self, interaction: discord.Interaction):
        embed = discord.Embed(title="LYRICS", description="Command `lyrics` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)



async def setup(bot):
    await bot.add_cog(MusicCommands(bot))
