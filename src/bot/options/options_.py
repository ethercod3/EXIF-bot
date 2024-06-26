from enum import Enum


class ActionEnum(Enum):
    View = "View"
    Delete = "Delete"


class VirtualEnv(Enum):
    save_file_to = "SAVE_TO"
    bot_token = "BOT_TOKEN"