import discord, aiohttp, os 

from discord.ext import commands 

 

client = commands.Bot(command_prefix="f54f2163542a9d0df01264dfe", intents=discord.Intents().all(), activity=discord.Activity(type=discord.ActivityType.watching, name="radoutil.instatus.com")) 

BotWebhook = os.environ['BotWebhook'] 

BotWebhook2 = os.environ['BotWebhook2'] 

 

 

@client.event 

async def on_ready(): 

print(f'Logged in as {client.user.name}#{client.user.discriminator} ({client.user.id})') 

 

@client.event 

async def on_member_update(before, after): 

if before.id == 880012534726393886 and before.status != after.status: 

if str(after.status) == 'offline': 

async with aiohttp.ClientSession() as session: 

async with session.post(BotWebhook, json={ 

"trigger": "down", 

"name": "Rado's Utilites is offline", 

"message": "Rado's Utilites is offline unexpectedly. Please wait until the owner fix the bot.", 

"status": "MAJOROUTAGE" 

}) as resp: 

print(resp) 

elif str(after.status) == 'online': 

async with aiohttp.ClientSession() as session: 

async with session.post(BotWebhook, json={ 

"trigger": "up", 

"name": "Rado's Utilites is online", 

"message": "Rado's Utilites is back online.", 

"status": "OPERATIONAL" 

}) as resp: 

print(resp) 

if before.id == 881784880516706314 and before.status != after.status: 

if str(after.status) == 'offline': 

async with aiohttp.ClientSession() as session: 

async with session.post(BotWebhook, json={ 

"trigger": "down", 

"name": "Rado's Utilites is offline", 

"message": "Rado's Utilites 2 is offline unexpectedly. Please wait until MEE6 owner fix the bot.", 

"status": "MAJOROUTAGE" 

}) as resp: 

print(resp) 

elif str(after.status) == 'online': 

async with aiohttp.ClientSession() as session: 

async with session.post(BotWebhook, json={ 

"trigger": "up", 

"name": "Rado's Utilites is online", 

"message": "Rado's Utilites 2 is back online.", 

"status": "OPERATIONAL" 

}) as resp: 

print(resp) 

 

client.run(os.environ["TOKEN"])

