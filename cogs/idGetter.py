import disnake
import os
import sys
import json
import subprocess
from disnake.ext import commands


if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)


class channelid(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['getidchannel', 'idgetchannel', 'idchannel', 'irusuchannelid', 'channelid'])
  async def channel(self, ctx, canale=None):

    if canale == None:
      await ctx.reply(":x: Devi indicare un canale per poterne ottenere l'ID")
      return

    if '#' in canale:
      canale1 = canale[2:len(canale)-1]
      embed = disnake.Embed(
        title='ID del canale',
        color=disnake.Color.from_rgb(255, 209, 220),
        description=f"<#{canale1}>"
      )

      embed.add_field(
        name='Sintassi',
        value=f'`{canale}`',
        inline=False
      )

      embed.add_field(
        name='ID',
        value=f'`{canale1}`',
        inline=False
      )
      await ctx.reply(embed=embed)

    #implementa la ricerca dei canali passando solamente il     nome
    else:
      pass

  @commands.command(aliases=['getidemoji', 'idgetemoji', 'idemoji', 'irusuemojiid', 'emojiid'])
  async def emoji(self, ctx, emoji=None):

    if emoji == None:
      await ctx.reply(":x: Devi indicare un emoji per poterne ottenere l'ID")
      return

    if ':' in emoji:
      emoji1 = f"\{emoji}"
      
      emojiOut = emoji1[len(emoji)-18:len(emoji)]
      embed = disnake.Embed(
        title="ID dell'emoji",
        color=disnake.Color.from_rgb(255, 209, 220),
        description=f"{emoji}"
      )

      embed.add_field(
        name='Sintassi', 
        value=f'`{emoji1[1:]}`', 
        inline=False
      )
      embed.add_field(
        name='ID',
        value=f'`{emojiOut}`',
        inline=False
      )
      
      await ctx.reply(embed=embed)
      
def setup(bot):
  bot.add_cog(channelid(bot))