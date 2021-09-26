import os

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR, "data")

# Discord Conf
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", False)
BOT_OWNER_ID = os.getenv("BOT_OWNER_ID", False)

# Permissions
MODERATOR_ROLE_NAME = "admin"

BOT_OWNER_ID = 168526449832099841
