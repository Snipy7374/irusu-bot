import disnake
import os
import sys
import json
from disnake.ext import commands


if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)
    whiteListedChannel = config["877130463662182410"]["whitelisted-channel"]


class memberAvList(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.whiteListedChannel = whiteListedChannel

  @commands.command(aliases=['avl'])
  async def avList(self, ctx):

    if str(ctx.channel.id) not in self.whiteListedChannel:
      await ctx.reply(':x: Questo canale non è in whitelist, pertanto i comandi sono disabilitati!')
      return

    elif str(ctx.channel.id) in self.whiteListedChannel:
      if ctx.message.content != None:
      
        if '@' in ctx.message.content:
          if ctx.author.avatar != None:
            ctxAuthorAvatar1 = ctx.author.avatar

          elif ctx.author.avatar == None:
            ctxAuthorAvatar1 = ctx.author.default_avatar

      
          avList = ctx.message.content[5:].split(', ')
          avId = []
          avName = []
          userList = []
          userAvatarList = []

          if len(avList) > 10:
  
            embed = disnake.Embed(
              title='Errore',
              color=disnake.Color.from_rgb(255, 1, 57),
              description=':x: Puoi specificare al massimo 10 membri!'
            )
            await ctx.reply(embed=embed)
            return

          for i in range(len(avList)):
  
            user = avList[i]
            userList.append(user)
            userId = user[2:20]
            avId.append(int(userId))
  
          for i in range(len(avId)):
  
            user = self.bot.get_user(avId[i])
            userAvatar = user.avatar
            userAvatarList.append(userAvatar)
            userName = user.name
            avName.append(userName)
  
          #await ctx.send(userList)
  
          PAGES = []
  
          for i in range(len(avName)):
          
            embed = disnake.Embed(
              title=f"[{i+1}] Av member list di {avName[i]}",
              color=disnake.Color.from_rgb(255, 209, 220)
            )
          
            PAGES.append(embed)
  
  
          for i in range(len(avName)):
            PAGES[i].set_author(
              name=f"{ctx.author.name}#{ctx.author.discriminator}", 
              icon_url=f"{ctxAuthorAvatar1}"
            )
            PAGES[i].set_image(
              url=f"{userAvatarList[i]}"
            )
            await ctx.send(embed=PAGES[i])
  
        elif '@' not in ctx.message.content:
  
  
          if ctx.author.avatar != None:
            ctxAuthorAvatar1 = ctx.author.avatar
  
          elif ctx.author.avatar == None:
            ctxAuthorAvatar1 = ctx.author.default_avatar
  
        
          avList = ctx.message.content[5:].split(', ')
          avId = []
          avName = []
          userAvatarList = []
  
          for i in range(len(avList)):
  
            user = avList[i]
            avId.append(user)
  
          for i in range(len(avId)):
  
            user = self.bot.get_user(int(avId[i]))
  
            if user.display_name == user.name:
              userName = user.name
            elif user.display_name != user.name:
              userName = user.display_name
  
            if user.avatar == None:
              userAvatar = user.default_avatar
            elif user.avatar != None:
              userAvatar = user.avatar
  
            userAvatarList.append(userAvatar)
            avName.append(userName)
  
          PAGES = []
  
          for i in range(len(avName)):
          
            embed = disnake.Embed(
              title=f"[{i+1}] Av member list di {avName[i]}",
              color=disnake.Color.from_rgb(255, 209, 220)
            )        
            PAGES.append(embed)
  
          for i in range(len(avName)):
            PAGES[i].set_author(
              name=f"{ctx.author.name}#{ctx.author.discriminator}", 
              icon_url=f"{ctxAuthorAvatar1}"
            )
            PAGES[i].set_image(
              url=f"{userAvatarList[i]}"
            )
            await ctx.send(embed=PAGES[i])



  @avList.error
  async def av_error(self, ctx, error):
    if isinstance(error, commands.MemberNotFound):

      embed = disnake.Embed(
        title='Errore',
        description=":x: Membro non trovato, controlla che il tag o l'ID sia corretto e riprova. Se il problema persiste contatta <@710570210159099984>.",
        color=disnake.Color.from_rgb(255, 1, 57)
      )
      await ctx.reply(embed=embed)

    if str(error) == 'Command raised an exception: HTTPException: 400 Bad Request (error code: 50006): Cannot send an empty message':

      embed = disnake.Embed(
        title='Errore',
        color=disnake.Color.from_rgb(255, 1, 57),
        description=':x: Per poter usare questo comando devi specificare una lista di membri!'
      )
      await ctx.reply(embed=embed)

    if str(error) == "Command raised an exception: ValueError: invalid literal for int() with base 10: ''":
      embed = disnake.Embed(
        title='Errore',
        color=disnake.Color.from_rgb(255, 1, 57),
        description=':x: Errore inatteso, contatta <@710570210159099984>'
      )
      await ctx.reply(embed=embed)

    if str(error) == "Command raised an exception: AttributeError: 'NoneType' object has no attribute 'display_name'":
      embed = disnake.Embed(
        title='Errore',
        color=disnake.Color.from_rgb(255, 1, 57),
        description=':x: Membri non trovati!'
      )
      await ctx.reply(embed=embed)


      
def setup(bot):
  bot.add_cog(memberAvList(bot))