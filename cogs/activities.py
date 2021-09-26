from activities.controller import ActivitiesController
import discord
from discord.ext import commands

from utils import (
    create_voice_channel,
    get_category_by_name,
    get_channel_by_name,
    mods_or_admin,
)


class Activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        brief="Let's you change the activity of the bot",
        usage="[play | stream | listen | watch] [title]",
    )
    @mods_or_admin()
    async def activity(
        self,
        ctx,
        bot_status: str = "stream",
        *,
        status: str = ">help | Check out the bot with the url",
    ):
        """
        Change the activity of the bot with >activity [play | stream | listen | watch] [title]
        """
        ctx.show_instance = ActivitiesController()
        activity_status = bot_status
        activity = ctx.show_instance.change_activ(activity_status, status)
        await self.bot.change_presence(activity=activity)
        await ctx.send(
            f"Activity changed to {activity_status} with message {activity.name}"
        )


def setup(bot):
    bot.add_cog(Activities(bot))
