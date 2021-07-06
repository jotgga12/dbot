
import discord

from random import *
import time


client=discord.Client()

token="ODYxOTIwMTMwNTkzNTg3MjQw.YOQzrA.5c3Aq5QrEFwY9Z5NvaSp7jMcugc"

@client.event
async def on_ready():
    print(client.user.name)
    print("성공적으로 봇이 시작됨")
    game=discord.Game("주식")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
   
    if message.content.startswith(">주식"):
        while True:
            joosick=randint(3000,5000)
            await message.channel.send(joosick)
            await message.channel.send("3분후 가격이 변동됩니다")
            time.sleep(150)

client.run(token)