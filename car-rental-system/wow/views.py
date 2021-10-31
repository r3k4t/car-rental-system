from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.



def index(request):
    return render(request, 'index.html')
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']

    #     user = auth.authenticate(username = username, password =password  )
    #     print(user, 'outside')

    #     if user is not None:
    #         print('AM HERE')
    #         auth.login(request , user)
    #         return redirect('/employeeportal')    
    #     else:
    #         print('inside else')
    #         messages.info(request, 'invalid username or password')
    #         return redirect("/")
    # else:
    #     print('hi')
    #     return render(request,'index.html')


# def register(request):

#     if request.method == 'POST':

#         email = request.POST['email']
#         username = request.POST['username']
#         password= request.POST['password']


#         user = User.objects.create_user(username = username , password = password , email = email)
#         user.save()
#         print('user created')
#         return redirect('/customer_login')

#     return render(request,'register.html')


# def customer_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username = username, password =password  )

#         if user is not None:
#             auth.login(request , user)
#             return redirect('/employeeportal')    
#         else:
#             messages.info(request, 'invalid username or password')
#             return redirect("/customer_login")
#     else:
#         return render(request,'customer_login.html')


# def employeeportal(request):
#     return render(request, 'employeeportal.html')

# def employeecustomerview(request):
#     return render(request, 'employeecustomerview.html')

# def employeeaddvehicle(request):
#     return render(request, 'employeeaddvehicle.html')


# def employeeaddlocation(request):
#     return render(request, 'employeeaddlocation.html')








