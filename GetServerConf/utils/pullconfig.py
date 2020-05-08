#!/lingtian/opt/python363/bin/python3
#_*_coding: utf-8_*_

# Author: chengjiawei@shein.com
# Date: 2020/02/17

import subprocess
import os
from django.conf import settings
from logger import logger
from rsyncCheck import rsyncCheck
import sys
import uuid
# directry check if end with "/" or not


# config file rsync
class rsyncGet(object):
	'''
	configFile为配置文件的名称，serverModule为rsync的模块名，若配置文件configFile不在服务的rsync模块对应的目录下，则需要填写相对路径
	适用于无密码传输模式
	'''
	def __init__(self, dstConfDir, configFile, server_name):
		self.dstConfDir = dstConfDir
		self.configFile = configFile
		self.server_name = server_name


	def readConfig(self, communicate_info):
		if 'message' not in communicate_info:
			with open(os.path.join(self.dstConfDir, self.server_name, self.configFile)) as f:
				lines = f.read()
				return lines

	def TempDir(self):
		if not os.path.exists(os.path.join(self.dstConfDir, self.server_name)):
			os.makedirs(os.path.join(self.dstConfDir, self.server_name))
		return os.path.join(self.dstConfDir, self.server_name)

	def delTempDir(self):
		os.rmdir(os.path.join(self.dstConfDir, self.server_name, self.configFile))

			
	def doCmd(self, rsyncDir, serverIp, serverModule):
		tempDir = self.TempDir()
		cmd = [rsyncDir, '-avz', 'test@' + serverIp + '::' + serverModule + '/' + self.configFile, tempDir]
		try:
			res = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		except FileNotFoundError as ex:
			logger.error('config Server has no'+self.rsyncDir + ex)
			messages = {
				"message" : "服务器为安装rsync客户端"
			} 
		res.wait()
		if res.poll() == 0:
			return res.communicate()
			# for line in res.communicate():
			# 	print(line.strip())
	
		elif res.returncode == 23:
			logger.error(self.serverIp+' '+self.serverModule+'has no'+self.configFile)
			messages = {
				"message" : "请确认配置文件路径是否正确"
			}
			
		elif res.returncode == 10:
			logger.error('server error'+self.serverIp)
			messages = {
				"message" : "服务器连接失败，请确认"
			}
		else:
			logger.error('connection timeout > 1000ms')
			messages = {
				"message" : "rsync连接超时（1s）"
			}
		self.delTempDir()
		return messages

				
	

if __name__ == '__main__':

	myrsync = rsyncGet('/lingtian/test_code/data/tempfile', 'application.yml')
	res = myrsync.doCmd('rsync', '10.54.1.54', 'inbox-api-service')
	resconfig = myrsync.readConfig(res)
