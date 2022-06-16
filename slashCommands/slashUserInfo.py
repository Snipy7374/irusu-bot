import disnake
import os
import sys
import json
import datetime
from disnake.ext import commands


if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)


class slashUserInfo(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(description="Risponde inviando le informazioni di un utente.")
  async def userinfo(self, inter, member: disnake.Member = None):

    if inter.author.avatar == None:
      authorAvatar = inter.author.default_avatar

    elif inter.author.avatar != None:
      authorAvatar = inter.author.avatar

    if member != None:
      if member.avatar == None:
        memberAvatar = member.default_avatar

      elif member.avatar != None:
        memberAvatar = member.avatar


    if member == None:
    
      embed = disnake.Embed(
        title=f'Informazioni per {inter.author.display_name}',
        description=f'<@{inter.author.id}>\nID: {inter.author.id}',
        color=disnake.Color.from_rgb(255, 209, 220),
        timestamp=datetime.datetime.utcnow()
      )
      embed.set_author(
       name=f"{inter.author.display_name}#{inter.author.discriminator}",
       icon_url=f"{authorAvatar}"
      )
      
      embed.add_field(
        name=f"Entrato il:", 
        value=f"{inter.author.joined_at.strftime('%d-%m-%Y %H:%M')}",
        inline=False
      )
      
      embed.add_field(
        name='Registrato il', 
        value=f"{inter.author.created_at.strftime('%d-%m-%Y %H:%M')}",
        inline=False
      )
      
      roles = (role for role in inter.author.roles[::-1])
      embed.add_field(
        name=f"Ruoli [{len(inter.author.roles)}]", 
        value=" ".join([role.mention for role in roles]), 
        inline=True
      )
      
      embed.set_thumbnail(
        url=f"{authorAvatar}"
      )
      
      embed.set_footer(
        text=f"ID: {inter.author.id}"
      )
      member = inter.author
      permissions = [perm[0] for perm in member.guild_permissions if perm[1]]
      str1 = "`, `"
      perms = (str1.join(permissions)).upper()
      
      embed.add_field(
        name="Permessi", 
        value=f"`{perms}`", 
        inline=False
      )

      await inter.response.send_message(embed=embed)

    
    elif member != None:
      embed = disnake.Embed(
        title=f'Informazioni per {member.name}',
        description=f'<@{member.id}>',
        color=disnake.Color.from_rgb(255, 209, 220),
        timestamp=datetime.datetime.utcnow()
      )
      embed.set_author(
        name=f"{inter.author.display_name}#{inter.author.discriminator}",
        icon_url=f"{authorAvatar}"
      )
      
      embed.add_field(
        name=f"Entrato il:", 
        value=f"{member.joined_at.strftime('%d-%m-%Y %H:%M')}",
        inline=False
      )
      
      embed.add_field(
        name='Registrato il', 
        value=f"{member.created_at.strftime('%d-%m-%Y %H:%M')}",
        inline=False
      )
      
      roles = (role for role in member.roles[::-1])
      embed.add_field(
        name=f"Ruoli [{len(member.roles)}]", 
        value=" ".join([role.mention for role in roles]), 
        inline=True
      )
      
      embed.set_thumbnail(
        url=f"{memberAvatar}"
      )
      
      embed.set_footer(
        text=f"ID: {member.id}"
      )
      
      permissions = [perm[0] for perm in member.guild_permissions if perm[1]]
      str1 = "`, `"
      perms = (str1.join(permissions)).upper()
      
      embed.add_field(
        name="Permessi", 
        value=f"`{perms}`", 
        inline=False
      )

      await inter.response.send_message(embed=embed)
    
    
      
def setup(bot):
  bot.add_cog(slashUserInfo(bot))