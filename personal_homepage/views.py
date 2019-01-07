from django.shortcuts import render
from display.models import Display


def home(request):
	# display = Display.description #模型的描述信息传递给变量
	display = Display.objects #将整个models传递过去
	return render(request, "home.html", {'display':display})