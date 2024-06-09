import email

# from turtle import color, title
import uuid
from django.shortcuts import redirect, render
from django.http import JsonResponse
from LILTHRIFTYSTORES.mixins import AjaxFormMixin
from customer.models import CartOrder, CartOrderItems, Manager

#from customer.models import CartOrder

from plugmanager.models import Category,Brand,ProductAttribute,Product, Size
from django.db.models import Max,Min,Count,Avg
from django.db.models.functions import ExtractMonth
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.shortcuts import render

from accounts.forms import AuthForm, ManagerUserForm, CustomerUserForm, Profileupdateform
from LILTHRIFTYSTORES.mixins import AjaxFormMixin, FormErrors, reCAPTCHAValidation
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
def  is_ajax(request):
	return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'







# Create your views here.

def lilthrifty_index(request,):
	data=ProductAttribute.objects.filter(is_featured=True).order_by('-id')
	category=Category.objects.all().order_by('id')
	brand=Brand.objects.all().order_by('-id')
	product=Product.objects.all().order_by('-id')
	producted=ProductAttribute.getproduct(product)
	datas=Category.objects.get(id=2)
	dataz=ProductAttribute.getCategories(category)
	datamen=Category.objects.get(id=1)
	category_all=Category.objects.all().order_by('id')
	category_update=ProductAttribute.get_categories(category_all)
	all_datazmen=ProductAttribute.getallCategories(category)
	datazmen=ProductAttribute.getmenCategories(category)
	alldatazmen=ProductAttribute.getallCategories(category)
	brands=ProductAttribute.getallbrands(brand)
	order=CartOrder.objects.all().order_by('-id')

	return render(request, "index.html",{'alldatazmen':alldatazmen,'datamen':datamen,'order':order,'data':data,'datas':datas,'dataz':dataz,'brands':brands,'producted':producted,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen})
    #'datas':datas,'datamen':datamen









def lilthrifty_allcategory_branch(request,category_id,product_id):
	category=Category.objects.all().order_by('-id')
	dataz=ProductAttribute.getCategories(category)
	datas=Category.objects.get(id=2)
	datamen=Category.objects.get(id=1)
	category_all=Category.objects.all().order_by('id')
	category_update=ProductAttribute.get_categories(category_all)
	all_datazmen=ProductAttribute.getallCategories(category)
	datazmen=ProductAttribute.getmenCategories(category)[:3]
	brand=Brand.objects.all().order_by('-id')
	products=Product.objects.all().order_by('-id')
	brands=ProductAttribute.getallbrands(brand)
	producted=ProductAttribute.getproduct(products)
	product=Product.objects.get(id=product_id)
	datazing=ProductAttribute.get_list__Categories(product)
	categorys=Category.objects.get(id=category_id)
	datazings=ProductAttribute.get_all_branch_listCategories(categorys)
	data=ProductAttribute.objects.filter(product=product.id).order_by('-id')
	# data=ProductAttribute.get_all__branch_Categories(product)

	return render(request,'allcategory_branch.html',{
	'data':data,'dataz':dataz,'datas':datas,'brands':brands,'producted':producted,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen,'datazing':datazing,'datazings':datazings,'product':product,'categorys':categorys
			})
	







 # Category
def lilthrifty_category_list(request):
	datas=Category.objects.get(id=1)
	data=Category.objects.get(id=2)
	
	return render(request,'category-list.html',{'data':data,'datas':datas})





# category product List According to Category female
def lilthrifty_category_product_list(request):
	categorys=Category.objects.all().order_by('-id')
	category=Category.objects.get(id=2)
	male=Category.objects.get(id=1)
	dataz=ProductAttribute.getCategories(category)
	data=ProductAttribute.getMaleCategories(category)	
	catmale=ProductAttribute.getMaleCategories(male)
	datas=Category.objects.get(id=2)
	datamen=Category.objects.get(id=1)
	category_all=Category.objects.all().order_by('id')
	category_update=ProductAttribute.get_categories(category_all)
	all_datazmen=ProductAttribute.getallCategories(categorys)
	datazmen=ProductAttribute.getmenCategories(category)
	brand=Brand.objects.all().order_by('-id')
	products=Product.objects.all().order_by('-id')
	brands=ProductAttribute.getallbrands(brand)
	producted=ProductAttribute.getproduct(products)

	return render(request,'category_product_list.html',{
			'data':data,
			'catmale':catmale,
			'dataz':dataz,
			'datas':datas,
			'producted':producted,
			'brands':brands,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen

			})






# female
def lilthrifty_product_available_lists(request,product_id):
	datas=Category.objects.get(id=2)
	category=Category.objects.all().order_by('-id')
	datass=ProductAttribute.getMaleCategories(category)	
	product=Product.objects.get(id=product_id)
	data=ProductAttribute.objects.filter(product=product.id).order_by('-id')
	datazing=ProductAttribute.getMalelistCategories(product)
	brand=Brand.objects.all().order_by('-id')
	products=Product.objects.all().order_by('-id')
	brands=ProductAttribute.getallbrands(brand)
	producted=ProductAttribute.getproduct(products)
	dataz=ProductAttribute.getCategories(category)
	datamen=Category.objects.get(id=1)
	category_all=Category.objects.all().order_by('id')
	category_update=ProductAttribute.get_categories(category_all)
	all_datazmen=ProductAttribute.getallCategories(category)
	datazmen=ProductAttribute.getmenCategories(category)

	return render(request,'product_available_lists.html',{
			'data':data,'datas':datas,'datass':datass,
			'dataz':dataz,'brands':brands,'producted':producted,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen,'datazing':datazing
			})





