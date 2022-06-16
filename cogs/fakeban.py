import disnake
import os
import sys
import datetime
import json
from disnake.ext import commands


if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)
    whiteListedChannel = config["877130463662182410"]["whitelisted-channel"]


class fakeBan(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.whiteListedChannel = whiteListedChannel


  @commands.command(aliases=['fban', 'trollban'])
  async def fakeBan(self, ctx, member: disnake.Member = None):

    reason = 'Complimenti sei stato trollato'

    if str(ctx.channel.id) not in self.whiteListedChannel:
      await ctx.reply(':x: Questo canale non è in whitelist, pertanto i comandi sono disabilitati!')
      return

    elif str(ctx.channel.id) in self.whiteListedChannel:

      if member == None:
        await ctx.reply(":x: per poter bannare qualcuno devi specificare l'utente da bannare!")
        return

      elif member != None:

        embed = disnake.Embed(
          title=f"{member.name}#{member.discriminator} è stato bannato!",
          description=f"{member.mention} è stato bannato da {ctx.author.name}#{ctx.author.discriminator} alle ore {datetime.datetime.utcnow().strftime('%H:%M:%S %d/%m/%y')} per il seguente motivo:\n `{reason}`",
          color=disnake.Color.from_rgb(255, 1, 57)
        )
        await ctx.reply(embed=embed)

      

        
def setup(bot):
  bot.add_cog(fakeBan(bot))