from django.shortcuts import render
from .forms import UserForm
from django.urls import reverse_lazy
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

def index(request):
    return render(request,'basic_app/index.html')

@login_required
def special(request):
    
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    
    logout(request)
    
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False
    

    if request.method == 'POST':

        
        user_form = UserForm(data=request.POST)

        
        if user_form.is_valid():

            
            user = user_form.save()

           
            user.set_password(user.password)

            
            user.save()


            
            registered = True

        else:
           
            print(user_form.errors)

    else:
        
        user_form = UserForm()


    return render(request,'basic_app/registration.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        
        if user:
            
            if user.is_active:
               
                login(request,user)
                
                return HttpResponseRedirect(reverse('index'))
            else:
                
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        
        return render(request, 'basic_app/login.html', {})


class YourEnvironmentListView(ListView):
    context_object_name = 'photographer'
    model = models.YourEnvironment


class YourEnvironmentDetailView(DetailView):
    context_object_name = 'photo_details'
    model = models.YourEnvironment
    template_name = 'basic_app/yourenvironment_detail.html'


class YourEnvironmentCreateView(LoginRequiredMixin,CreateView):
    fields = ('name',)
    model = models.YourEnvironment


class YourPicsCreateView(LoginRequiredMixin,CreateView):
    fields = ("pic_name","image","image_description","Category")
    model = models.YourPics
 

# class YourPicsUpdateView(UpdateView):
#     fields = ("pic_name","image","image_desc")
#     model = models.YourPics


# class YourEnvironmentDeleteView(DeleteView):
#     model = models.School
#     success_url = reverse_lazy("basic_app:list")

