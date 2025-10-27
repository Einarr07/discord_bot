import discord
from discord.ext import commands


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rolmenu(self, ctx):
        embed = discord.Embed(title="Elige tu rol", description="Reacciona con 💧 para el rol de Hidratado")
        message = await ctx.send(embed=embed)
        await message.add_reaction("💧")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.bot:
            return
        guild = reaction.message.guild
        role = discord.utils.get(guild.roles, name="Hidratado")
        if role and str(reaction.emoji) == "💧":
            await user.add_roles(role)
            await user.send("Te asigné el rol **Hidratado 🚰**. ¡Mantente fresco!")


async def setup(bot):
    await bot.add_cog(Roles(bot))
