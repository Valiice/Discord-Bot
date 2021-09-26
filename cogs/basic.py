from discord.ext import commands
import discord

import datetime

# from TextToOwO.owo import text_to_owo

from utils import notify_user

from settings import BOT_OWNER_ID


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send(
            "Please check with !help the usage of this command or talk to the owner of the bot"
        )

    @commands.command(name="maker", brief="Shows the person who made the bot")
    async def maker_command(self, ctx):
        async with ctx.channel.typing():
            bot_owner = self.bot.get_user(BOT_OWNER_ID)
            embed = discord.Embed(title="Bot Maker", colour=discord.Colour.blurple())

            embed.set_thumbnail(url=f"{bot_owner.avatar_url}")
            embed.add_field(
                name="Contact",
                value=f"You can contact {bot_owner.name}#{bot_owner.discriminator} if something is wrong with the bot.",
                inline=False,
            )
            embed.set_author(name=f"{bot_owner.name}#{bot_owner.discriminator}")
            embed.set_footer(text=datetime.datetime.now())
            await ctx.send(embed=embed)

    @commands.command(
        brief="Sends a ping to the bot and checks the ms between the connection"
    )
    async def ping(self, ctx):
        if round(self.bot.latency * 1000) < 300:
            await ctx.send(f"**Pong {round(self.bot.latency * 1000)}ms**")
        else:
            await ctx.send(f"**Yikes I'm lagging. {round(self.bot.latency * 1000)}ms**")

    @commands.command(brief="Sends the invite link into the chat")
    @commands.guild_only()
    async def invite(self, ctx):
        async with ctx.channel.typing():
            await ctx.send(
                "This is the link to the programming server! https://discord.gg/qBDRGPh4"
            )

    @commands.command(brief="Let's poke a member in their dm's")
    async def poke(self, ctx, member: discord.Member = None):
        if member is not None:
            message = "%s Poked you!!!!" % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("Please use @mention to poke someone.")


def setup(bot):
    bot.add_cog(Basic(bot))
