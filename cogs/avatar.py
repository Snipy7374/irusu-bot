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


class avatar(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.whiteListedChannel = whiteListedChannel

  @commands.command(aliases=['avatar'])
  async def av(self, ctx, member: disnake.Member = None):

    if str(ctx.channel.id) not in self.whiteListedChannel:
      await ctx.reply(':x: Questo canale non è in whitelist, pertanto i comandi sono disabilitati!')
      return

    elif str(ctx.channel.id) in self.whiteListedChannel:
      if member == None:

        if ctx.author.avatar == None:
          ctxAuthorAvatar = ctx.author.default_avatar
        
        elif ctx.author.avatar != None:
          ctxAuthorAvatar = ctx.author.avatar

      
        embed = disnake.Embed(
          title=f'Avatar di {ctx.author.display_name}',
          color=disnake.Color.from_rgb(255, 209, 220)
        )
        embed.set_author(
          name=f"{ctx.author.name}#{ctx.author.discriminator}", 
          icon_url=f"{ctxAuthorAvatar}"
        )
        embed.set_image(url=f"{ctxAuthorAvatar}")


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

        if ctx.author.avatar != None and member.avatar == None:
          ctxAuthorAvatar1 = ctx.author.avatar
          memberAvatar1 = member.default_avatar

        elif ctx.author.avatar != None and member.avatar != None:
          ctxAuthorAvatar1 = ctx.author.avatar
          memberAvatar1 = member.avatar

        elif ctx.author.avatar == None and member.avatar != None:
          ctxAuthorAvatar1 = ctx.author.default_avatar
          memberAvatar1 = member.avatar

        elif ctx.author.avatar == None and member.avatar == None:
          ctxAuthorAvatar1 = ctx.author.default_avatar
          memberAvatar1 = member.default_avatar

      
        embed = disnake.Embed(
          title=f'Avatar di {member.display_name}',
          color=disnake.Color.from_rgb(255, 209, 220)
        )
        embed.set_author(
          name=f"{ctx.author.name}#{ctx.author.discriminator}", 
          icon_url=f"{ctxAuthorAvatar1}"
        )
        embed.set_image(url=f"{memberAvatar1}")

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


  @av.error
  async def av_error(self, ctx, error):
    if isinstance(error, commands.MemberNotFound):

      embed = disnake.Embed(
        title='Errore',
        description=":x: Membro non trovato, controlla che il tag o l'ID sia corretto e riprova. Se il problema persiste contatta <@710570210159099984>.",
        color=disnake.Color.from_rgb(255, 1, 57)
      )
      await ctx.reply(embed=embed)

      
def setup(bot):
  bot.add_cog(avatar(bot))