import disnake
import datetime
from disnake.ext.commands import has_permissions
from disnake.ext import commands


class slashBan(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(description="Banna un utente.")
  @has_permissions(ban_members=True)
  async def ban(self, inter, member: disnake.Member, *, cronologia: int = None, reason = "Nessuna motivazione fornita dallo staff"):
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
      await inter.response.send_message(embed=embed)
      return

    if int(member.id) == int(inter.author.id):
      embed = disnake.Embed(
        title='Errore',
        color=disnake.Color.from_rgb(255, 1, 57),
        description=":x: Non puoi bannare te stesso!"
      )
      await inter.response.send_message(embed=embed)
      return

    elif int(member.id) == int(self.bot.user.id):
      embed = disnake.Embed(
        title='Errore',
        color=disnake.Color.from_rgb(255, 1, 57),
        description=f":x: Non puoi bannare {self.bot.user.name}#{self.bot.user.discriminator}!"
      )
      await inter.response.send_message(embed=embed)
      return



    elif member != None:
      
      embed = disnake.Embed(
        title=f'Membro {member.name}#{member.discriminator} bannato!',
        description=f"{member.name}#{member.discriminator} è stato bannato da {inter.author.name}#{inter.author.discriminator}",
        color=disnake.Color.from_rgb(255, 1, 57),
        timestamp=datetime.datetime.utcnow()
      )
      embed.add_field(
        name="Motivo",
        value=f"{reason}"
      )
      embed.set_author(
        name=f"Comando eseguito da {inter.author.name}#{inter.author.discriminator}"
      )
      embed.set_thumbnail(
        url=f"{memberAvatar}"
      )
      await member.ban(delete_message_days=cronologia ,reason=reason)
      await member.send(
        f"Sei stato bannato da {guild} dallo staffer {inter.author.name}#{inter.author.discriminator} per la seguente motivazione: {reason}"
      )
      await inter.response.send_message("Membro bannato!")

      await logsChannel.send(
        f"`[{datetime.datetime.utcnow().strftime('%H:%M:%S | %d-%m-%Y')}]` **{inter.author.name}#{inter.author.discriminator}**\n(ID:{inter.author.id}) ha bannato un utente:",
        embed=embed
      )

      
def setup(bot):
  bot.add_cog(slashBan(bot))