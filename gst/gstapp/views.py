from django.http import HttpResponse


def index(request):
	return HttpResponse("Hello, world. You're at the gstapp index.")

def businesses(request):
	return HttpResponse("You're looking at businesses page")

def products(request):
	return HttpResponse("You're looking at products page")

def b2b_txn(request):
	return HttpResponse("You're looking at b2b_txn page")

def b2c_txn(request):
	return HttpResponse("You're looking at b2c_txn page")