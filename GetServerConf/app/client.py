#!/lingtian/opt/python363/bin/python3
#_*_coding: utf-8_*_

# Author: chengjiawei@shein.com
# Date: 2020/02/17

import subprocess
import os
from django.conf import settings
from loguru import logger

# directry check if end with "/" or not
def checkDirSlash(dir):
	if dir.endswith('/'):
		return dir
	else:
		return dir+'/'

#  log settting

logfile = checkDirSlash(settings.CONFIG_LOGS["DIR"]) + "info_{time}.log"
rotation = settings.CONFIG_LOGS["ROTATION"]
retention = settings.CONFIG_LOGS["RETENTION"]
log_format = settings.CONFIG_LOGS["FORMAT"]
log_level = settings.CONFIG_LOGS["LEVEL"]

logger.add(logfile, format=log_format, rotation=rotation, retention=retention, level=log_level)


# config file rsync
class myRsync(object):
	def __init__(self, configDir, configFile, dstConfDir, serverIp, serverModule, rsyncDir="/usr/bin/rsync"):
		self.configDir = configDir
		self.rsyncDir = rsyncDir
		self.configFile = configFile
		self.serverIp = serverIp
		self.serverModule = serverModule
		self.dstConfDir = dstConfDir

	def rsyncCheck(func):
		def inner(self, configFile='application.yml'):
			rFlag = os.path.isfile(self.rsyncDir)
			cFlag = os.path.isfile(self.configDir + '/' + configFile)
			if rFlag and cFlag:
				res = func(self, configFile='application.yml')
				return res
			elif not rFlag:
				logger.error("系统无rsync命令，请安装")
				print("系统无rsync命令，请安装")
			else:
				logger.error("无指定的配置文件位置")
				print("无指定的配置文件位置")
		return inner


	def readConfig(self):
		pass		
			

	#@rsyncCheck
	def getConfig(self, configFile="application.yml"):
		cmd = [self.rsyncDir, '-avz', 'test@' + self.serverIp + '::' + self.serverModule + '/' + configFile, self.dstConfDir]
		res = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		res.wait()
		if res.poll() == 0:
			for line in res.communicate():
				print(line.strip())
	
		elif res.returncode == 23:
			messages = {
				"message" : "请确认配置文件路径是否正确"
			}
			print(messages["message"])
		else:
			print(res.returncode)
			print("命令执行超时（1s）")
	def checkDstConfDir(self):
		try:
				
	@rsyncCheck
	def pullConfig(self):
		pass
	

if __name__ == '__main__':

	myrsync = myRsync(configDir='/lingtain/code/java/inbox-api-service', configFile='application.yml', dstConfDir='/lingtian/test_code/data/tempfile', serverIp='10.54.1.54', serverModule='inbox-api-service')
	myrsync.getConfig("applicatin.yml")
