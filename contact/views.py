from django.shortcuts import render
from . models import Contact
# Create your views here.
def contact(request):

    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,age=age,gender=gender,email=email,message=message)
        contact.save()
    
        return render(request,'contact/index.html')
    
    return render(request,'contact/index.html')
