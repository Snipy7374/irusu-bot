import disnake
import os
import sys
import json
import asyncio
import random
from disnake.ext import commands


if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)
    whiteListedChannel = config["877130463662182410"]["whitelisted-channel"]


class ball(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.whiteListedChannel = whiteListedChannel


  @commands.command(aliases=['8ball'])
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def ball(self, ctx):

    choices = {
      "E' decisamente così": "🟢",
      "E' certo": "🟢",
      "Senza dubbio": "🟢",
      "Decisamente sì":"🟢",
      "Puoi contarci": "🟢",
      "Da come la vedo io, sì": "🟢",
      "Probabilmente": "🟢",
      "Buone prospettive": "🟢",
      "Sì": "🟢",
      "I segni dicono di sì": "🟢",
      "Risposta confusa, riprova": "🟡",
      "Richiedi dopo": "🟡",
      "Meglio non risponderti adesso": "🟡",
      "Impossibile predirlo adesso": "🟡",
      "Concentrati e chiedilo nuovamente": "🟡",
      "Non contarci": "🔴",
      "La mia risposta è no": "🔴",
      "Le mie risosrse dicono di no": "🔴",
      "Le prospettive non sono così buone": "🔴",
      "Sono molto dubbioso": "🔴",
      "Decisamente no": "🔴",
      "Non è certamente così": "🔴",
      "No": "🔴"
    }

    if str(ctx.channel.id) not in self.whiteListedChannel:
      await ctx.reply(':x: Questo canale non è in whitelist, pertanto i comandi sono disabilitati!')
      return

    elif str(ctx.channel.id) in self.whiteListedChannel:

      response = random.choice(list(choices.keys()))
      emoji = choices[response]

      if ctx.author.avatar == None:
        ctxAuthorAvatar = ctx.author.default_avatar
        
      elif ctx.author.avatar != None:
        ctxAuthorAvatar = ctx.author.avatar

      if 'snipy' in ctx.message.content.lower():
        embed = disnake.Embed(
          title="🔮 8ball",
          description=f"**La tua domanda**\n{ctx.message.content[7:]}",
          color=disnake.Color.from_rgb(255, 209, 220)
        )
        embed.add_field(
          name="La mia risposta",
          value=f":x: Non posso rispondere!!!",
          inline=False
        )
        embed.set_author(
          name=f"{ctx.author.name}#{ctx.author.discriminator}",
          icon_url=f"{ctxAuthorAvatar}"
        )
        await ctx.reply(embed=embed)
        return
      
      
      embed = disnake.Embed(
        title="🔮 8ball",
        description=f"**La tua domanda**\n{ctx.message.content[7:]}",
        color=disnake.Color.from_rgb(255, 209, 220)
      )
      embed.add_field(
        name="La mia risposta",
        value=f"{emoji} {response}",
        inline=False
      )
      embed.set_author(
        name=f"{ctx.author.name}#{ctx.author.discriminator}",
        icon_url=f"{ctxAuthorAvatar}"
      )
      await ctx.reply(embed=embed)


  @ball.error
  async def ball_error(self, ctx, error):
    if 'You are on cooldown.' in str(error):
      
      message = await ctx.reply(f':x: Sei in cooldown! Aspetta ancora {str(error)[33:40]} per poter usare questo comando!')
      await asyncio.sleep(2)
      await ctx.message.delete()
      await asyncio.sleep(2)
      await message.delete()

      

        
def setup(bot):
  bot.add_cog(ball(bot))