import disnake
import os
import asyncio
import sys
import json
from disnake.ext import commands


if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)
    whiteListedChannel = config["877130463662182410"]["whitelisted-channel"]


class avatarGuild(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.whiteListedChannel = whiteListedChannel


  @commands.command(aliases=['avg', 'avatarguild'])
  async def avs(self, ctx, member: disnake.Member = None):

    if str(ctx.channel.id) not in self.whiteListedChannel:
      msg = await ctx.reply(':x: Questo canale non è in whitelist, pertanto i comandi sono disabilitati!')
      await asyncio.sleep(2)
      await mesg.delete()
      return

    elif str(ctx.channel.id) in self.whiteListedChannel:

      if member == None:

        if ctx.author.guild_avatar != None and ctx.author.avatar != None:
          authorGuildAvatar = ctx.author.guild_avatar
          authorAvatar = ctx.author.avatar

        elif ctx.author.guild_avatar == None and ctx.author.avatar == None:
          authorGuildAvatar = ctx.author.default_avatar
          authorAvatar = ctx.author.default_avatar

        elif ctx.author.guild_avatar != None and ctx.author.avatar == None:
          authorGuildAvatar = ctx.author.guild_avatar
          authorAvatar = ctx.author.default_avatar

        elif ctx.author.guild_avatar == None and ctx.author.avatar != None:
          authorGuildAvatar = ctx.author.avatar
          authorAvatar = ctx.author.avatar

      
        embed = disnake.Embed(
          title=f'Avatar of {ctx.author.display_name}',
          color=disnake.Color.from_rgb(255, 209, 220)
        )
        embed.set_author(
          name=f"{ctx.author.name}#{ctx.author.discriminator}", 
          icon_url=f"{authorAvatar}"
        )
        embed.set_image(url=f"{authorGuildAvatar}")

        view = disnake.ui.View()
        item = disnake.ui.Button(style=disnake.ButtonStyle.danger, label="🗑️ Delete")
        view.add_item(item=item)


        msg = await ctx.reply(embed=embed, view=view)


        def check(res):
          return ctx.author == res.user and res.channel == ctx.channel and msg == res.message

        res = await self.bot.wait_for("button_click", check=check)

        
        if res.component.label.startswith("🗑️ Delete"):
          await ctx.message.delete()
          await msg.delete()

      

      elif member != None:

        if member.guild_avatar != None and ctx.author.avatar != None:
          memberGuildAvatar = member.guild_avatar
          authorAvatar = ctx.author.avatar

        elif member.guild_avatar == None and ctx.author.avatar == None:
          memberGuildAvatar = member.default_avatar
          authorAvatar = ctx.author.default_avatar

        elif member.guild_avatar != None and ctx.author.avatar == None:
          memberGuildAvatar = member.guild_avatar
          authorAvatar = ctx.author.default_avatar

        elif member.guild_avatar == None and ctx.author.avatar != None:
          memberGuildAvatar = member.avatar
          authorAvatar = ctx.author.avatar

      
        embed = disnake.Embed(
          title=f'Avatar Guild of {member.display_name}',
          color=disnake.Color.from_rgb(255, 209, 220)
        )
        embed.set_author(
          name=f"{ctx.author.name}#{ctx.author.discriminator}", 
          icon_url=f"{authorAvatar}"
        )
        embed.set_image(url=f"{memberGuildAvatar}")

        view = disnake.ui.View()
        item = disnake.ui.Button(style=disnake.ButtonStyle.danger, label="🗑️ Delete")
        view.add_item(item=item)


        msg = await ctx.reply(embed=embed, view=view)


        def check(res):
          return ctx.author == res.user and res.channel == ctx.channel and msg == res.message

        res = await self.bot.wait_for("button_click", check=check)

        
        if res.component.label.startswith("🗑️ Delete"):
          await ctx.message.delete()
          await msg.delete()
        



  @avs.error
  async def avs_error(self, ctx, error):
    if isinstance(error, commands.MemberNotFound):

      embed = disnake.Embed(
        title='Errore',
        description=":x: Membro non trovato, controlla che il tag o l'ID sia corretto e riprova. Se il problema persiste contatta <@710570210159099984>.",
        color=disnake.Color.from_rgb(255, 1, 57)
      )
      await ctx.reply(embed=embed)


        
def setup(bot):
  bot.add_cog(avatarGuild(bot))