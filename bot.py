from discord.utils import get
#from discord import FFmpegPCMAudio

import asyncio

from discord.ext.commands import Greedy
from discord import User


# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="$")


# ON_MESSAGE() EVENT LISTENER. NOTICE IT IS USING @BOT.EVENT AS OPPOSED TO @BOT.COMMAND().
# @bot.event
# async def on_message(message):
#     # CHECK IF THE MESSAGE SENT TO THE CHANNEL IS "HELLO".
#     if message.content == "hello":
#         # SENDS A MESSAGE TO THE CHANNEL.
#         await message.channel.send("pies are better than cakes. change my mind.")
#
#     # INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
#     await bot.process_commands(message)



# COMMAND $PING. INVOKES ONLY WHEN THE MESSAGE "$PING" IS SEND IN THE DISCORD SERVER.
# ALTERNATIVELY @BOT.COMMAND(NAME="PING") CAN BE USED IF ANOTHER FUNCTION NAME IS DESIRED.
@bot.command(
    # ADDS THIS VALUE TO THE $HELP PING MESSAGE.
    help="Uses come crazy logic to determine if pong is actually the correct value or not.",
    # ADDS THIS VALUE TO THE $HELP MESSAGE.
    brief="Prints pong back to the channel."
)
async def ping(ctx):
    # SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
    await ctx.channel.send("pong")


# COMMAND $PRINT. THIS TAKES AN IN A LIST OF ARGUMENTS FROM THE USER AND SIMPLY PRINTS THE VALUES BACK TO THE CHANNEL.
@bot.command(
    # ADDS THIS VALUE TO THE $HELP PRINT MESSAGE.
    help="Looks like you need some help.",
    # ADDS THIS VALUE TO THE $HELP MESSAGE.
    brief="Prints the list of values back to the channel."
)
async def print(ctx, *args):
    response = ""

    # LOOPS THROUGH THE LIST OF ARGUMENTS THAT THE USER INPUTS.
    for arg in args:
        response = response + " " + arg

    # SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
    await ctx.channel.send(response)

@bot.command(
    # ADDS THIS VALUE TO THE $HELP PING MESSAGE.
    help="WEUUUUUUUUUUUU.",
    # ADDS THIS VALUE TO THE $HELP MESSAGE.
    brief="Plays R2D2 screaming"
)
async def scream(ctx):
    id = str(ctx.message.author.id)
    channel = ctx.message.author.voice.channel
    if not channel:
        print("User tried to request voice bot, but was not in a voice channel")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await voice.disconnect()
    if voice and voice.is_connected():
        await voice.move_to(channel)
        print(f"The bot has moved to {channel}")
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}")

    voice.play(discord.FFmpegPCMAudio("sounds/r2d2.mp3"))


@bot.command(
    # ADDS THIS VALUE TO THE $HELP PING MESSAGE.
    help="cri.",
    # ADDS THIS VALUE TO THE $HELP MESSAGE.
    brief="Plays R2D2 screaming"
)
async def cry(ctx):
    id = str(ctx.message.author.id)
    channel = ctx.message.author.voice.channel
    if not channel:
        print("User tried to request voice bot, but was not in a voice channel")
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await voice.disconnect()
    if voice and voice.is_connected():
        await voice.move_to(channel)
        print(f"The bot has moved to {channel}")
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}")

    voice.play(discord.FFmpegPCMAudio("sounds/baby-cry.mp3"))




@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == 'Chill':
            await member.guild.system_channel.send("Alarm!")


@bot.command()
async def DM(ctx, user: discord.User, *, message=None):
    print(user)
    message = message or "This Message is sent via DM"
    # Be annoying and send the message one word at a time
    word_list = message.split(' ')
    for w in word_list:
        await user.send(w)

    # Be uber annoying and send one character at a time
    # for c in message:
    #     if c == " ":
    #         await user.send('­')
    #     else:
    #         await user.send(c)
    #await user.send(message)

@bot.command()
async def send_dm(ctx, member: discord.Member, *, content):
    print(f'Sending message to {discord.Member}')
    channel = await member.create_dm()
    await channel.send(content)


@bot.command()
async def pm(ctx, users: Greedy[User], *, message):
    for user in users:
        await user.send(message)


@bot.command()
async def ff(ctx, users: Greedy[User], *, value):
    # Send a message to the mentioned user!
    for user in users:
        print(users)
        await user.send(f"{value}")
    #await user.send(f"||Sent by {ctx.author.display_name} via VX Helper.||")


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)
