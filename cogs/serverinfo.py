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



class serverinfo(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
      

  @commands.command(aliases=['guildinfo', 'infoserver', 'informazioniserver', 'info', 'infoirusu'])
  async def serverinfo(self, ctx):

    if ctx.author.avatar == None:
      authorAvatar = ctx.author.default_avatar

    elif ctx.author.avatar != None:
      authorAvatar = ctx.author.avatar
    
    embed = disnake.Embed(
      title=f'Informazioni per {ctx.guild.name}',
      color=disnake.Color.from_rgb(255, 209, 220),
      timestamp=datetime.datetime.utcnow()
    )
    embed.set_author(
      name=f"{ctx.author.name}#{ctx.author.discriminator}", 
      icon_url=f"{authorAvatar}"
    )
    embed.set_footer(text=f"Guild ID: {ctx.guild.id}")
    embed.add_field(
      name='Owner', 
      value=f'{ctx.guild.owner}', 
      inline=True
    )
    embed.add_field(
      name='Livello Boosts', 
      value=f'`{ctx.guild.premium_tier}`', 
      inline=True
    )
    embed.add_field(
      name='Numero di Boosters', value=f'`{ctx.guild.premium_subscription_count}`', 
      inline=True
    )
    embed.add_field(
      name='Numero Canali', 
      value=f'Canali testuali `{len(ctx.guild.channels)}`\nCanali vocali `{len(ctx.guild.voice_channels)}`\nCanali stage `{len(ctx.guild.stage_channels)}`', 
      inline=True
    )

    if int(ctx.guild.mfa_level) == 1:
      security = "2FA attivo"

    elif int(ctx.guild.mfa_level) == 0:
      security = "2FA non attivo"

    
    if str(ctx.guild.explicit_content_filter) == "all_members":
      filter = "Filtro attivo per tutti i membri"

    elif str(ctx.guild.explicit_content_filter) == "no_role":
      filter = "Filtro attivo solamente per i membri privi di ruoli"

    elif str(ctx.guild.explicit_content_filter) == "disabled":
      filter = "Filtro disattivato per tutti gli utenti"

    
    if str(ctx.guild.default_notifications) == "NotificationLevel.all_messages":
      notify = "Notifiche attive per tutti i messaggi"

    elif str(ctx.guild.default_notifications) == "NotificationLevel.only_mentions":
      notify = "Notifiche attive solamente per le menzioni"

    
    embed.add_field(
      name='Info', 
      value=f'Livello di sicurezza `{ctx.guild.verification_level}`\nLivello di sicurezza per moderare `{security}`\nFiltro dei contenuti espliciti `{filter}`\nNotifiche `{notify}`\nCreato il `{ctx.guild.created_at.date()}`\nCanale delle regole `{ctx.guild.rules_channel}`\n[Link logo]({ctx.guild.icon} "Link logo")', 
      inline=False
    )

    features = [feat for feat in ctx.guild.features]
    str1 = "`, `"
    feat = (str1.join(features)).upper()

    
    embed.add_field(
      name="Features del server",
      value=f"`{feat}`",
      inline=False
    )
    embed.add_field(
      name='Prefisso', 
      value=f"<@948229353077112872>\n`{config['877130463662182410']['prefix']}`"
    )

    if ctx.guild.banner != None:
      embed.set_image(
        url=f"{ctx.guild.banner}"
      )
    else:
      pass

    global members
    global bots
    
    for member in ctx.guild.members:
      if not member.bot:
        members += 1

    for member in ctx.guild.members:
      if member.bot:
        bots += 1
    
    embed.add_field(
      name='Membri', 
      value=f"Membri totali `{len(ctx.guild.members)}`\nUmani `{members}`\nBot `{bots}`"
    )
    embed.add_field(
      name='Ruoli', 
      value=f"`{len(ctx.guild.roles)}` ruoli"
    )
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    await ctx.reply(embed=embed)
    
    #resetting the counter
    members, bots = 0, 0

    
      
def setup(bot):
  bot.add_cog(serverinfo(bot))