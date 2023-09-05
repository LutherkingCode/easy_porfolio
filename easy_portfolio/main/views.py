from django.shortcuts import render,redirect
from django.http import HttpResponseForbidden
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.contrib.auth.models import User
from .forms import ProjectForm

from django.shortcuts import render
from .models import Project  # Import your Project model

def home(request):
    users = User.objects.order_by('-date_joined')
    return render(request, 'home.html', {'users': users})




# This view handles the subscription process of  a new user
# it ensure that  new users credentials are encrypted before storing to the database for future usages
def create_account(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        return redirect('open_session')
    else :
        return render(request,'create_account.html') 


def open_session(request) :
    if request.method== 'POST':
       username=request.POST['username']
       password=request.POST['password']
       user=authenticate(request,username=username,password=password)
       if user is not None :
           login(request,user)
           next_url = request.session.get('next')
           if next_url is not None :
              return HttpResponseRedirect(next_url)
           else :
               return redirect('home')
          
       else:
           invalid_credentials = "Invalid username or password."
           return render(request, 'login.html', {'invalid_credentials':invalid_credentials})
           
    else :
       return render(request,'login.html')



#Close the user session
def close_session(request):
    logout(request)
    return redirect("home")


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User  # Import the User model
from .models import Project

def user_details(request, user_id):
    if request.user.is_authenticated:
        # Retrieve the user based on the user_id or return a 404 page if the user doesn't exist
        user = get_object_or_404(User, pk=user_id)

        # Retrieve all projects associated with the user
        projects = Project.objects.filter(user=user)

        return render(request, 'user_details.html', {'user': user, 'projects': projects})
    else:
        return redirect('open_session')  # Redirect to the login view if the user is not authenticated


def create_project(request):
    form = ProjectForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = request.user  
                project.save()
                return redirect('home')  
        else:
            return render(request, 'create_project.html', {'form': form})
    else:
        return redirect('open_session')  


        
       
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

   
    return render(request, 'project_details.html', {'project': project})


def delete_project(request, project_id):
    
    project = get_object_or_404(Project, pk=project_id)

    
    if request.user == project.user:
        
        project.delete()
        return redirect('home')  