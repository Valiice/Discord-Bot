DEBUG = True

if DEBUG:
    print("We are in debug")
    from pathlib import Path
    from dotenv import load_dotenv

    env_path = Path(".") / ".env.debug"
    load_dotenv(dotenv_path=env_path)
    from settings_files._global import *
else:
    print("We are in production")
    from settings_files._global import *
