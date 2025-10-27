import discord
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='general')
        if channel:
            embed = discord.Embed(
                title="¡Bienvenido!",
                description=f"Oye, {member.mention} trata de no ser manco 😅",
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            await channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Welcome(bot))
