import disnake
import os
import sys
import json
import datetime
import asyncio
from disnake.ext import commands


if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)


class emojiAdder(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.cooldown = 0

  
  @commands.Cog.listener()
  async def on_message(self, message):


    welcAliasList = ['welcome', 'welc', 'benvenuto', 'benv']
    snipyAliasList = ['Snipy', 'snipy', 'SNIPY', 'snipo', 'snaipi', 'Snaipi', 'SNAIPI', 'Snipo', 'SNIPO']
    zenoAliasList = ['zeno', 'zen']
    tommiAliasList = ['tomm', 'tommy']
    starsAliasList = ['stars']
    bipolarAliasList = ['bipo', 'bipolar']
    lilithAliasList = ['lilith', 'lili']
    enderAliasList = ['ender', 'endy']
    egoAliasList = ['ego', 'eghy']


    
    
    if message.author.id == 948229353077112872:
      return

    
    if self.cooldown == 0:
      
      if message.content.lower() in welcAliasList:
          emoji = '<:IRUSUWe  lcomeSign:879051616760791081>'
          await asyncio.sleep(1)
          await message.add_reaction(emoji)
          self.cooldown = 1
          await asyncio.sleep(2)
          self.cooldown = 0
  
      elif message.content.lower() in zenoAliasList:
          emoji = '<:IRUSUzeno:947985467146657842>'
          await asyncio.sleep(1)
          await message.add_reaction(emoji)
          self.cooldown = 1
          await asyncio.sleep(5)
          self.cooldown = 0
  
      elif message.content.lower() in tommiAliasList:
          emoji = '<:IRUSUtommisediadiash:947455526130843708>'
          await asyncio.sleep(1)
          await message.add_reaction(emoji)
          self.cooldown = 1
          await asyncio.sleep(5)
          self.cooldown = 0
  
      elif message.content.lower() in starsAliasList:
          emoji = '🧜🏼‍♀️'
          await asyncio.sleep(1)
          await message.add_reaction(emoji)
          self.cooldown = 1
          await asyncio.sleep(5)
          self.cooldown = 0
  
      elif message.content.lower() in bipolarAliasList:
        emoji = '<a:IRUSUbipolar:955541375624032347>'
        await asyncio.sleep(1)
        await message.add_reaction(emoji)
        self.cooldown = 1
        await asyncio.sleep(5)
        self.cooldown = 0

      elif message.content.lower() == 'luca':
        await asyncio.sleep(1)
        await message.add_reaction("<a:IRUSUkirbydance:972546070112505856>")
        self.cooldown = 1
        await asyncio.sleep(5)
        self.cooldown = 0
  
      elif message.content in snipyAliasList:
        emoji = '<:IRUSUcosce2:950398433854881822>'
        await asyncio.sleep(1)
        await message.add_reaction(emoji)
        self.cooldown = 1
        await asyncio.sleep(5)
        self.cooldown = 0
  
      elif message.content.lower() in lilithAliasList:
        emoji = '<a:IRUSULili:946436228440535050>'
        await asyncio.sleep(1)
        await message.add_reaction(emoji)
        self.cooldown = 1
        await asyncio.sleep(5)
        self.cooldown = 0
  
      elif message.content.lower() in enderAliasList:
        emoji = '<:IRUSUKannaSip:915978690918227998>'
        await asyncio.sleep(1)
        await message.add_reaction(emoji)
        self.cooldown = 1
        await asyncio.sleep(5)
        self.cooldown = 0
  
      elif message.content.lower() in egoAliasList:
        emoji = '<:IRUSUego:962636219701944330>'
        await asyncio.sleep(1)
        await message.add_reaction(emoji)
        self.cooldown = 1
        await asyncio.sleep(5)
        self.cooldown = 0
  
      
      if message.content.lower() == 'bas':
        await asyncio.sleep(1)
        await message.reply('il + pazzo')
        self.cooldown = 1
        await asyncio.sleep(5)
        self.cooldown = 0

      
      elif message.content.lower() == 'katia':
        await asyncio.sleep(1)
        await message.reply('hatia <:IRUSUkatia:963796346995880028>')
        self.cooldown = 1
        await asyncio.sleep(5)
        self.cooldown = 0
  
      elif message.content.lower() == 'ash':
        await asyncio.sleep(1)
        await message.add_reaction('<:IRUSUcosce1:950398433963941928>')
        self.cooldown = 1
        await asyncio.sleep(5)
        self.cooldown = 0
  
      elif message.content.lower() == 'skio':
        await asyncio.sleep(1)
        await message.add_reaction('<:IRUSUKannaWaaaa:881957807857999942>')
        self.cooldown = 1
        await asyncio.sleep(5)
        self.cooldown = 0

      elif '306899711351324693' in str(message.content):
        await asyncio.sleep(1)
        await message.add_reaction("<a:IRUSULeon:971006241507803147>")
        self.cooldown = 1
        await asyncio.sleep(5)
        self.cooldown = 0
  
      elif message.content.lower() == 'faffy':
        await asyncio.sleep(1)
        await message.add_reaction('<a:IRUSUgattofuffy:964210896018751548>')
        self.cooldown = 1
        await asyncio.sleep(5)
        self.cooldown = 0
    
    elif self.cooldown == 1:
      return

    
def setup(bot):
  bot.add_cog(emojiAdder(bot))