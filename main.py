import os
import json
import sys
import disnake
from disnake.ext.commands import Bot
from pymongo import MongoClient
import pymongo


### pip install -U git+https://github.com/Chromosomologist/disnake-ext-components

#web server
from keep_alive import keep_alive

if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)

def get_prefix(bot, message):
  with open("config.json", "r") as f:  prefixes = json.load(f)
  return prefixes[str(message.guild.id)]["prefix"]

intents = disnake.Intents.all()
bot = Bot(
  command_prefix=get_prefix, 
  intents=intents, 
  help_command=None, 
  case_insensitive=True,
  sync_commands_debug=True,
  test_guilds=[877130463662182410]
)
TOKEN = os.environ['TOKEN']
prefix = config['877130463662182410']['prefix']

@bot.event
async def on_ready():
  print(f"Logged in as {bot.user}", "\nI'm alive")

@bot.command()
async def load(ctx, exstension):
  bot.load_extension(f"cogs.{extension}")
  bot.load_extension(f"slashCommands.{extension}")

@bot.command()
async def unload(ctx, exstension):
  bot.unload_extension(f"cogs.{extension}")
  bot.unload_extension(f"slashCommands.{extension}")

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

for slashName in os.listdir('./slashCommands'):
  if slashName.endswith('.py'):
    bot.load_extension(f'slashCommands.{slashName[:-3]}')


keep_alive()
bot.run(TOKEN, reconnect=True)
