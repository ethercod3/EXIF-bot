from enum import StrEnum


class ActionEnum(StrEnum):
    View = "View"
    Delete = "Delete"


class VirtualEnv(StrEnum):
    save_file_to = "SAVE_TO"
    bot_token = "BOT_TOKEN"
