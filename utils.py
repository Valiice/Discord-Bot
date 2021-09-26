import json
import random
import os

import requests

# from emoji import UNICODE_EMOJI_ENGLISH

from settings import *

from discord.ext import commands

from settings import MODERATOR_ROLE_NAME, BOT_OWNER_ID


async def create_text_channel(guild, channel_name):
    """
    Create a new text channel in the category "Game"
    """
    category = get_category_by_name(guild, "Games")
    channel = await guild.create_text_channel(channel_name, category=category)
    return channel


async def create_voice_channel(
    guild, channel_name, category_name="voice-channels", user_limit=None
):
    """
    Create a new voice channel in the category "Game"
    """
    category = get_category_by_name(guild, category_name)
    channel = await guild.create_voice_channel(
        channel_name, category=category, user_limit=user_limit
    )
    return channel


def get_channel_by_name(guild, channel_name):
    """
    Get channel object by channel_name
    """
    channel = None
    for c in guild.channels:
        if c.name.lower() == channel_name.lower():
            channel = c
            break
    return channel


def get_category_by_name(guild, category_name):
    """
    Get category object by category_name
    """
    category = None
    for c in guild.categories:
        if c.name == category_name:
            category = c
            break
    return category


def perm_checker(ctx):
    if ctx.author.id == 168526449832099841:
        return True
    for role in ctx.author.roles:
        role = role.name
        if role == MODERATOR_ROLE_NAME:
            return True


def mods_or_admin():
    async def predicate(ctx):
        return perm_checker(ctx)

    return commands.check(predicate)


def bot_maker():
    async def predicate(ctx):
        if ctx.author.id == BOT_OWNER_ID:
            return True

    return commands.check(predicate)


async def notify_user(member, message):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
        await channel.send(message)


# def is_emoji(s):
#     count = 0
#     for emoji in UNICODE_EMOJI_ENGLISH:
#         count += s.count(emoji)
#         if count > 1:
#             return False
#     return bool(count)
