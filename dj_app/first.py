from django.http import HttpResponse
from django.shortcuts import render
def wel(request):
	return render(request,'temp.html')
def sec(request):
	mess =request.GET['message']
	msg  =mess.split()
	return render(request,'count.html',{'msg':mess,"length":len(msg)})	