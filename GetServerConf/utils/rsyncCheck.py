# 
# @Author: chengjiawei
# @Date: 2020-04-08 18:16:01
# @Last Modified by: chengjiawei
# @Last Modified time: 2020-04-08 18:16:01
# # #/

class rsyncCheck:
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