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


class userinfo(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['usrinfo', 'user', 'infouser', 'whoami'])
  async def userinfo(self, ctx, member: disnake.Member = None):

    if ctx.author.avatar == None:
      authorAvatar = ctx.author.default_avatar

    elif ctx.author.avatar != None:
      authorAvatar = ctx.author.avatar

    if member != None:
      if member.avatar == None:
        memberAvatar = member.default_avatar

      elif member.avatar != None:
        memberAvatar = member.avatar


    if member == None:
    
      embed = disnake.Embed(
        title=f'Informazioni per {ctx.author.display_name}',
        description=f'<@{ctx.author.id}>\nID: {ctx.author.id}',
        color=disnake.Color.from_rgb(255, 209, 220),
        timestamp=datetime.datetime.utcnow()
      )
      embed.set_author(
       name=f"{ctx.author.display_name}#{ctx.author.discriminator}",
       icon_url=f"{authorAvatar}"
      )
      
      embed.add_field(
        name=f"Entrato il:", 
        value=f"{ctx.author.joined_at.strftime('%d-%m-%Y %H:%M')}",
        inline=False
      )
      
      embed.add_field(
        name='Registrato il', 
        value=f"{ctx.author.created_at.strftime('%d-%m-%Y %H:%M')}",
        inline=False
      )
      
      roles = (role for role in ctx.author.roles[::-1])
      embed.add_field(
        name=f"Ruoli [{len(ctx.author.roles)}]", 
        value=" ".join([role.mention for role in roles]), 
        inline=True
      )
      
      embed.set_thumbnail(
        url=f"{authorAvatar}"
      )
      
      embed.set_footer(
        text=f"ID: {ctx.author.id}"
      )
      member = ctx.message.author
      permissions = [perm[0] for perm in member.guild_permissions if perm[1]]
      str1 = "`, `"
      perms = (str1.join(permissions)).upper()
      
      embed.add_field(
        name="Permessi", 
        value=f"`{perms}`", 
        inline=False
      )

      await ctx.reply(embed=embed)

    
    elif member != None:
      embed = disnake.Embed(
        title=f'Informazioni per {member.name}',
        description=f'<@{member.id}>',
        color=disnake.Color.from_rgb(255, 209, 220),
        timestamp=datetime.datetime.utcnow()
      )
      embed.set_author(
        name=f"{ctx.author.display_name}#{ctx.author.discriminator}",
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

      await ctx.reply(embed=embed)

  @userinfo.error
  async def userinfo_error(self, ctx, error):
    if isinstance(error, commands.MemberNotFound):

      embed = disnake.Embed(
        title='Errore',
        description=":x: Membro non trovato, controlla che il tag o l'ID sia corretto e riprova. Se il problema persiste contatta <@710570210159099984>.",
        color=disnake.Color.from_rgb(255, 1, 57)
      )
      await ctx.reply(embed=embed)

    
    
      
def setup(bot):
  bot.add_cog(userinfo(bot))