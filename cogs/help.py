import disnake
import os
import sys
import json
from disnake.ext import commands
from disnake.ext.commands import Bot

bot = Bot(help_command=None)

if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)


class help(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

    with open("config.json", "r") as f:  prefixes = json.load(f)
    get_prefix = prefixes["877130463662182410"]["prefix"]
    self.get_prefix = get_prefix

  @commands.command()
  async def invite(self, ctx):
    if ctx.author.id == 710570210159099984:
      await ctx.send("https://discord.com/api/oauth2/authorize?client_id=948229353077112872&permissions=8&scope=bot%20applications.commands")
    else:
      return

  @bot.group(aliases=['aiuto'])
  async def help(self, ctx):

    if ctx.author.avatar != None:
      avatar = ctx.author.avatar
    else:
      avatar = ctx.author.default_avatar
    
    if ctx.invoked_subcommand != None:
      return
    embedHelp = disnake.Embed(
      title='Comando Help',
      color=disnake.Color.from_rgb(255, 209, 220),
    )
    embedHelp.set_author(
      name=f"{ctx.author.name}#{ctx.author.discriminator}", 
      icon_url=f"{avatar}"
    )
    embedHelp.add_field(
      name='Misc', 
      value='`av`, `help`, `avs`, `avl`, `banner`', 
      inline=False
    )
    embedHelp.add_field(
      name='Utiliy', 
      value='`serverinfo`, `userinfo`, `channel`, `emoji`', 
      inline=False
    )
    embedHelp.add_field(
      name='Moderation',
      value='`ban`, `unban`, `setprefix`, `cprexi`',
      inline=False
    )
    embedHelp.set_footer(
      text='Per maggiori informazioni su un comando esegui >help [comando]'
    )
    embedHelp.set_thumbnail(
      url=f"{self.bot.user.avatar}"
    )
    await ctx.reply(embed=embedHelp)

  @help.command(aliases=['av'])
  async def avatar(self, ctx):
    
    if ctx.author.avatar != None:
      avatar = ctx.author.avatar
    else:
      avatar = ctx.author.default_avatar
      
    embed = disnake.Embed(
      title='avatar [membro]',
      color=disnake.Color.from_rgb(255, 209, 220),
      description="Restituisce il tuo avatar, se specificato può restituire l'avatar di altri utenti. Per specificare un utente di cui si vuole l'avatar, si può specificare il suo ID oppure basterà menzinarlo (es. ID: `710570210159099984`; es. menzione:  `@Snipy#7374`)"
    )
    embed.set_author(
      name=f"{ctx.author.name}#{ctx.author.discriminator}", 
      icon_url=f"{avatar}"
    )
    embed.add_field(
      name='Alias', 
      value='`av`, `avatar`'
    )
    embed.add_field(
      name='Utilizzo', 
      value=f"`{self.get_prefix}av <@MENZIONE>`\n`{self.get_prefix}av <ID>`\n`{self.get_prefix}avatar <@MENZIONE>`\n`{self.get_prefix}avatar <ID>`", 
      inline=False
    )
    
    await ctx.reply(embed=embed)

  @help.command(aliases=['avg', 'avatarguild'])
  async def avs(self, ctx):

    if ctx.author.avatar != None:
      avatar = ctx.author.avatar
    else:
      avatar = ctx.author.default_avatar
    
    embed = disnake.Embed(
      title='avs [membro]',
      color=disnake.Color.from_rgb(255, 209, 220),
      description="Restituisce l'avatar specifico per un solo server di un membro, se specificato può restituire l'avatar di altri utenti. Per specificare un utente di cui si vuole l'avatar si può usare il suo ID oppure basterà menzionarlo (es. ID: `710570210159099984`; es. menzione:  `@Snipy#7374`)"
    )
    embed.set_author(
      name=f"{ctx.author.name}#{ctx.author.discriminator}", 
      icon_url=f"{avatar}"
    )
    embed.add_field(
      name='Alias', 
      value='`avs`, `avatarguild`, `avg`'
    )
    embed.add_field(
      name='Utilizzo', 
      value=f"`{self.get_prefix}avs <@MENZIONE>`\n`{self.get_prefix}avs <ID>`\n`{self.get_prefix}avg <@MENZIONE>`\n`{self.get_prefix}avg <ID>`", 
      inline=False
    )
    
    await ctx.send(embed=embed)

  @help.command(aliases=['guildinfo', 'infoserver', 'informazioniserver', 'serverinfo', 'infoirusu'])
  async def info(self, ctx):

    if ctx.author.avatar != None:
      avatar = ctx.author.avatar
    else:
      avatar = ctx.author.default_avatar
    
    embed = disnake.Embed(
      title='serverinfo',
      color=disnake.Color.from_rgb(255, 209, 220),
      description="Restituisce le informazioni del server."
    )
    embed.set_author(
      name=f"{ctx.author.name}#{ctx.author.discriminator}", 
      icon_url=f"{avatar}"
    )
    embed.add_field(
      name='Alias', 
      value='`guildinfo`, `infoserver`, `informazioniserver`, `serverinfo`, `infoirusu`'
    )
    embed.add_field(
      name='Utilizzo', 
      value=f"`{self.get_prefix}info`", 
      inline=False
    )
    
    await ctx.reply(embed=embed)

  @help.command(aliases=['usrinfo', 'user', 'infouser', 'whoami'])
  async def userinfo(self, ctx):

    if ctx.author.avatar != None:
      avatar = ctx.author.avatar
    else:
      avatar = ctx.author.default_avatar

    embed = disnake.Embed(
      title='userinfo [member]',
      color=disnake.Color.from_rgb(255, 209, 220),
      description="Restituisce le informazioni specifiche per un utente del server, se specificato può restituire le informazioni di altri utenti. Per specificare un utente si può usare il suo ID oppure basterà menzionarlo (es. ID: `710570210159099984`; es. menzione:  `@Snipy#7374`)"
    )
    embed.set_author(
      name=f"{ctx.author.name}#{ctx.author.discriminator}", 
      icon_url=f"{avatar}"
    )
    embed.add_field(
      name='Alias', 
      value='`usrinfo`, `user`, `infouser`, `whoami`'
    )
    embed.add_field(
      name='Utilizzo', 
      value=f"`{self.get_prefix}userinfo`", 
      inline=False
    )
    
    await ctx.reply(embed=embed)


  @help.command(aliases=['avatarlist', 'avlist'])
  async def avl(self, ctx):

    if ctx.author.avatar != None:
      avatar = ctx.author.avatar
    else:
      avatar = ctx.author.default_avatar
    
    embed = disnake.Embed(
      title='avl [member1, member2, ..., member10]',
      color=disnake.Color.from_rgb(255, 209, 220),
      description="Restituisce una lista di avatar di una lista di membri.\nPuoi indicare un massimo di 10 utenti (ID o tag), inoltre è importante il rispetto della sintassi, le virgole sono necessarie."
    )
    embed.set_author(
      name=f"{ctx.author.name}#{ctx.author.discriminator}", 
      icon_url=f"{avatar}"
    )
    embed.add_field(
      name='Alias', 
      value='`avl`, `avlist`'
    )
    embed.add_field(
      name='Utilizzo', 
      value=f"`{self.get_prefix}avl @membro1, @membro2`", 
      inline=False
    )
    
    await ctx.reply(embed=embed)


  @help.command(aliases=['ub'])
  async def banner(self, ctx):

    if ctx.author.avatar != None:
      avatar = ctx.author.avatar
    else:
      avatar = ctx.author.default_avatar
    
    embed = disnake.Embed(
      title='banner [member]',
      color=disnake.Color.from_rgb(255, 209, 220),
      description="Restituisce il banner di un utente, se non viene indicato alcun utente restituisce il banner di chi esegue il comando."
    )
    embed.set_author(
      name=f"{ctx.author.name}#{ctx.author.discriminator}", 
      icon_url=f"{avatar}"
    )
    embed.add_field(
      name='Alias', 
      value='`banner`, `ub`'
    )
    embed.add_field(
      name='Utilizzo', 
      value=f"`{self.get_prefix}banner @membro`", 
      inline=False
    )
    
    await ctx.reply(embed=embed)

  @help.command(aliases=['getidemoji', 'idgetemoji', 'idemoji', 'irusuemojiid', 'emojiid'])
  async def emoji(self, ctx):

    if ctx.author.avatar != None:
      avatar = ctx.author.avatar
    else:
      avatar = ctx.author.default_avatar
    
    embed = disnake.Embed(
      title='emoji [emoji]',
      color=disnake.Color.from_rgb(255, 209, 220),
      description="Restituisce l'ID di un emoji inviandone una."
    )
    embed.set_author(
      name=f"{ctx.author.name}#{ctx.author.discriminator}", 
      icon_url=f"{avatar}"
    )
    embed.add_field(
      name='Alias', 
      value='`getidemoji`, `idgetemoji`, `idemoji`, `irusuemojiid`, `emojiid`'
    )
    embed.add_field(
      name='Utilizzo', 
      value=f"`{self.get_prefix}emoji :emoji:`", 
      inline=False
    )
    
    await ctx.reply(embed=embed)

  @help.command(aliases=['getidchannel', 'idgetchannel', 'idchannel', 'irusuchannelid', 'channelid'])
  async def channel(self, ctx):

    if ctx.author.avatar != None:
      avatar = ctx.author.avatar
    else:
      avatar = ctx.author.default_avatar
    
    embed = disnake.Embed(
      title='channel [canale]',
      color=disnake.Color.from_rgb(255, 209, 220),
      description="Restituisce l'ID di un canale taggandone uno."
    )
    embed.set_author(
      name=f"{ctx.author.name}#{ctx.author.discriminator}", 
      icon_url=f"{avatar}"
    )
    embed.add_field(
      name='Alias', 
      value='`getidchannel`, `idgetchannel`, `idchannel`, `irusuchannelid`, `channelid`'
    )
    embed.add_field(
      name='Utilizzo', 
      value=f"`{self.get_prefix}channel #canale`", 
      inline=False
    )
    
    await ctx.reply(embed=embed)

      
  
def setup(bot):
  bot.add_cog(help(bot))