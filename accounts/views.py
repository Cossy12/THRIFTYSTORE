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

class CustomerSignUpView(AjaxFormMixin, FormView):
	'''
	Generic FormView with our mixin for user sign-up with reCAPTURE security
	'''

	template_name = "registration/customer_signup.html"
	form_class = CustomerUserForm
	success_url = "/"

	#reCAPTURE key required in context
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["recaptcha_site_key"] = settings.RECAPTCHA_PUBLIC_KEY
		return context

	#over write the mixin logic to get, check and save reCAPTURE score
	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)	
		if is_ajax(self.request):
			token = form.cleaned_data.get('token')
			captcha = reCAPTCHAValidation(token)
			if captcha["success"]:
				obj = form.save()
				obj.email = obj.username
				obj.save()
				up = obj.userprofile
				up.captcha_score = float(captcha["score"])
				up.save()
				
				login(self.request, obj, backend='django.contrib.auth.backends.ModelBackend')

				#change result & message on success
				result = "Success"
				# message = "Thank you for signing up"
				message = 'The app site is under update, please try again later", "sorry for the inconvinience'

				server_d = 'sorry'
				server_d_ms = 'The app site is under update, please try again later", "sorry for the inconvinience'
			
				
			data = {'result': result, 'message': message,'server_d':server_d,'server_d_ms':server_d_ms}
			return JsonResponse(data)

		return response


class ManagerSignUpView(AjaxFormMixin, FormView):
	'''
	Generic FormView with our mixin for user sign-up with reCAPTURE security
	'''

	template_name = "registration/plugmanager_signup.html"
	form_class = ManagerUserForm
	success_url = "/"

	#reCAPTURE key required in context
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["recaptcha_site_key"] = settings.RECAPTCHA_PUBLIC_KEY
		return context

	#over write the mixin logic to get, check and save reCAPTURE score
	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)	
		if is_ajax(self.request):
			token = form.cleaned_data.get('token')
			captcha = reCAPTCHAValidation(token)
			if captcha["success"]:
				obj = form.save()
				obj.email = obj.username
				obj.save()
				up = obj.userprofile
				up.captcha_score = float(captcha["score"])
				up.save()
				
				login(self.request, obj, backend='django.contrib.auth.backends.ModelBackend')

				#change result & message on success
				result = "Success"
				# message = "Thank you for signing up"
				message = 'The app site is under update, please try again later", "sorry for the inconvinience'

				server_d = 'sorry'
				server_d_ms = 'The app site is under update, please try again later", "sorry for the inconvinience'
			
				
			data = {'result': result, 'message': message,'server_d':server_d,'server_d_ms':server_d_ms}
			return JsonResponse(data)

		return response




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

