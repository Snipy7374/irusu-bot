import disnake
import os
import sys
import json
import datetime
from disnake.ext import commands
from disnake.ext.commands import has_permissions
from disnake.ext.commands import MissingPermissions

members = 0
bots = 0

if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)



class slashInvite(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(description="Ottieni il link di invito del bot.")
  @has_permissions(administrator=True)
  async def invite(self, inter):

    embed = disnake.Embed(
      title='Invitami!!',
      description='https://discord.com/api/oauth2/authorize?client_id=948229353077112872&permissions=8&scope=applications.commands%20bot',
      color=disnake.Color.from_rgb(255, 209, 220)
    )
    embed.set_thumbnail(url=f"{inter.guild.icon}")
    
    await inter.response.send_message(embed=embed)

  @invite.error
  async def invite_error(self, inter, error):
    if isinstance(error, MissingPermissions):
      await inter.response.send_message(":x: Non hai i permessi necessari per vedere queste informazioni (Administrator)!")

def setup(bot):
  bot.add_cog(slashInvite(bot))