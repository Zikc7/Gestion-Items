from .setting import Setting
from .logging import config_logger


app_settings = Setting()
config_logger(app_settings.DEBUG)