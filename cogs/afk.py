import disnake
import os
import sys
import json
import asyncio
from replit import db
from disnake.ext import commands


if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)


class afk(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  
  @commands.command(aliases=['setafk'])
  async def afk(self, ctx, reason = None):

    if reason is None:
      reason = "Motivo non fornito dall'utente"
    else:
      reason = ctx.message.content[5:]

    afk_user = db.keys()
    
    if f"afk{str(ctx.author.id)}" in afk_user:
      msg = await ctx.reply(f"{ctx.author.mention} già afk!")
      await asyncio.sleep(2)
      await msg.delete()
      return

    else:

      db[f"afk{str(ctx.author.id)}"] = [reason]
    

    #await ctx.send(db["afk"].keys())
      await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}")
      await ctx.reply(f"{ctx.author.mention} ho impostato il tuo profilo come AFK con il seguente motivo: {reason}")

  @commands.command()
  async def noafk(self, ctx, member: disnake.Member = None):

    if member is None:
      member = ctx.author
      
    if ctx.author.id == 710570210159099984:
      del db[f"afk{member.id}"]
      msg = await ctx.send(f"{member.id} settato come non AFK")
      await asyncio.sleep(2)
      await msg.delete()
      

    else:
      await ctx.send("Non hai il permesso necessario per eseguire questo comando")


  @commands.Cog.listener()
  async def on_message(self, message):

    # {"afk123": [reason]}
    #await ctx.send(f'{next(v for k,v in db.items() if k.startswith("afk"))}')
    afk_user = [v for v in db.keys() if v.startswith("afk")]

    for i in afk_user:
      if message.author.id == 948229353077112872:
        return
        
      if f"{i[3:]}" in message.content:
        reason = str(db[f'afk{i[3:]}'])
        await message.reply(f"Il membro che hai menzionato è AFK per il seguente motivo: {reason[21:len(reason)-3]}")

    if message.reference is not None:

      msg = await message.channel.fetch_message(message.reference.message_id)
      #print(msg.author.id)
      if f"afk{msg.author.id}" in afk_user:
        reason = str(db[f'afk{msg.author.id}'])
        await message.reply(f"Il membro a cui hai risposto è AFK per il seguente motivo: {reason[21:len(reason)-3]}")
      

    if message.content.startswith(">afk"):
      return
    if f"afk{message.author.id}" in db.keys():
      del db[f"afk{message.author.id}"]
      await message.author.edit(nick=f"{message.author.display_name[6:]}")
      msg = await message.reply("Non sei più AFK!")
      await asyncio.sleep(2)
      await msg.delete()

  @commands.command()
  async def afklist(self, ctx):
    if ctx.author.id == 710570210159099984:
      
      afk_list = [v for v in db.keys() if v.startswith('afk')]
      
      embed = disnake.Embed(
        title="Membri AFK",
        color=disnake.Color.from_rgb(255, 209, 220)
      )
      for i in afk_list:
        embed.add_field(
          name=f"DB id: {i}",
          value=f"<@!{i[3:]}>",
          inline=False
        )
      await ctx.send(embed=embed)
    else:
      return


    
      
def setup(bot):
  bot.add_cog(afk(bot))