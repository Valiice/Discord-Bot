from .model import ActivitiesStatus


class ActivitiesController:
    current_activity = None

    def activity_commands(self):
        self.current_activity = ActivitiesStatus()
        return self.current_activity.get_choices()

    def change_activ(self, bot_activity: str, status: str):
        self.current_activity = ActivitiesStatus(status)
        new_activ = self.current_activity.change_activity(bot_activity)
        return new_activ
