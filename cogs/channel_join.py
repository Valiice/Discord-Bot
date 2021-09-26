from discord.ext import commands

from utils import create_voice_channel, get_category_by_name, get_channel_by_name


class JoinToCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.bot:
            return

        if after.channel is not None:
            if after.channel.name == "Join To Create":
                channel = await create_voice_channel(
                    after.channel.guild,
                    f"{member.name}-voice-channel".lower(),
                    category_name=">Join To Create<",
                )
                if channel is not None:
                    await member.move_to(channel)

        if before.channel is not None:
            if (
                before.channel.category.id
                == get_category_by_name(before.channel.guild, ">Join To Create<").id
            ):
                channel = get_channel_by_name(before.channel.guild, "Join To Create")
                if len(before.channel.members) == 0 and before.channel != channel:
                    await before.channel.delete()


def setup(bot):
    bot.add_cog(JoinToCreate(bot))
