import discord
from discord.ext import commands
from decouple import config

from utils import *

#token
discord_api_key = config('DISCORD_BOT_TOKEN')

# initialize bot
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# here, on_ready() tells that bot is ready to receive command
# This is for testing
@client.event
async def on_ready():
    print("The bot is now ready for use")
    print("-----------------------------")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Reading participant data
    if message.content.lower().startswith("!evalbot new event"):
        print("First if-else block")
        if message.author.id == message.channel.guild.owner_id:
            response = await eventData(message)
            await message.channel.send(response)

    # Adding tokens
    elif message.content.lower().startswith("!evalbot add token"):
        if message.author.id == message.channel.guild.owner_id:
            amount = int(str(message.content).split("\n")[1])
            username = "abhunia."
            # command = f"t@points add @{username} {amount}"
            command = f"t!points @{username}"
            await message.channel.send(command)

    # delete event from database
    elif message.content.lower().startswith("!evalbot delete event"):
        if message.author.id == message.channel.guild.owner_id:
            response = await delete_event(message)
            await message.channel.send(response)

    # Checking the desired Format
    elif message.content.lower().startswith("!evalbot"):
        response = await fomatting_check(message)
        await message.channel.send(response)


@client.event
async def on_message_edit(before, after):
    if after.author == client.user:
        return
    if after.content.lower().startswith("!evalbot new event"):
        if after.author.id == after.channel.guild.owner_id:
            response = await eventData(after)
            await after.channel.send(response)
    elif after.content.lower().startswith("!evalbot"):
        response = await fomatting_check(after)
        await after.channel.send (response)

# it tells the bot to run
client.run(discord_api_key)