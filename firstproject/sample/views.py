from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# without using templates

# def home(request):   
#     return HttpResponse("hello world")

def login(request):
    return HttpResponse("I am login page")  # we can pass only one argument,

def palindrome(request):
    s=request.GET.get('name')
    if s!=None:
        if s==s[::-1]:
            return HttpResponse("<h1 style=color:red;background-color:black;text-align:center;>PALINDROME</h1>")
        else:
            return HttpResponse("<h1 style=color:green;background-color:orange;> not a palindrome</h1>")
    else:
        return HttpResponse("check the variable") 

def displayTwoVariable(request):
    a=request.GET.get("empname")            
    b=request.GET.get("age")
    return HttpResponse(f'Employee name:{a}<br>Age:{b}')  #[In searchengine=> '?'=>it used to separate urls and variable, '&&'=>it used to add more than one variable



#With Templates
def home(request):
    return render(request,'home.html')

def login(request):
    name=request.GET.get('name')
    password=request.GET.get('password')
    confirm_pas=request.GET.get('confirm_password')
    return render(request,'login.html',{'u_n':name,'p':password,'c_p':confirm_pas})

def signup(request):
    return render(request,'signup.html')

def display(request):
    name=request.GET.get('name')
    password=request.GET.get('password')
    confirm_pas=request.GET.get('confirm_password')
    return render(request,'display.html',{'u_n':name,'p':password,'c_p':confirm_pas})


# JINJA TAGS:
#  -This are the independent tags which are not belongs to either python or html
#  -Jinja tags help has to write python code inside the html file
#  Syntax:
#     1.{{ }}->VARIABLE
#         -it is used to represent the given characters are variable
#     2.{% %}->CONDITIONAL AND LOOPING