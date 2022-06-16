import disnake
import os
import sys
import json
import subprocess
from disnake.ext import commands


if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)


class slashPing(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(description="Risponde inviando la latenza del bot e altre informazioni utili.")
  async def ping(self, inter):

    embed = disnake.Embed(
      title='Informazioni sul Bot',
      color=disnake.Color.from_rgb(255, 209, 220)
    )

    embed.add_field(
      name='Latenza',
      value=f'{round(self.bot.latency * 1000)} ms',
      inline=False
    )
    embed.add_field(
      name='Versione della libreria', 
      value=f"`{disnake.__version__}`", 
      inline=False
    )

    x = int(subprocess.check_output('cat /proc/cpuinfo | grep "physical id" | sort -u | wc -l', shell=True))
    
    embed.add_field(
      name='Numero di socket della CPU', 
      value=f"{x}", 
      inline=True
    )
    embed.add_field(
      name='Memoria Totale', 
      value="1024 Mb", 
      inline=True
    )
    await inter.response.send_message(embed=embed)


      
def setup(bot):
  bot.add_cog(slashPing(bot))