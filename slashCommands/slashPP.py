import disnake
import os
import sys
import json
import random
from disnake.ext import commands


if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)


class slashPP(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(description="Invia la lunghezza del PP di un utente.")
  async def penis(self, inter, member: disnake.Member = None):
    x = random.randint(1, 15)

    if inter.author.avatar != None:
      interAuthorAvatar = inter.author.avatar

    elif inter.author.avatar == None:
      interAuthorAvatar = inter.author.default_avatar
    
    if member == None:

      if inter.author.id == 710570210159099984:
        embed = disnake.Embed(
          title='PP of my master, Snipy-sama',
          description=f"8{'='*35}D",
          color=disnake.Color.from_rgb(255, 209, 220)
        )
        embed.set_author(name=f"{inter.author.display_name}#{inter.author.discriminator}", icon_url=f"{interAuthorAvatar}")
        
        await inter.response.send_message(f"<@!{inter.author.id}>", embed=embed)
        return
      
      embed = disnake.Embed(
          title=f"PP of {inter.author.display_name}#{inter.author.discriminator}",
          description=f"8{'='*x}D",
          color=disnake.Color.from_rgb(255, 209, 220)
        )
      embed.set_author(name=f"{inter.author.display_name}#{inter.author.discriminator}", icon_url=f"{interAuthorAvatar}")
      
      await inter.response.send_message(embed=embed)
    

    elif member != None:
      
      if inter.author.avatar != None:
        interAuthorAvatar = inter.author.avatar

      elif inter.author.avatar == None:
        interAuthorAvatar = inter.author.default_avatar
    
      
      if member.id == 710570210159099984:
        embed = disnake.Embed(
          title='PP of my master, Snipy-sama',
          description=f"8{'='*35}D",
          color=disnake.Color.from_rgb(255, 209, 220)
        )
        embed.set_author(name=f"{inter.author.display_name}#{inter.author.discriminator}", icon_url=f"{interAuthorAvatar}")
        
        await inter.response.send_message(embed=embed)

      else:
        embed = disnake.Embed(
          title=f"PP of {member.display_name}#{member.discriminator}",
          description=f"8{'='*x}D",
          color=disnake.Color.from_rgb(255, 209, 220)
        )
        embed.set_author(name=f"{inter.author.display_name}#{inter.author.discriminator}", icon_url=f"{interAuthorAvatar}")
      
        await inter.response.send_message(embed=embed)

    
def setup(bot):
  bot.add_cog(slashPP(bot))