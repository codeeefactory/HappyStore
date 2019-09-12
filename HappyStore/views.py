from django.shortcuts import render
from HappyStore.models import POST
from django.shortcuts import redirect,HttpResponseRedirect
from . import Forms
def startpage(request):
	return render(request, "startpage.html")
def index(request):
	post=POST.objects.all()
	dic={"post":post}

	return render(request,"homepage.html",dic)

def contact(request):
	return render(request,"contact.html")

def about(request):
	return render(request,"about_site.html")
def Login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Forms.LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Forms.LoginForm()

    return render(request, 'Login.html', {'form': form})
# Create your views here.
