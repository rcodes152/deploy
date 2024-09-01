from django.shortcuts import render, HttpResponse ,redirect
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        # Create a Contact instance and save it to the database
        contact = Contact(name=name, email=email, message=message, date=datetime.today())
        contact.save()

        # Redirect to the thank you page
        return redirect('thank_you')
    else:
        return render(request, 'contact.html')

def lipsticks(request):
    return HttpResponse("This is the lipsticks page.")

def ingredients(request):
    return HttpResponse("This is the ingredients page.")

def brands(request):
    return HttpResponse("This is the brands page.")

def thank_you(request):
    return render(request, 'thank_you.html')
