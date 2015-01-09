from django.shortcuts import render

from .forms import EmailForm
# Create your views here.
def home(request):
	form = EmailForm(request.POST)
	context = {"form": form}
	template = 'home.html'
	return render(request, template, context)