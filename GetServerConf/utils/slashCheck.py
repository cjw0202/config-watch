# 
# @Author: chengjiawei
# @Date: 2020-04-08 18:08:52
# @Last Modified by: chengjiawei
# @Last Modified time: 2020-04-08 18:08:52
# # #

class slashCheck:
	'''
	返回带 / 的路径
	'''
	def checkDirSlash(dir):
	if dir.endswith('/'):
		return dir
	else:
		return dir+'/'