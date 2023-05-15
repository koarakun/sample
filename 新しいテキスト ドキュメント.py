import asyncio
from ctypes import Union
import datetime
from typing import List
import discord
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print("起動完了")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)}個のコマンドを同期しました")
    except Exception as e:
        print(f"同期エラーが発生しました: {e}")

# slashコマンドの基本
@bot.tree.command(name="hello", description="slashコマンドの基本形です")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello World!")

bot.run("トークン")