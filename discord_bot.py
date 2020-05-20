import discord
from discord.ext import commands
import aiml
import asyncio
import os

assert os.path.isfile("TOKEN")
with open("TOKEN", "r") as file:
    TOKEN = file.read().strip()

#  載入Alice核心
os.chdir('alice')
alice = aiml.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')

bot = commands.Bot(command_prefix="//")  # 設定//為指令

@bot.event
async def on_ready():
    """
    確認機器人上線
    """
    print("Bot is ready.")


@bot.event
async def on_member_join(member):
    """
    在頻道發送加入伺服器訊息
    """
    channel = bot.get_channel(698895507992346674)
    await channel.send(f'{member} join ! ')



@bot.event
async def on_member_remove(member):
    """
    在頻道發送離開伺服器訊息
    """
    channel = bot.get_channel(698895507992346674)
    await channel.send(f'{member} leave ! ')


# ---------命令區-------------


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')


@bot.command()
async def chat(ctx, *args):
    """
    聊天功能
    """
    RetMsg = alice.respond(" ".join(args).lstrip())
    await ctx.send(RetMsg)

# 執行機器人
if __name__ == "__main__":
    bot.run(TOKEN)
    
