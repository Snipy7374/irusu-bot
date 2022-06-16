import disnake
import os
import sys
import json
from disnake.ext import commands
from disnake.ext.commands import has_permissions
from disnake.ext.commands import MissingPermissions


if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)


class prefixSetter(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['prefix', 'prefixset', 'irusuprefix', 'prefixsetter'])
  @has_permissions(administrator=True)
  async def setprefix(self, ctx, prefix):

    db = {
      str(ctx.guild.id): {
        "prefix": str(prefix)
      }
    }
    json_object = json.dumps(db)
    
    with open("config.json", "w+") as f:  
      f.write(json_object)
      
    return await ctx.reply("Prefix updated to {0}".format(prefix))

  @setprefix.error
  async def setprefix_error(self, ctx, error):
    if isinstance(error, MissingPermissions):
      await ctx.reply(":x: Non hai i permessi necessari per modificare il prefisso (Administrator)!")

  
  @commands.command(aliases=['currentprefix', 'prefixes'])
  @has_permissions(administrator=True)
  async def cprefix(self, ctx):

    with open('config.json', 'r') as jsonFile:
      data = json.load(jsonFile)

      return await ctx.reply(data)

  @cprefix.error
  async def cpreix_error(self, ctx, error):
    if isinstance(error, MissingPermissions):
      await ctx.reply(":x: Non hai i permessi necessari per vedere queste informazioni (Administrator)!")

    
def setup(bot):
  bot.add_cog(prefixSetter(bot))