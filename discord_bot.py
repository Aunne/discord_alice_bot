import discord
from discord.ext import commands
import aiml
import asyncio
import os

os.chdir('alice')
alice = aiml.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')

TOKEN="Njk4NDIxMTM3MjY4Mjc3Mjc4.Xq51kw.qqEB-wImFdR2I5R7ODBDdj_QWc0"

client = discord.Client()
bot=commands.Bot(command_prefix="//") #設定//為指令


@bot.event
async def on_ready() :
    print("Bot is ready.")
#確認機器人上線

@bot.event
async def on_member_join(member) :
    channel = bot.get_channel(698895507992346674)
    await channel.send(f'{member} join ! ')
#在頻道發送加入伺服器訊息

@bot.event
async def on_member_remove(member) :
    channel = bot.get_channel(698895507992346674)
    await channel.send(f'{member} leave ! ')
#在頻道發送離開伺服器訊息

#---------命令區-------------

@bot.command()
async def ping(ctx) :
    await ctx.send(f'{round(bot.latency*1000)} ms')

@bot.command()
async def chat(ctx,ClientMessage) : 
  RetMsg = alice.respond(ClientMessage)
  await ctx.send(RetMsg)
  

bot.run(TOKEN) 
#執行機器人