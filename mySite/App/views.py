from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html')

def basicInfo(request):
	return render(request, 'basic_info.html')
