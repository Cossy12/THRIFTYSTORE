from django.shortcuts import render

from LILTHRIFTYSTORES.mixins import AjaxFormMixin
from accounts.forms import AuthForm, ManagerUserForm, CustomerUserForm, Profileupdateform
from django.conf import settings
from LILTHRIFTYSTORES.mixins import AjaxFormMixin, FormErrors, reCAPTCHAValidation
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from customer.models import CartOrder, CartOrderItems

from plugmanager.models import Brand, Category, Product, ProductAttribute
from .models import User






def  is_ajax(request):
	return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Create your views here.






def sign_out(request):
	'''
	Basic view for user sign out
	'''
	logout(request)
	return redirect(reverse('index'))




#@login_required
#def get_user_profile(request):

#	update = User.objects.get(username=request.user.username)

#	if request.method == 'POST':
#		form = Profileupdateform(request.POST,request.FILES,instance=update)
#
#		if form.is_valid():
#				form.save()
#				return redirect("accounts:profile") 
#	else:
#		form = Profileupdateform(instance=update)
#		return render(request, 'profile.html', {'form': form})






def get_user_profile(request):

	managerorders=CartOrderItems.objects.filter(manager=request.user.username).order_by('-id')
	order=CartOrder.objects.filter(customer=request.user).order_by('id')
	ordered=CartOrderItems.getorderlist(order)
	orders=CartOrderItems.getorderlisted(order)

	#orders=CartOrderItems.objects.filter(customer=request.user).order_by('-id')



	return render(request, "profile.html",{'orders':orders,'ordered':ordered,'managerorders':managerorders})
#@login_required
def edit_profile(request):

	update = User.objects.get(username=request.user.username)

	if request.method == 'POST':
		form = Profileupdateform(request.POST,request.FILES,instance=update)

		if form.is_valid():
			form.save()
			return redirect("accounts:profile") 
	else:
		form = Profileupdateform(instance=update)

		return render(request, 'edit_profile.html', {'form': form})

def edit_profile(request):
    update = User.objects.get(username=request.user.username)

    if request.method == 'POST':
        form =  Profileupdateform(request.POST,request.FILES,instance=update)
        if form.is_valid():
            try:
                form.save()
                return redirect("accounts:profile")
            except:
                # If the form is invalid, 
                pass
        # This part is missing:
        # Here you need an else for when the form is invalid.
        else:
            return render(request,'edit_profile.html',{'form' : form})
    else:
        form = Profileupdateform(instance=update)
        return render(request,'edit_profile.html',{'form' : form})

