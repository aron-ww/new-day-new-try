import discord
from discord.ext import commands
from discord import app_commands

EMBED_GIF = "https://i.gifer.com/origin/60/606dc4f509be21ae620b538570dc1417_w200.gif"
FOOTER = "Coded with ❤️ by aron.ww"

class ExtraCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def cmd1(self, ctx):
        embed = discord.Embed(title="CMD1", description="Command `cmd1` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd1", description="Command `cmd1` executed.")
    async def slash_cmd1(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD1", description="Command `cmd1` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd2(self, ctx):
        embed = discord.Embed(title="CMD2", description="Command `cmd2` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd2", description="Command `cmd2` executed.")
    async def slash_cmd2(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD2", description="Command `cmd2` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd3(self, ctx):
        embed = discord.Embed(title="CMD3", description="Command `cmd3` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd3", description="Command `cmd3` executed.")
    async def slash_cmd3(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD3", description="Command `cmd3` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd4(self, ctx):
        embed = discord.Embed(title="CMD4", description="Command `cmd4` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd4", description="Command `cmd4` executed.")
    async def slash_cmd4(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD4", description="Command `cmd4` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd5(self, ctx):
        embed = discord.Embed(title="CMD5", description="Command `cmd5` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd5", description="Command `cmd5` executed.")
    async def slash_cmd5(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD5", description="Command `cmd5` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd6(self, ctx):
        embed = discord.Embed(title="CMD6", description="Command `cmd6` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd6", description="Command `cmd6` executed.")
    async def slash_cmd6(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD6", description="Command `cmd6` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd7(self, ctx):
        embed = discord.Embed(title="CMD7", description="Command `cmd7` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd7", description="Command `cmd7` executed.")
    async def slash_cmd7(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD7", description="Command `cmd7` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd8(self, ctx):
        embed = discord.Embed(title="CMD8", description="Command `cmd8` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd8", description="Command `cmd8` executed.")
    async def slash_cmd8(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD8", description="Command `cmd8` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd9(self, ctx):
        embed = discord.Embed(title="CMD9", description="Command `cmd9` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd9", description="Command `cmd9` executed.")
    async def slash_cmd9(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD9", description="Command `cmd9` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd10(self, ctx):
        embed = discord.Embed(title="CMD10", description="Command `cmd10` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd10", description="Command `cmd10` executed.")
    async def slash_cmd10(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD10", description="Command `cmd10` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd11(self, ctx):
        embed = discord.Embed(title="CMD11", description="Command `cmd11` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd11", description="Command `cmd11` executed.")
    async def slash_cmd11(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD11", description="Command `cmd11` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd12(self, ctx):
        embed = discord.Embed(title="CMD12", description="Command `cmd12` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd12", description="Command `cmd12` executed.")
    async def slash_cmd12(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD12", description="Command `cmd12` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd13(self, ctx):
        embed = discord.Embed(title="CMD13", description="Command `cmd13` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd13", description="Command `cmd13` executed.")
    async def slash_cmd13(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD13", description="Command `cmd13` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd14(self, ctx):
        embed = discord.Embed(title="CMD14", description="Command `cmd14` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd14", description="Command `cmd14` executed.")
    async def slash_cmd14(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD14", description="Command `cmd14` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd15(self, ctx):
        embed = discord.Embed(title="CMD15", description="Command `cmd15` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd15", description="Command `cmd15` executed.")
    async def slash_cmd15(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD15", description="Command `cmd15` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd16(self, ctx):
        embed = discord.Embed(title="CMD16", description="Command `cmd16` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd16", description="Command `cmd16` executed.")
    async def slash_cmd16(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD16", description="Command `cmd16` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd17(self, ctx):
        embed = discord.Embed(title="CMD17", description="Command `cmd17` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd17", description="Command `cmd17` executed.")
    async def slash_cmd17(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD17", description="Command `cmd17` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd18(self, ctx):
        embed = discord.Embed(title="CMD18", description="Command `cmd18` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd18", description="Command `cmd18` executed.")
    async def slash_cmd18(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD18", description="Command `cmd18` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd19(self, ctx):
        embed = discord.Embed(title="CMD19", description="Command `cmd19` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd19", description="Command `cmd19` executed.")
    async def slash_cmd19(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD19", description="Command `cmd19` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd20(self, ctx):
        embed = discord.Embed(title="CMD20", description="Command `cmd20` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd20", description="Command `cmd20` executed.")
    async def slash_cmd20(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD20", description="Command `cmd20` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd21(self, ctx):
        embed = discord.Embed(title="CMD21", description="Command `cmd21` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd21", description="Command `cmd21` executed.")
    async def slash_cmd21(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD21", description="Command `cmd21` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd22(self, ctx):
        embed = discord.Embed(title="CMD22", description="Command `cmd22` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd22", description="Command `cmd22` executed.")
    async def slash_cmd22(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD22", description="Command `cmd22` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd23(self, ctx):
        embed = discord.Embed(title="CMD23", description="Command `cmd23` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd23", description="Command `cmd23` executed.")
    async def slash_cmd23(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD23", description="Command `cmd23` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd24(self, ctx):
        embed = discord.Embed(title="CMD24", description="Command `cmd24` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd24", description="Command `cmd24` executed.")
    async def slash_cmd24(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD24", description="Command `cmd24` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd25(self, ctx):
        embed = discord.Embed(title="CMD25", description="Command `cmd25` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd25", description="Command `cmd25` executed.")
    async def slash_cmd25(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD25", description="Command `cmd25` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd26(self, ctx):
        embed = discord.Embed(title="CMD26", description="Command `cmd26` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd26", description="Command `cmd26` executed.")
    async def slash_cmd26(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD26", description="Command `cmd26` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd27(self, ctx):
        embed = discord.Embed(title="CMD27", description="Command `cmd27` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd27", description="Command `cmd27` executed.")
    async def slash_cmd27(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD27", description="Command `cmd27` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd28(self, ctx):
        embed = discord.Embed(title="CMD28", description="Command `cmd28` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd28", description="Command `cmd28` executed.")
    async def slash_cmd28(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD28", description="Command `cmd28` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd29(self, ctx):
        embed = discord.Embed(title="CMD29", description="Command `cmd29` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd29", description="Command `cmd29` executed.")
    async def slash_cmd29(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD29", description="Command `cmd29` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd30(self, ctx):
        embed = discord.Embed(title="CMD30", description="Command `cmd30` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd30", description="Command `cmd30` executed.")
    async def slash_cmd30(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD30", description="Command `cmd30` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd31(self, ctx):
        embed = discord.Embed(title="CMD31", description="Command `cmd31` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd31", description="Command `cmd31` executed.")
    async def slash_cmd31(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD31", description="Command `cmd31` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd32(self, ctx):
        embed = discord.Embed(title="CMD32", description="Command `cmd32` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd32", description="Command `cmd32` executed.")
    async def slash_cmd32(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD32", description="Command `cmd32` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd33(self, ctx):
        embed = discord.Embed(title="CMD33", description="Command `cmd33` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd33", description="Command `cmd33` executed.")
    async def slash_cmd33(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD33", description="Command `cmd33` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd34(self, ctx):
        embed = discord.Embed(title="CMD34", description="Command `cmd34` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd34", description="Command `cmd34` executed.")
    async def slash_cmd34(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD34", description="Command `cmd34` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd35(self, ctx):
        embed = discord.Embed(title="CMD35", description="Command `cmd35` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd35", description="Command `cmd35` executed.")
    async def slash_cmd35(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD35", description="Command `cmd35` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd36(self, ctx):
        embed = discord.Embed(title="CMD36", description="Command `cmd36` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd36", description="Command `cmd36` executed.")
    async def slash_cmd36(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD36", description="Command `cmd36` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd37(self, ctx):
        embed = discord.Embed(title="CMD37", description="Command `cmd37` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd37", description="Command `cmd37` executed.")
    async def slash_cmd37(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD37", description="Command `cmd37` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd38(self, ctx):
        embed = discord.Embed(title="CMD38", description="Command `cmd38` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd38", description="Command `cmd38` executed.")
    async def slash_cmd38(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD38", description="Command `cmd38` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd39(self, ctx):
        embed = discord.Embed(title="CMD39", description="Command `cmd39` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd39", description="Command `cmd39` executed.")
    async def slash_cmd39(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD39", description="Command `cmd39` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd40(self, ctx):
        embed = discord.Embed(title="CMD40", description="Command `cmd40` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd40", description="Command `cmd40` executed.")
    async def slash_cmd40(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD40", description="Command `cmd40` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd41(self, ctx):
        embed = discord.Embed(title="CMD41", description="Command `cmd41` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd41", description="Command `cmd41` executed.")
    async def slash_cmd41(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD41", description="Command `cmd41` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd42(self, ctx):
        embed = discord.Embed(title="CMD42", description="Command `cmd42` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd42", description="Command `cmd42` executed.")
    async def slash_cmd42(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD42", description="Command `cmd42` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd43(self, ctx):
        embed = discord.Embed(title="CMD43", description="Command `cmd43` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd43", description="Command `cmd43` executed.")
    async def slash_cmd43(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD43", description="Command `cmd43` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd44(self, ctx):
        embed = discord.Embed(title="CMD44", description="Command `cmd44` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd44", description="Command `cmd44` executed.")
    async def slash_cmd44(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD44", description="Command `cmd44` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd45(self, ctx):
        embed = discord.Embed(title="CMD45", description="Command `cmd45` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd45", description="Command `cmd45` executed.")
    async def slash_cmd45(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD45", description="Command `cmd45` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd46(self, ctx):
        embed = discord.Embed(title="CMD46", description="Command `cmd46` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd46", description="Command `cmd46` executed.")
    async def slash_cmd46(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD46", description="Command `cmd46` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd47(self, ctx):
        embed = discord.Embed(title="CMD47", description="Command `cmd47` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd47", description="Command `cmd47` executed.")
    async def slash_cmd47(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD47", description="Command `cmd47` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd48(self, ctx):
        embed = discord.Embed(title="CMD48", description="Command `cmd48` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd48", description="Command `cmd48` executed.")
    async def slash_cmd48(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD48", description="Command `cmd48` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd49(self, ctx):
        embed = discord.Embed(title="CMD49", description="Command `cmd49` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd49", description="Command `cmd49` executed.")
    async def slash_cmd49(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD49", description="Command `cmd49` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)


    @commands.command()
    async def cmd50(self, ctx):
        embed = discord.Embed(title="CMD50", description="Command `cmd50` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await ctx.send(embed=embed)

    @app_commands.command(name="cmd50", description="Command `cmd50` executed.")
    async def slash_cmd50(self, interaction: discord.Interaction):
        embed = discord.Embed(title="CMD50", description="Command `cmd50` executed.", color=0x00ffcc)
        embed.set_thumbnail(url=EMBED_GIF)
        embed.set_footer(text=FOOTER)
        await interaction.response.send_message(embed=embed)



async def setup(bot):
    await bot.add_cog(ExtraCommands(bot))
