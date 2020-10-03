#Import Discord Package
import discord
from discord.ext import commands
import asyncio
import glob
from dotenv import load_dotenv
import os

load_dotenv() # Load your Discord Token

TOKEN = os.getenv("TOKEN") 

bot = commands.Bot(command_prefix='.',case_insensitive=True)

print('Ready!')

@bot.command()
async def wew(ctx):

    await ctx.message.delete()
    channel = ctx.author.voice.channel
    print(channel)
    await channel.connect()
    vc = ctx.voice_client

    counter = 0

    song = ("wow.mp3")
    vc.play(discord.FFmpegPCMAudio(song))
    while vc.is_playing():
        await asyncio.sleep(1)
        counter = counter + 1
    await vc.disconnect()

@bot.command()
async def thicc(ctx):

    await ctx.message.delete()
    channel = ctx.author.voice.channel
    print(channel)
    await channel.connect()
    vc = ctx.voice_client

    counter = 0

    song = ("THICC.mp3")
    vc.play(discord.FFmpegPCMAudio(song))
    while vc.is_playing():
        await asyncio.sleep(1)
        counter = counter + 1
    await vc.disconnect()
    

@bot.command()
async def woof(ctx):
    
    await ctx.message.delete()
    channel = ctx.author.voice.channel
    print(channel)
    await channel.connect()
    vc = ctx.voice_client

    counter = 0

    song = ("barks.mp3")
    vc.play(discord.FFmpegPCMAudio(song))
    while vc.is_playing():
        await asyncio.sleep(1)
        counter = counter + 1
    await vc.disconnect()


@bot.command()
async def welcome(ctx):
    
    await ctx.message.delete()
    channel = ctx.author.voice.channel
    print(channel)
    await channel.connect()
    vc = ctx.voice_client

    counter = 0

    song = ("Welcome.mp3")
    vc.play(discord.FFmpegPCMAudio(song))
    while vc.is_playing():
        await asyncio.sleep(1)
        counter = counter + 1
    await vc.disconnect()


@bot.command()
async def grapefruit(ctx):
    
    await ctx.message.delete()
    channel = ctx.author.voice.channel
    print(channel)
    await channel.connect()
    vc = ctx.voice_client

    counter = 0

    song = ("grapefruit.mp3")
    vc.play(discord.FFmpegPCMAudio(song))
    while vc.is_playing():
        await asyncio.sleep(1)
        counter = counter + 1
    await vc.disconnect()

@bot.command()
async def hello(ctx):
    
    await ctx.message.delete()
    channel = ctx.author.voice.channel
    print(channel)
    await channel.connect()
    vc = ctx.voice_client

    counter = 0

    song = ("hello.mp3")
    vc.play(discord.FFmpegPCMAudio(song))
    while vc.is_playing():
        await asyncio.sleep(1)
        counter = counter + 1
    await vc.disconnect()




bot.run (TOKEN)
