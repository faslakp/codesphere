from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View

from store.forms import SignUpForm

class SignUpView(View) :
    template_name="register.html"

    form_class=SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=self.form_class(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            print("account created")

            return redirect("signup")
        else:

            print("failed to create account")

            return render(request,self.template_name,{"form":form_instance})
        


