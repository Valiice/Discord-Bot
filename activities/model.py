import discord


class ActivitiesStatus:
    status_message = ""
    status = {}

    def __init__(self, msg: str = ">help | Check out the bot with the url"):
        self.status_message = msg
        self.status = {
            "play": discord.Game(name=self.status_message),
            "stream": discord.Streaming(
                name=self.status_message,
                url="https://github.com/Valiice/Howest-Discord-Bot",
            ),
            "listen": discord.Activity(
                type=discord.ActivityType.listening, name=self.status_message
            ),
            "watch": discord.Activity(
                type=discord.ActivityType.watching, name=self.status_message
            ),
        }

    def get_choices(self):
        s = " | ".join(x for x in self.status.keys())
        return s

    def change_activity(self, activ):
        if activ in self.status:
            return self.status[activ]
        else:
            activ = "play"
            return self.status[activ]