#male product list
def lilthrifty_category_product_list_male(request):
	category=Category.objects.all().order_by('-id')
	datamen=Category.objects.get(id=1)
	category_all=Category.objects.all().order_by('id')
	category_update=ProductAttribute.get_categories(category_all)
	all_datazmen=ProductAttribute.getallCategories(category)
	datazmen=ProductAttribute.getmenCategories(category)
	datasmen=ProductAttribute.getMen(category)
	brand=Brand.objects.all().order_by('-id')
	product=Product.objects.all().order_by('-id')
	brands=ProductAttribute.getallbrands(brand)
	producted=ProductAttribute.getproduct(product)
	datas=Category.objects.get(id=2)
	dataz=ProductAttribute.getCategories(category)
	

	return render(request,'category_product_list_male.html',{
			'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen,'datasmen':datasmen,'brands':brands,'producted':producted,'dataz':dataz,'datas':datas,
			
			})





#male
def lilthrifty_product_available_lists_male(request,product_id):
	category=Category.objects.all().order_by('-id')
	dataz=ProductAttribute.getCategories(category)
	datas=Category.objects.get(id=2)
	datamen=Category.objects.get(id=1)
	category_all=Category.objects.all().order_by('id')
	category_update=ProductAttribute.get_categories(category_all)
	all_datazmen=ProductAttribute.getallCategories(category)
	# datazmen=ProductAttribute.getmenCategories(category)[:3]
	datazmen=ProductAttribute.getmenCategories(category)
	brand=Brand.objects.all().order_by('-id')
	products=Product.objects.all().order_by('-id')
	brands=ProductAttribute.getallbrands(brand)
	producted=ProductAttribute.getproduct(products)
	product=Product.objects.get(id=product_id)
	datazing=ProductAttribute.getMalelistCategories(product)
	
	data=ProductAttribute.objects.filter(product=product.id).order_by('-id')
	return render(request,'product_available_lists_male.html',{
	'data':data,'dataz':dataz,'datas':datas,'brands':brands,'producted':producted,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen,'datazing':datazing
			})











# Add to cart
def lilthrifty_add_to_cart(request):
	# del request.session['cartdata']
	cart_p={}
	cart_p[str(request.GET['id'])]={
		'image':request.GET['image'],
		'title':request.GET['title'],
		'qty':request.GET['qty'],
		'price':request.GET['price'],
		'size':request.GET['size'],
		'color':request.GET['color'],
		'manager':request.GET['manager']


	}
	if 'cartdata' in request.session:
		if str(request.GET['id']) in request.session['cartdata']:
			cart_data=request.session['cartdata']
			cart_data[str(request.GET['id'])]['qty']=int(cart_p[str(request.GET['id'])]['qty'])
			cart_data.update(cart_data)
			request.session['cartdata']=cart_data
		else:
			cart_data=request.session['cartdata']
			cart_data.update(cart_p)
			request.session['cartdata']=cart_data
	else:
		request.session['cartdata']=cart_p
	return JsonResponse({'data':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})





# Cart List Page
#@login_required
def lilthrifty_cart_list(request):
	products=Product.objects.all().order_by('-id')
	brand=Brand.objects.all().order_by('-id')
	brands=ProductAttribute.getallbrands(brand)
	producted=ProductAttribute.getproduct(products)
	category=Category.objects.all().order_by('-id')
	datas=Category.objects.get(id=2)
	dataz=ProductAttribute.getCategories(category)
	datamen=Category.objects.get(id=1)
	category_all=Category.objects.all().order_by('id')
	category_update=ProductAttribute.get_categories(category_all)
	all_datazmen=ProductAttribute.getallCategories(category)
	datazmen=ProductAttribute.getmenCategories(category)
	total_amt=0
	sum_total_amt=0
	if 'cartdata' in request.session:
		for p_id,item in request.session['cartdata'].items():
			total_amt+=int(item['qty'])*float(item['price'])
			sum_total_amt=total_amt+int(100)
		return render(request, 'cart.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,'sum_total_amt':sum_total_amt,'datas':datas,'brands':brands,'producted':producted,'dataz':dataz,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen})
	else:
		return render(request, 'cart.html',{'cart_data':'','totalitems':0,'total_amt':total_amt,'sum_total_amt':sum_total_amt,'datas':datas,'brands':brands,'producted':producted,'dataz':dataz,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen})

# Delete Cart Item
def lilthrifty_delete_cart_item(request):
	p_id=str(request.GET['id'])
	if 'cartdata' in request.session:
		if p_id in request.session['cartdata']:
			cart_data=request.session['cartdata']
			del request.session['cartdata'][p_id]
			request.session['cartdata']=cart_data
	total_amt=0
	for p_id,item in request.session['cartdata'].items():
		total_amt+=int(item['qty'])*float(item['price'])
	t=render_to_string('ajax/cart-list.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
	return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})











