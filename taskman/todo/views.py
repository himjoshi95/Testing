from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .forms import TodoForm,UserRegisterForm,UserLoginForm
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    todo_list = Todo.objects.all().filter(status=False).order_by('-id')                  # to access Todo create object todo_list

    form = TodoForm()                               # to access Todoform class > create object of form
    context = {'form':form,'todo_list':todo_list}                         # dictionary created  a context dictionary to pass in html page
    return render(request,'todo/index.html',context)

def addtodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(task = request.POST['task'],deadline= request.POST['deadline'])
        new_todo.save()
    return redirect('index')

def deletetask(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)                   #filter that person
    todo.status = True
    todo.save()
    return redirect('index')

def completetask(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)                     #filter that person
    todo.complete = True
    todo.save()
    return redirect('index')

def updatetask(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)                           # filter that person
    context = {'todo': todo}                                      # get value by making dictionary
    return render(request, 'todo/update.html',context)

def edittask(request,todo_id):
    todo = Todo.objects.get(pk=todo_id) 
    task = request.POST['tname']                                       #capture values in post
    deadline = request.POST['dname']
    print(task,"asfdasf")
    print(deadline,"asfasfasf")
    #if request.method == 'POST':
        #form = TodoForm(request.POST)
        #if form.is_valid():
        #    new_todo = Todo(task = request.POST['task'],deadline= request.POST['deadline'])
            #new_todo.save()

                                           # capture
    return render(request,'todo/index.html')

def reg(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
          #new_todo = User(username = request.POST['username'],email= request.POST['email'],password1= request.POST['password1'],password2= request.POST['password2'])
          #new_todo.save()
          form.save()


    form =UserRegisterForm()
    context = {'form':form}
    return render(request,'todo/register.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        password = request.POST['psw']
        print(password)
        
        user = User.objects.filter(email=email)
        print(user) 

        print(user.password1)

        #if user.password1 == password:
            #print("User exists")
     

    form = UserLoginForm()
    context = {'form':form}

    
    
    return render(request,'todo/login.html',context)



    
