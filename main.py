import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX", ".")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands")
    except Exception as e:
        print(f"Error syncing commands: {e}")

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)

# ──────────────────────────────────────
# Fake web server to keep Render alive
# ──────────────────────────────────────
import threading
from flask import Flask
from waitress import serve

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    serve(app, host="0.0.0.0", port=8080)

threading.Thread(target=run_web).start()
# ──────────────────────────────────────

