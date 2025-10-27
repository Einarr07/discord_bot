import discord
from discord.ext import commands, tasks


class Reminders(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.water_reminder.start()

    @tasks.loop(minutes=60)
    async def water_reminder(self):
        channel = discord.utils.get(self.bot.get_all_channels(), name="general")
        if channel:
            await channel.send("A pasado una hora, es momento de beber agua. ¡Mantente hidratado!")

    @water_reminder.before_loop
    async def before_reminder(self):
        await self.bot.wait_until_ready()


async def setup(bot):
    await bot.add_cog(Reminders(bot))
