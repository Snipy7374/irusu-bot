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


class avUltimate(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


  @commands.slash_command()
  async def avatar(self, ctx):
    return

    
  # AVATAR GUILD
  @avatar.sub_command(description="Ottieni l'avatar guild di un utente, se ne ha uno")
  async def guild(self, inter, user: disnake.Member = None):
    
    if user is None:

      if inter.author.guild_avatar is not None:
        authorGuildAvatar = inter.author.guild_avatar

      else:
        authorGuildAvatar = inter.author.default_avatar

      if inter.author.avatar is not None:
        authorAvatar = inter.author.avatar

      else:
        authorAvatar = inter.author.default_avatar

      embed = disnake.Embed(
        title=f'Avatar di {inter.author.display_name}',
        color=disnake.Color.from_rgb(255, 209, 220)
      )
      embed.set_author(
        name=f"{inter.author.name}#{inter.author.discriminator}", 
        icon_url=f"{authorAvatar}"
      )
      embed.set_image(url=f"{authorGuildAvatar}")
      await inter.response.send_message(embed=embed)


    elif user is not None:

      if user.guild_avatar is not None:
        memberGuildAvatar = user.guild_avatar

      else:
        memberGuildAvatar = user.default_avatar

      if inter.author.avatar is not None:
        authorAvatar = inter.author.avatar

      else:
        authorAvatar = inter.authror.default_avatar

      embed = disnake.Embed(
        title=f'Avatar Guild di {user.display_name}',
        color=disnake.Color.from_rgb(255, 209, 220)
      )
      embed.set_author(
        name=f"{inter.author.name}#{inter.author.discriminator}", 
        icon_url=f"{authorAvatar}"
      )
      embed.set_image(url=f"{memberGuildAvatar}")
      await inter.response.send_message(embed=embed)



      
  # USER BANNER
  @avatar.sub_command(description="Ottieni il banner di un utente, se ne ha uno")
  async def banner(self, inter, user: disnake.Member = None):

    if user is None:

      user = await self.bot.fetch_user(inter.author.id)
      
      if user.banner is None:
        embed = disnake.Embed(
          title="Errore!",
          description=":x: Questo membro non possiede un banner!",
          color=disnake.Color.from_rgb(255, 1, 57)
        )
        await inter.response.send_message(embed=embed)
        return
        
      elif user.banner is not None:
        ctxAuthorBanner = user.banner

        if inter.author.avatar is None:
          ctxAuthorAvatar = inter.author.default_avatar
        
        elif inter.author.avatar is not None:
          ctxAuthorAvatar = inter.author.avatar

      
      embed = disnake.Embed(
        title=f'Banner di {inter.author.display_name}',
        color=disnake.Color.from_rgb(255, 209, 220)
      )
      embed.set_author(
        name=f"{inter.author.name}#{inter.author.discriminator}", 
        icon_url=f"{ctxAuthorAvatar}"
      )
      embed.set_image(url=f"{ctxAuthorBanner}")
      await inter.response.send_message(embed=embed)


    elif user is not None:

      user = await self.bot.fetch_user(user.id)

      if user.banner is None:
        embed = disnake.Embed(
          title="Errore!",
          description=":x: Questo membro non possiede un banner!",
          color=disnake.Color.from_rgb(255, 1, 57)
        )
        await inter.response.send_message(embed=embed)
        return

      elif user.banner is not None:
        UserBanner = user.banner
        

        if inter.author.avatar is not None:
          ctxAuthorAvatar1 = inter.author.avatar

        elif inter.author.avatar is None:
          ctxAuthorAvatar1 = inter.author.default_avatar

      
      embed = disnake.Embed(
        title=f'Banner di {user.display_name}',
        color=disnake.Color.from_rgb(255, 209, 220)
      )
      embed.set_author(
        name=f"{inter.author.name}#{inter.author.discriminator}", 
        icon_url=f"{ctxAuthorAvatar1}"
      )
      embed.set_image(url=f"{UserBanner}")
      await inter.response.send_message(embed=embed)


      
  
  # AVATAR DEFAULT USER AND NON GUILD AVATAR
  @avatar.sub_command(description="Ottieni l'avatar di un utente, se ne ha uno")
  async def user(self, inter, user: disnake.Member = None):

    if user is None:

      if inter.author.avatar is None:
        ctxAuthorAvatar = inter.author.default_avatar
        
      else:
        ctxAuthorAvatar = inter.author.avatar

      
      embed = disnake.Embed(
        title=f'Avatar di {inter.author.display_name}',
        color=disnake.Color.from_rgb(255, 209, 220)
      )
      embed.set_author(
        name=f"{inter.author.name}#{inter.author.discriminator}", 
        icon_url=f"{ctxAuthorAvatar}"
      )
      embed.set_image(url=f"{ctxAuthorAvatar}")
      
      await inter.response.send_message(embed=embed)

    elif user is not None:

      if inter.author.avatar is not None:
        ctxAuthorAvatar1 = inter.author.avatar
      
      else:
        ctxAuthorAvatar1 = inter.author.default_avatar

      if user.avatar is None:
        memberAvatar1 = user.default_avatar

      else:
        memberAvatar1 = user.avatar
      
      embed = disnake.Embed(
        title=f'Avatar di {user.display_name}',
        color=disnake.Color.from_rgb(255, 209, 220)
      )
      embed.set_author(
        name=f"{inter.author.name}#{inter.author.discriminator}", 
        icon_url=f"{ctxAuthorAvatar1}"
      )
      embed.set_image(url=f"{memberAvatar1}")
      await inter.response.send_message(embed=embed)

  

    
def setup(bot):
  bot.add_cog(avUltimate(bot))