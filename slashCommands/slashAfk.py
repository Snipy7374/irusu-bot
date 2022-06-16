import disnake
import os
import sys
from disnake.ext.commands import has_permissions
from disnake.ext.commands import MissingPermissions
import json
import asyncio
from replit import db
from disnake.ext import commands


if not os.path.isfile("./config.json"):
  sys.exit("Config file not found")

else:
  with open("./config.json") as file:
    config = json.load(file)


class slashAfk(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command()
  async def afk(self, inter):
    return
  
  @afk.sub_command(description="Imposta il tuo profilo come AFK e setta un motivo da mostrare")
  async def set(self, inter, reason = None):

    if reason is None:
      reason = "Motivo non fornito dall'utente"

    afk_user = db.keys()
    
    if f"afk{str(inter.author.id)}" in afk_user:
      await inter.response.send_message(f"{inter.author.mention} già afk!")
      return

    else:
    #await ctx.send(db["afk"].keys())
      if len(inter.author.display_name) < 27:
        await inter.author.edit(nick=f"[AFK] {inter.author.display_name}")
        db[f"afk{str(inter.author.id)}"] = [reason]
        await inter.response.send_message(f"{inter.author.mention} ho impostato il tuo profilo come AFK con il seguente motivo: {reason}")
      if len(inter.author.display_name) >= 27:
        db[f"afk{str(inter.author.id)}"] = [reason]
        await inter.response.send_message(f"{inter.author.mention} ho impostato il tuo profilo come AFK con il seguente motivo: {reason}\n Tuttavia non ho potuto modificare il tuo nickname perchè troppo lungo!")


  @afk.sub_command_group()
  async def mod(self, inter):
    return

  @mod.sub_command(description="Resetta il motivo di un membro AFK")
  @has_permissions(manage_nicknames=True)
  async def reset(self, inter, member: disnake.Member = None):

    reason = "Motivo non fornito dall'utente"
    afk_list = [v for v in db.keys() if v.startswith('afk')]

    if member is None:


      if f"afk{inter.author.id}" in afk_list:
        db[f"afk{str(inter.author.id)}"] = [reason]
        await inter.response.send_message(f"{inter.author.mention} ho reimpostato il tuo motivo AFK allo stato di default: {reason}")
      else:
        await inter.response.send_message(f"{inter.author.mention} non sei AFK!")

    elif member is not None:

      if f"afk{member.id}" in afk_list:
        db[f"afk{str(member.id)}"] = [reason]
        await inter.response.send_message(f"Motivo AFK di {member.name}#{member.discriminator} (`{member.id}`) è stato reimpostato al valore di default")
      else:
        await inter.response.send_message(f"{member.name}#{member.discriminator} non è AFK!")

  
  @mod.sub_command(description="Ottieni la lista di tutti gli utenti AFK")
  @has_permissions(manage_nicknames=True)
  async def list(self, inter):

    afk_list = [v for v in db.keys() if v.startswith('afk')]

    
    if afk_list == []:  
      embed = disnake.Embed(
        title="Membri AFK",
        description="Nessun membro AFK :'(",
        color=disnake.Color.from_rgb(255, 209, 220)
      )
      
    else:
      embed = disnake.Embed(
        title="Membri AFK",
        color=disnake.Color.from_rgb(255, 209, 220)
      )
      
      for i in afk_list:

        reason = db[i]
        
        embed.add_field(
          name=f"DB id: {i}",
          value=f"<@!{i[3:]}>\n{str(reason)[20:len(reason)-3]}",
          inline=False
        )
    await inter.response.send_message(embed=embed)

  @mod.sub_command(description="Rimuovi un utente dalla lista degli AFK con un ID")
  @has_permissions(manage_nicknames=True)
  async def clear_with_id(self, inter, id = None):

    if id is None:
      id = inter.author.id

    try:
      del db[f"afk{id}"]
    except:
      await inter.response.send_message(f"{id} questo utente non può essere rimosso dalla lista degli AFK perchè non è AFK o perchè non esiste")
    
    await inter.response.send_message(f"{id} settato come non AFK")
    if len(inter.author.display_name) < 27:
      await inter.author.edit(nick=f"{inter.author.display_name[4:]}")
    if len(inter.author.display_name) >= 27 and "[AFK]" not in str(inter.author.display_name):
      return


  @mod.sub_command(description="Rimuovi un utente dalla lista degli AFK")
  @has_permissions(manage_nicknames=True)
  async def clear(self, inter, member: disnake.Member = None):

    if member is None:
      member = inter.author
      
    del db[f"afk{member.id}"]
    await inter.response.send_message(f"{member.id} settato come non AFK")
    if len(inter.author.display_name) < 27:
      await inter.author.edit(nick=f"{inter.author.display_name[4:]}")
    if len(inter.author.display_name) >= 27 and "[AFK]" not in str(inter.author.display_name):
      return

  @clear_with_id.error
  async def clear_with_id_error(self, inter, error):
    if isinstance(error, MissingPermissions):
      embed = disnake.Embed(
        title="Errore",
        description=f":x: {inter.author.mention} Non hai il permesso necessario per eseguire questo comando! (Gestire nickname)",
        color=disnake.Color.from_rgb(255, 1, 57)
      )
      await inter.response.send_message(embed=embed)
  
  @clear.error
  async def clear_error(self, inter, error):
    if isinstance(error, MissingPermissions):

      embed = disnake.Embed(
        title="Errore",
        description=f":x: {inter.author.mention} Non hai il permesso necessario per eseguire questo comando! (Gestire nickname)",
        color=disnake.Color.from_rgb(255, 1, 57)
      )
      
      await inter.response.send_message(embed=embed)


  @list.error
  async def list_error(self, inter, error):
    if isinstance(error, MissingPermissions):

      embed = disnake.Embed(
        title="Errore",
        description=f":x: {inter.author.mention} Non hai il permesso necessario per eseguire questo comando! (Gestire nickname)",
        color=disnake.Color.from_rgb(255, 1, 57)
      )
      
      await inter.response.send_message(embed=embed)

  


    
      
def setup(bot):
  bot.add_cog(slashAfk(bot))