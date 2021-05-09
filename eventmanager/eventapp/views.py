from django.shortcuts import render, redirect
from django.contrib import messages
from .models import participant, program, Contact

# Create your views here.
def guest(request):


    prog1 = program.objects.filter(day="Day 1")
    prog2 = program.objects.filter(day="Day 2")
    prog3 = program.objects.filter(day="Day 3")
    prog4 = program.objects.filter(day="Day 4")


    if request.method == "POST":

        if("register" in request.POST):

            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            topic = request.POST['topic']
            description = request.POST['description']

            participa = participant(name=name,email=email,address=address,topic=topic,description=description)
            participa.save()

            print("inserted......")
            messages.success(request, "You have successfully been registered!!!")
            return redirect('/')

    context = {
        "prog1":prog1,"prog2":prog2,"prog3":prog3,"prog4":prog4
    }

    return render(request,"index.html",context)

def contact(request):
    if request.method == "POST":

        if("contact" in request.POST):

            namee = request.POST['name']
            emaile = request.POST['email']
            messagee = request.POST['message']
            
            contac = Contact(Name=namee,email=emaile,message=messagee)
            contac.save()

            print("Contact inserted......")
            messages.success(request, "Your message was sent successfully")
            return render(request,'index.html')

    return render(request,"contact.html")
