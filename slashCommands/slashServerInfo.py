import disnake
import os
import sys
import json
import datetime
from disnake.ext import commands

members = 0
bots = 0

if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)



class slashServerInfo(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
      
  @commands.slash_command(description="Invia le informazioni pubbliche del server.")
  async def serverinfo(self, inter):

    if inter.author.avatar == None:
      authorAvatar = inter.author.default_avatar

    elif inter.author.avatar != None:
      authorAvatar = inter.author.avatar
    
    embed = disnake.Embed(
      title=f'Informazioni per {inter.guild.name}',
      color=disnake.Color.from_rgb(255, 209, 220),
      timestamp=datetime.datetime.utcnow()
    )
    embed.set_author(
      name=f"{inter.author.name}#{inter.author.discriminator}", 
      icon_url=f"{authorAvatar}"
    )
    embed.set_footer(text=f"Guild ID: {inter.guild.id}")
    embed.add_field(
      name='Owner', 
      value=f'{inter.guild.owner}', 
      inline=True
    )
    embed.add_field(
      name='Livello Boosts', 
      value=f'`{inter.guild.premium_tier}`', 
      inline=True
    )
    embed.add_field(
      name='Numero di Boosters', value=f'`{inter.guild.premium_subscription_count}`', 
      inline=True
    )
    embed.add_field(
      name='Numero Canali', 
      value=f'Canali testuali `{len(inter.guild.channels)}`\nCanali vocali `{len(inter.guild.voice_channels)}`\nCanali stage `{len(inter.guild.stage_channels)}`', 
      inline=True
    )
    embed.add_field(
      name='Info', 
      value=f'Livello di sicurezza `{inter.guild.verification_level}`\nCreato il `{inter.guild.created_at.date()}`\nCanale delle regole `{inter.guild.rules_channel}`\n[Link logo]({inter.guild.icon} "Link logo")', 
      inline=False
    )
    embed.add_field(
      name='Prefisso', 
      value=f"<@948229353077112872>\n`{config['877130463662182410']['prefix']}`"
    )

    global members
    global bots
    
    for member in inter.guild.members:
      if not member.bot:
        members += 1

    for member in inter.guild.members:
      if member.bot:
        bots += 1
    
    embed.add_field(
      name='Membri', 
      value=f"Membri totali `{len(inter.guild.members)}`\nUmani `{members}`\nBot `{bots}`"
    )
    embed.add_field(
      name='Ruoli', 
      value=f"`{len(inter.guild.roles)}` ruoli"
    )

    if inter.guild.banner != None:
      embed.set_image(
        url=f"{inter.guild.banner}"
      )
    else:
      pass
    embed.set_thumbnail(url=f"{inter.guild.icon}")
    await inter.response.send_message(embed=embed)
    
    #resetting the counter
    members, bots = 0, 0

    
      
def setup(bot):
  bot.add_cog(slashServerInfo(bot))