from discord.ext import commands
import discord

import datetime

from utils import mods_or_admin

from settings import BOT_OWNER_ID


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Unload the cog")
    @mods_or_admin()
    async def unload(self, ctx, cog: str):
        """
        Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner
        """
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("Could not unload cog")
            return
        await ctx.send("Cog unloaded")

    @commands.command(brief="Load the cog")
    @mods_or_admin()
    async def load(self, ctx, cog: str):
        """
        Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner
        """
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not load cog")
            return
        await ctx.send("Cog loaded")

    @commands.command(brief="Reload the cog")
    @mods_or_admin()
    async def reload(self, ctx, cog: str):
        """
        Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner
        """
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could not reload cog")
            return
        await ctx.send("Cog reloaded")

    @commands.command(brief="Gets the server status")
    @mods_or_admin()
    async def status(self, ctx):
        """
        This shows a bigger interface about the server status
        """
        guild = ctx.guild

        no_voice_channels = len(guild.voice_channels)
        no_text_channels = len(guild.text_channels)

        embed = discord.Embed(
            description="Server Status", colour=discord.Colour.blurple()
        )

        # embed.set_thumbnail(
        #     url="https://media.discordapp.net/attachments/759103848844623912/861295912759459860/CatMaidEmoji.png"
        # )

        # embed.set_image(
        #     url="https://cdn.discordapp.com/attachments/759103848844623912/860592076818612254/E3iNhyTXMAQeG0B.jpg"
        # )

        emoji_string = ""
        for e in guild.emojis:
            if e.is_usable():
                emoji_string += str(e)
        embed.add_field(
            name="Custom Emoji",
            value=emoji_string or "No emoji available",
            inline=False,
        )

        embed.add_field(name="Server Name", value=guild.name, inline=False)

        embed.add_field(name="# Voice Channels", value=no_voice_channels)

        embed.add_field(name="# Text Channels", value=no_text_channels)

        embed.add_field(name="AFK Channel", value=guild.afk_channel)
        bot_owner = self.bot.get_user(BOT_OWNER_ID)
        embed.add_field(
            name="Bot Maker",
            value=f"Please contact {bot_owner.name}#{bot_owner.discriminator} if something is wrong with the bot.",
            inline=False,
        )
        embed.set_author(name=self.bot.user.name)
        embed.set_footer(text=datetime.datetime.now())
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))
