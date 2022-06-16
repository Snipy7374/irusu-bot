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


class troll(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['pp'])
  async def penis(self, ctx, member: disnake.Member = None):
    x = random.randint(1, 15)

    if ctx.author.avatar != None:
      ctxAuthorAvatar = ctx.author.avatar

    elif ctx.author.avatar == None:
      ctxAuthorAvatar = ctx.author.default_avatar
    
    if member == None:

      if ctx.author.id == 710570210159099984:
        embed = disnake.Embed(
          title='PP of my master, Snipy-sama',
          description=f"8{'='*35}D",
          color=disnake.Color.from_rgb(255, 209, 220)
        )
        embed.set_author(name=f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url=f"{ctxAuthorAvatar}")
        
        await ctx.send(f"<@!{ctx.author.id}>", embed=embed)
        return
      
      embed = disnake.Embed(
          title=f"PP of {ctx.author.display_name}#{ctx.author.discriminator}",
          description=f"8{'='*x}D",
          color=disnake.Color.from_rgb(255, 209, 220)
        )
      embed.set_author(name=f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url=f"{ctxAuthorAvatar}")
      
      await ctx.reply(embed=embed)
    

    elif member != None:
      
      if ctx.author.avatar != None:
        ctxAuthorAvatar = ctx.author.avatar

      elif ctx.author.avatar == None:
        ctxAuthorAvatar = ctx.author.default_avatar
    
      
      if member.id == 710570210159099984:
        embed = disnake.Embed(
          title='PP of my master, Snipy-sama',
          description=f"8{'='*35}D",
          color=disnake.Color.from_rgb(255, 209, 220)
        )
        embed.set_author(name=f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url=f"{ctxAuthorAvatar}")
        
        await ctx.reply(embed=embed)

      else:
        embed = disnake.Embed(
          title=f"PP of {member.display_name}#{member.discriminator}",
          description=f"8{'='*x}D",
          color=disnake.Color.from_rgb(255, 209, 220)
        )
        embed.set_author(name=f"{ctx.author.display_name}#{ctx.author.discriminator}", icon_url=f"{ctxAuthorAvatar}")
      
        await ctx.reply(embed=embed)

  @penis.error
  async def penis_error(self, ctx, error):
    if isinstance(error, commands.MemberNotFound):

      embed = disnake.Embed(
        title='Errore',
        description=":x: Membro non trovato, controlla che il tag o l'ID sia corretto e riprova. Se il problema persiste contatta @Snipy#7374.",
        color=disnake.Color.from_rgb(255, 1, 57)
      )
      await ctx.reply(embed=embed)
    

    
def setup(bot):
  bot.add_cog(troll(bot))