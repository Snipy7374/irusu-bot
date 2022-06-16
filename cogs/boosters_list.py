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


class boosters(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['boosters', 'contributors', 'boosterslist', 'listboosters', 'boosterlist', 'listbooster', 'blist'])
  async def booster(self, ctx):

    bList = []
    for i in ctx.guild.premium_subscribers:
      member = i.mention + " " + i.premium_since.strftime('%d/%m/%Y')
      bList.append(member)
    
    outList = '\n'.join(bList)
    
    embed = disnake.Embed(
      title=f'Lista dei boosters di {ctx.guild.name}',
      color=disnake.Color.from_rgb(255, 209, 220),
      description=f"**Grazie a tutti voi!!**\n\n{outList}"
    )
    
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    await ctx.reply(embed=embed)

      
def setup(bot):
  bot.add_cog(boosters(bot))