# 
# @Author: chengjiawei
# @Date: 2020-04-09 11:33:53
# @Last Modified by: chengjiawei
# @Last Modified time: 2020-04-09 11:33:53
# # #


import os
from django.conf import settings
from loguru import logger


logfile = os.path.join((settings.CONFIG_LOGS["DIR"]), "info_{time}.log")
rotation = settings.CONFIG_LOGS["ROTATION"]
retention = settings.CONFIG_LOGS["RETENTION"]
log_format = settings.CONFIG_LOGS["FORMAT"]
log_level = settings.CONFIG_LOGS["LEVEL"]

logger.add(logfile, format=log_format, rotation=rotation, retention=retention, level=log_level)
