from django.db import models
from django.utils import timezone

# Create your models here.


class Configfile(models.Model):
	name = models.CharField(verbose_name='项目名', max_length=128)
	config = models.CharField(verbose_name='配置文件', max_length=128)
	content = models.TextField(verbose_name='配置内容', blank=True)
	remark = models.CharField(verbose_name='备注', max_length=256, blank=True)
	model_name = models.CharField(verbose_name='rsync模块名', max_length=128, null=True)
	server_ip = models.GenericIPAddressField(verbose_name='服务IP', protocol='IPV4', null=True)
	update_time = models.DateTimeField('更新时间')
	create_time = models.DateTimeField('添加时间', auto_now_add=True)
	
	def save(self, *args, **kwargs):
		self.update_time = timezone.now()
		super().save(*args, **kwargs)
			

	class Meta:
		verbose_name = '配置信息'
		verbose_name_plural = '配置信息'

	
