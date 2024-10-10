from django.shortcuts import render,redirect
from .models import User

# Create your views here.

def home(request):
    data = User.objects.all()
    return render(request, 'userapp/home.html', {'data': data})

# def addUser(request):
#     if request.method =="POST":
#         print("Added")
#     # #user Input se data catch kiya 
#     user_name=request.POST.get("user_name")
#     user_email=request.POST.get("user_email")
#     user_number=request.POST.get("user_number")
#     user_description=request.POST.get("user_description")

#     # # create and object for Model class
#     # #Humne Store name ke variable m saara data fetch karke store kara liya
#     store = User(
#     name=user_name,
#     email=user_email,
#     number=user_number,
#     description=user_description,
#     )
    
#     store.save()
#     return redirect("/userapp/home/")

    


#     return render(request,'userapp/adduser.html')

def addUser(request):
    if request.method == "POST":
        # Get data from the form
        user_name = request.POST.get("user_name")
        user_email = request.POST.get("user_email")
        user_number = request.POST.get("user_number")
        user_description = request.POST.get("user_description")

        # Create an object for the User model
        store = User(
            name=user_name,
            email=user_email,
            number=user_number,
            description=user_description
        )
        
        # Save the object to the database
        store.save()
        
        # Redirect to the home page
        return redirect("/userapp/home/")

    # Handle GET request by rendering the form
    return render(request, 'userapp/adduser.html')







def deleteUser(request,demo_id):
    rem = User.objects.get(pk=demo_id)
    rem.delete()
    return redirect("/userapp/home/" )


def updateUser(request,id):
    upd =User.objects.get(pk=id)
    return render(request, "userapp/update.html",{'upd':upd})


def do_updateUser(request,id):
    user_name = request.POST.get("user_name")
    user_email = request.POST.get("user_email")
    user_number = request.POST.get("user_number")
    user_description = request.POST.get("user_description")
    
    upd=User.objects.get(pk=id)
    upd.name=user_name
    upd.email=user_email
    upd.number=user_number
    upd.description=user_description

    upd.save()
    return redirect("/userapp/home/" )



     