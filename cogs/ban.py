import disnake
import datetime
from disnake.ext.commands import has_permissions
from disnake.ext.commands import MissingPermissions
from disnake.ext import commands


class ban(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @has_permissions(ban_members =True)
  async def ban(self, ctx, member: disnake.Member = None, *, reason = "Nessuna motivazione fornita"):
    logsChannel = self.bot.get_channel(877143830955180102)
    guild =  self.bot.get_guild(877130463662182410)

    if member.avatar == None:
      memberAvatar = member.default_avatar
    else:
      memberAvatar = member.avatar
    
    if member == None:
      
      embed = disnake.Embed(
        title=f'Errore',
        color=disnake.Color.from_rgb(255, 1, 57),
        description=":x: Devi specificare un membro da bannare per poter usare questo comando!"
      )
      await ctx.reply(embed=embed)
      return

    if int(member.id) == int(ctx.author.id):
      embed = disnake.Embed(
        title='Errore',
        color=disnake.Color.from_rgb(255, 1, 57),
        description=":x: Non puoi bannare te stesso!"
      )
      await ctx.reply(embed=embed)
      return

    elif int(member.id) == int(self.bot.user.id):
      embed = disnake.Embed(
        title='Errore',
        color=disnake.Color.from_rgb(255, 1, 57),
        description=f":x: Non puoi bannare {self.bot.user.name}#{self.bot.user.discriminator}!"
      )
      await ctx.reply(embed=embed)
      return



    elif member != None:
      
      embed = disnake.Embed(
        title=f'Membro {member.name}#{member.discriminator} bannato!',
        description=f"{member.name}#{member.discriminator} è stato bannato da {ctx.author.name}#{ctx.author.discriminator}",
        color=disnake.Color.from_rgb(255, 1, 57),
        timestamp=datetime.datetime.utcnow()
      )
      embed.add_field(
        name="Motivo",
        value=f"{reason}"
      )
      embed.set_author(
        name=f"Comando eseguito da {ctx.author.name}#{ctx.author.discriminator}"
      )
      embed.set_thumbnail(
        url=f"{memberAvatar}"
      )
      await member.ban(reason=reason)
      await member.send(
        f"Sei stato bannato da {guild} dallo staffer {ctx.author.name}#{ctx.author.discriminator} per la seguente motivazione: {reason}"
      )
      await ctx.reply("Membro bannato!")

      await logsChannel.send(
        f"`[{datetime.datetime.utcnow().strftime('%H:%M:%S | %d-%m-%Y')}]` **{ctx.author.name}#{ctx.author.discriminator}**\n(ID:{ctx.author.id}) ha bannato un utente:",
        embed=embed
      )

  
  @ban.error
  async def ban_error(self, ctx, error):
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
        description=f":x: {ctx.author.mention} non hai il permesso di bannare utenti in questo server!",
        color=disnake.Color.from_rgb(255, 1, 57)
      )
      await ctx.reply(embed=embed)

    elif str(error) == "Command raised an exception: AttributeError: 'NoneType' object has no attribute 'avatar'":

      embed = disnake.Embed(
        title=f'Errore',
        color=disnake.Color.from_rgb(255, 1, 57),
        description=":x: Devi specificare un membro da bannare per poter usare questo comando!"
      )
      await ctx.reply(embed=embed)

      
def setup(bot):
  bot.add_cog(ban(bot))