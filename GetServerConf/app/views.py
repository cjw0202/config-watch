from django.shortcuts import render
from pullconfig import rsyncGet
from .models import Configfile

# Create your views here.

def index(request):
	configs = Configfile.objects.all()
	context = {
		'configs': configs
	}
	return render(request, 'app/index.html', context=context)

def detail(request, pk):
	res = Configfile.objects.get(pk=pk)
	name = res.name
	ip = res.server_ip
	server_module = res.model_name
	config = res.config
	dstdir = '/lingtian/test_code/data/tempfile'
	rsy = rsyncGet(dstdir, config, name)
	resconfig = rsy.doCmd('rsync', ip, server_module)
	resconfig = rsy.readConfig(resconfig)

	context = {
		'name': name,
		'file_content': resconfig,
		'configfile_name': config,
		'remark': ''
	}
	return render(request, 'app/detail.html', context=context)
