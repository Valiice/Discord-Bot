import discord
from discord import FFmpegOpusAudio, client
from discord.ext import commands
import youtube_dl
import asyncio


async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("You're not in a voice channel!")
        return
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, url):
        await join(ctx)
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
            "executable": r"C:\FFmpeg\bin\ffmpeg.exe",
        }
        YDL_OPTIONS = {"format": "bestaudio"}
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info["formats"][0]["url"]
            source = await FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
            await ctx.send(f"Now playing {info['title']}.")

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Paused ⏸️")

    @commands.command()
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("Resume ▶️")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        secondint = 20

        # Im too tired for this shit. If i remove this it breaks...
        for member in before.channel.members:
            if member.bot:
                # onlyBot = True
                print(member.name)

        if len(before.channel.members) == 1 and member.bot:
            print("start timer")
            while True:
                secondint -= 1
                if secondint == 0:

                    bot_connection = member.guild.voice_client
                    await bot_connection.disconnect()
                    print("timer has ended")
                    break
                await asyncio.sleep(1)


def setup(bot):
    bot.add_cog(Music(bot))
