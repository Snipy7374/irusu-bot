import os
import disnake
from disnake.ext import commands
from disnake.ext.commands import BucketType, cooldown
from disnake.ext.commands import has_permissions
from disnake.ext.commands import MissingPermissions
import nest_asyncio
import json
import asyncio
import sys
from replit import db

#del db["710570210159099984"]
#db["710570210159099984"] = {"wallet": 100, "bank": 500000, "invetary": ["apple", "water"]}
nest_asyncio.apply()

with open('./market.json') as f:
    d1 = json.load(f)



class economy(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


  @commands.Cog.listener()
  async def on_ready(self):
    print("Comandi economy caricati correttamente")

  async def open_account(self, id: int):
    db[str(id)] = {"wallet": 0, "bank": 100, "inventary": []}

  async def update_wallet(self, id: int, wallet: int):
    if id is not None:
      user_info = db[str(id)]
      user_info["wallet"] = wallet

  async def update_bank(self, id: int, bank: int):
    if id is not None:
      user_info = db[str(id)]
      user_info["bank"] = bank

  async def delete_profile(self, id: int):
    if id is not None:
      del db[str(id)]

  @commands.command()
  async def delete(self, ctx, member: disnake.Member = None):

    if member is None:
      member = ctx.author

    await self.delete_profile(member.id)
    await ctx.send(f"Profilo di {member.mention} cancellato!")

  @commands.command()
  async def register(self, ctx):

    users = db.keys()
    
    if str(ctx.author.id) in users:
      await ctx.send(f"Membero {ctx.author.mention} già registrato!")
      
    if str(ctx.author.id) not in users:
      await self.open_account(ctx.author.id)
      await ctx.send(f"Membro {ctx.author.mention} registrato!")

  @commands.command()
  @has_permissions(administrator=True)
  async def forceRegister(self, ctx, member: disnake.Member = None):

    users = db.keys()

    if member is None:
      await ctx.send("Impossibile registrare forzatamente il nulla, bakaaa!")
      return
    
    if str(member.id) in users:
      await ctx.send(f"Membero {member.mention} già registrato!")
    
    if str(member.id) not in users:
      await self.open_account(member.id)
      await ctx.send(f"{member.mention} registrato correttamente!")


  @commands.command()
  async def balance(self, ctx, member: disnake.Member = None):

    if member is None:
      member = ctx.author


    user_info = db[f"{str(member.id)}"] 
    # {"wallet": int, "bank": int, "inventary": ["apple", "water"]}
    embed = disnake.Embed(
      title=f"Balance di {member.display_name}",
      colour=disnake.Color.from_rgb(255, 209, 220)
    )
    embed.add_field(
      name="Wallet",
      value=f'`{user_info["wallet"]}`',
      inline=False
    )
    embed.add_field(
      name="Bank",
      value=f'`{user_info["bank"]}`',
      inline=False
    )
    if user_info["inventary"] == []:
      inventary = "Vuoto"
    else:
      inventary = user_info["inventary"]
    embed.add_field(
      name="Inventario",
      value=f'{inventary}',
      inline=False
    )

    if ctx.author.avatar != None:
      avatar = ctx.author.avatar
    else:
      avatar = ctx.author.default_avatar

    embed.set_author(
      name=f"{ctx.author.name}#{ctx.author.discriminator}", 
      icon_url=f"{avatar}"
    )
  
    await ctx.send(embed=embed)

  
  @commands.command()
  async def wallet(self, ctx, wallet: int, member: disnake.Member = None):

    if member is None:
      member = ctx.author

    if member.id == 710570210159099984:
      await self.update_wallet(member.id, wallet)
      await ctx.send(f'Wallet di {member.name}#{member.discriminator} settato a `{db[str(member.id)]["wallet"]}`')
    else:
      await ctx.send(":x: Non hai il permesso di eseguire questo comando!")

  @commands.command()
  async def bank(self, ctx, bank: int, member: disnake.Member = None):

    if member is None:
      member = ctx.author

      if member.id == 710570210159099984:
        await self.update_bank(member.id, bank)
        await ctx.send(f"{db[str(member.id)]['bank']}")
      else:
        await ctx.send(":x: Non hai il permesso di eseguire questo comando!")


  @forceRegister.error
  async def forceRegister_error(self, ctx, error):
    if isinstance(error, commands.MemberNotFound):

      embed = disnake.Embed(
        title='Errore',
        description=":x: Membro non trovato, controlla che il tag o l'ID sia corretto e riprova. Se il problema persiste contatta <@710570210159099984>.",
        color=disnake.Color.from_rgb(255, 1, 57)
      )
      await ctx.reply(embed=embed)

    elif isinstance(error, MissingPermissions):

      embed = disnake.Embed(
        title="Errore",
        description=f":x: {ctx.author.mention} non hai il permesso di usare questo comando!",
        color=disnake.Color.from_rgb(255, 1, 57)
      )
      await ctx.reply(embed=embed)

  @wallet.error
  async def wallet_error(self, ctx, error):

    if str(error) == 'Converting to "int" failed for parameter "wallet".':

      embed = disnake.Embed(
        title="Errore",
        description=f":x: valore non valido, perfavore utilizza solamente numeri interi!",
        color=disnake.Color.from_rgb(255, 1, 57)
      )
      await ctx.reply(embed=embed)

        
def setup(bot):
  bot.add_cog(economy(bot))
