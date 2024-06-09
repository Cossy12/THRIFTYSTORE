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






 # Category
def lilthrifty_allcategory(request,category_id):
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
	brands=ProductAttribute.getallbrands(brand)
	order=CartOrder.objects.all().order_by('-id')
	categorys=Category.objects.get(id=category_id)
	alldatazmen=ProductAttribute.get_allCategories(categorys)
	alldatazmens=ProductAttribute.objects.filter(category=categorys).order_by('-id')
	datazmen=ProductAttribute.getmenCategories(category)
	
	return render(request, "allcategorys.html",{'categorys':categorys,'alldatazmens':alldatazmens,'alldatazmen':alldatazmen,'order':order,'data':data,'dataz':dataz,'datas':datas,'category':category,'brands':brands,'producted':producted,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen})

	



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






# Brand
def lilthrifty_brand_list(request):
    datass=ProductAttribute.objects.all().order_by('-id')
    brand=Brand.objects.all().order_by('-id')
    product=Product.objects.all().order_by('-id')
    brands=ProductAttribute.getallbrands(brand)
    producted=ProductAttribute.getproduct(product)
    category=Category.objects.all().order_by('-id')
    datas=Category.objects.get(id=2)
    dataz=ProductAttribute.getCategories(category)
    datamen=Category.objects.get(id=1)
    category_all=Category.objects.all().order_by('id')
    category_update=ProductAttribute.get_categories(category_all)
    all_datazmen=ProductAttribute.getallCategories(category)
    datazmen=ProductAttribute.getmenCategories(category)

    return render(request,'brand-list.html',{'brands':brands,'datas':datas,'brands':brands,'producted':producted,'datass':datass,'dataz':dataz,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen})







# Product List
def lilthrifty_product_list(request):
	total_data=ProductAttribute.objects.count()
	#data=ProductAttribute.objects.all().order_by('-id')[:3]

	data=ProductAttribute.objects.all().order_by('-id')
	min_price=ProductAttribute.objects.aggregate(Min('price'))
	max_price=ProductAttribute.objects.aggregate(Max('price'))
	return render(request,'product_list.html',
		{
			'data':data,
			'total_data':total_data,
			'min_price':min_price,
			'max_price':max_price,
		}
		)





# Product List According to Brand
def lilthrifty_brand_product_list(request,brand_id):
	brand=Brand.objects.get(id=brand_id)
	data=ProductAttribute.objects.filter(brand=brand).order_by('-id')
	branded=Brand.objects.all().order_by('-id')
	product=Product.objects.all().order_by('-id')
	brands=ProductAttribute.getallbrands(branded)
	producted=ProductAttribute.getproduct(product)
	category=Category.objects.get(id=2)
	datas=Category.objects.get(id=2)
	dataz=ProductAttribute.getCategories(category)
	datamen=Category.objects.get(id=1)
	category_all=Category.objects.all().order_by('id')
	category_update=ProductAttribute.get_categories(category_all)
	all_datazmen=ProductAttribute.getallCategories(category_all)
	datazmen=ProductAttribute.getmenCategories(category)
	branding=ProductAttribute.getbrand(brand)
	return render(request,'brand_product_list.html',{
			'data':data,'brands':brands,'producted':producted,'dataz':dataz,'datas':datas,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen,'branding':branding,'branched':brand
			})






# Product Detail
def lilthrifty_product_detail(request,id):
    products=ProductAttribute.objects.get(id=id)
    category=Category.objects.all().order_by('-id')

    datamen=Category.objects.get(id=1)
    category_all=Category.objects.all().order_by('id')
    category_update=ProductAttribute.get_categories(category_all)
    all_datazmen=ProductAttribute.getallCategories(category)
    datazmen=ProductAttribute.getmenCategories(category)
    brand=Brand.objects.all().order_by('-id')
    brands=ProductAttribute.getallbrands(brand)
    product=Product.objects.all().order_by('-id')
    producted=ProductAttribute.getproduct(product)
    datas=Category.objects.get(id=2)
    dataz=ProductAttribute.getCategories(category)  
    related_products=ProductAttribute.objects.filter(product=products.product).exclude(id=id)[:4]
    colors=ProductAttribute.objects.filter(title=products.title).values('color__id','color__title','color__color_code').distinct()
    sizes=ProductAttribute.objects.filter(title=products.title).values('size__id','size__title','price','color__id').distinct()
    prices=ProductAttribute.objects.filter(title=products.title).values('size__id','size__title','price','color__id').distinct()
	



    return render(request, 'product_detail.html',{'data':products,'colors':colors,'sizes':sizes,'related':related_products,'prices':prices,
													'dataz':dataz,'datas':datas,'brands':brands,'producted':producted,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen})





# product_available
def lilthrifty_product_available(request):
	product=Product.objects.all().order_by('-id')
	data=ProductAttribute.getproduct(product)
	datass=ProductAttribute.objects.all().order_by('-id')
	brand=Brand.objects.all().order_by('-id')
	brands=ProductAttribute.getallbrands(brand)
	producted=ProductAttribute.getproduct(product)
	category=Category.objects.all().order_by('-id')
	datas=Category.objects.get(id=2)
	dataz=ProductAttribute.getCategories(category)
	datamen=Category.objects.get(id=1)
	category_all=Category.objects.all().order_by('id')
	category_update=ProductAttribute.get_categories(category_all)
	all_datazmen=ProductAttribute.getallCategories(category)
	datazmen=ProductAttribute.getmenCategories(category)


	return render(request,'product_available.html',{'data':data,'datas':datas,'brands':brands,'producted':producted,'datass':datass,'dataz':dataz,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen})





#product_available_list
def lilthrifty_product_available_list(request,product_id):
	product=Product.objects.get(id=product_id)
	products=Product.objects.all().order_by('-id')
	data=ProductAttribute.objects.filter(product=product).order_by('-id')
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
	datazing=ProductAttribute.getgoods(product)
	# send_filter_product_id(request,product_id)

	return render(request,'product_available_list.html',{
			'data':data,'brands':brands,'producted':producted,'product':product,
			'dataz':dataz,'datas':datas,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen,'datazing':datazing
			})
					#def lilthrifty_product_available_lists(request):
						#product=Product.objects.get(id=5)
						#data=ProductAttribute.objects.filter(product=product).order_by('-id')

						#return render(request,'product_available_lists.html',{
							#	'data':data,
							#	})


def lilthrifty_send_filter_product_id(request,product_id):
	product=product_id
	
	return render(request,'sidebarfilter_branch_allcategory.html',{'filters_producted':product})







# Filter Data
def lilthrifty_filter_data(request):
    
	colors=request.GET.getlist('color[]')
	categories=request.GET.getlist('category[]')
	branded=request.GET.getlist('brand[]')
	products=request.GET.getlist('product[]')
	sizes=request.GET.getlist('size[]')
	minPrice=request.GET['minPrice']
	maxPrice=request.GET['maxPrice']
	product=Product.objects.all().order_by('-id')
	producted=ProductAttribute.objects.filter(product__in=product).distinct('product')
	allProducts=ProductAttribute.objects.all().order_by('-id').distinct('id')
	allProducts=allProducts.filter(price__gte=minPrice)
	allProducts=allProducts.filter(price__lte=maxPrice)
	if len(colors)>0:
		allProducts=allProducts.filter(color__id__in=colors).distinct()
	if len(categories)>0:
		allProducts=allProducts.filter(category__id__in=categories).distinct()
	if len(branded)>0:
		allProducts=allProducts.filter(brand__id__in=branded).distinct()
	if len(sizes)>0:
		allProducts=allProducts.filter(size__id__in=sizes).distinct()
	if len(products)>0:
		allProducts=allProducts.filter(product__id__in=products).distinct()
	testing=ProductAttribute.objects.filter(product__in=product).distinct('product')
	testing=testing.filter(price__gte=minPrice)
	testing=testing.filter(price__lte=maxPrice)
	if len(colors)>0:
		testing=testing.filter(color__id__in=colors).distinct('product')
	if len(categories)>0:
		testing=testing.filter(category__id__in=categories).distinct('product')
	if len(branded)>0:
		testing=testing.filter(brand__id__in=branded).distinct('product')
	if len(sizes)>0:
		testing=testing.filter(size__id__in=sizes).distinct('product')
	if len(products)>0:
		testing=testing.filter(product__id__in=products).distinct('product')
	t=render_to_string('ajax/product-list.html',{'data':allProducts,'datas':testing})
	return JsonResponse({'data':t})







# Filter Data
def lilthrifty_filter_data_sub_1(request):
    
	colors=request.GET.getlist('color[]')
	categories=request.GET.getlist('category[]')
	branded=request.GET.getlist('brand[]')
	products=request.GET.getlist('product[]')
	sizes=request.GET.getlist('size[]')
	minPrice=request.GET['minPrice']
	maxPrice=request.GET['maxPrice']
	product=Product.objects.all().order_by('-id')
	category=Category.objects.all().order_by('-id')
	producted=ProductAttribute.objects.filter(product__in=product).distinct('product')
	allProducts=ProductAttribute.get_Men(category)
	allProducts=allProducts.filter(price__gte=minPrice)
	allProducts=allProducts.filter(price__lte=maxPrice)
	if len(colors)>0:
		allProducts=allProducts.filter(color__id__in=colors).distinct()
	if len(categories)>0:
		allProducts=allProducts.filter(category__id__in=categories).distinct()
	if len(branded)>0:
		allProducts=allProducts.filter(brand__id__in=branded).distinct()
	if len(sizes)>0:
		allProducts=allProducts.filter(size__id__in=sizes).distinct()
	if len(products)>0:
		allProducts=allProducts.filter(product__id__in=products).distinct()
	testing=ProductAttribute.get_men_Categories(category)
	testing=testing.filter(price__gte=minPrice)
	testing=testing.filter(price__lte=maxPrice)
	if len(colors)>0:
		testing=testing.filter(color__id__in=colors).distinct('product')
	if len(categories)>0:
		testing=testing.filter(category__id__in=categories).distinct('product')
	if len(branded)>0:
		testing=testing.filter(brand__id__in=branded).distinct('product')
	if len(sizes)>0:
		testing=testing.filter(size__id__in=sizes).distinct('product')
	if len(products)>0:
		testing=testing.filter(product__id__in=products).distinct('product')
	t=render_to_string('ajax/category_product_list_male_ajax.html',{'data':allProducts,'datas':testing})
	return JsonResponse({'data':t})





# Filter Data
def lilthrifty_filter_data_brand(request):
    
	colors=request.GET.getlist('color[]')
	categories=request.GET.getlist('category[]')
	branded=request.GET.getlist('brand[]')
	products=request.GET.getlist('product[]')
	sizes=request.GET.getlist('size[]')
	minPrice=request.GET['minPrice']
	maxPrice=request.GET['maxPrice']
	brand=Brand.objects.all().order_by('-id')
	allProducts=ProductAttribute.objects.all().order_by('-id').distinct('id')
	allProducts=allProducts.filter(price__gte=minPrice)
	allProducts=allProducts.filter(price__lte=maxPrice)
	if len(colors)>0:
		allProducts=allProducts.filter(color__id__in=colors).distinct()
	if len(categories)>0:
		allProducts=allProducts.filter(category__id__in=categories).distinct()
	if len(branded)>0:
		allProducts=allProducts.filter(brand__id__in=branded).distinct()
	if len(sizes)>0:
		allProducts=allProducts.filter(size__id__in=sizes).distinct()
	if len(products)>0:
		allProducts=allProducts.filter(product__id__in=products).distinct()
	testing=ProductAttribute.objects.filter(brand__in=brand).distinct('brand')
	testing=testing.filter(price__gte=minPrice)
	testing=testing.filter(price__lte=maxPrice)
	if len(colors)>0:
		testing=testing.filter(color__id__in=colors).distinct('brand')
	if len(categories)>0:
		testing=testing.filter(category__id__in=categories).distinct('brand')
	if len(branded)>0:
		testing=testing.filter(brand__id__in=branded).distinct('brand')
	if len(sizes)>0:
		testing=testing.filter(size__id__in=sizes).distinct('brand')
	if len(products)>0:
		testing=testing.filter(product__id__in=products).distinct('brand')
	t=render_to_string('ajax/brand-list_ajax.html',{'data':allProducts,'datas':testing})
	return JsonResponse({'data':t})



# Filter Data
def lilthrifty_filter_data_sub_2(request):
    
	colors=request.GET.getlist('color[]')
	categories=request.GET.getlist('category[]')
	branded=request.GET.getlist('brand[]')
	products=request.GET.getlist('product[]')
	sizes=request.GET.getlist('size[]')
	minPrice=request.GET['minPrice']
	maxPrice=request.GET['maxPrice']
	product=Product.objects.all().order_by('-id')
	category=Category.objects.all().order_by('-id')	
	producted=ProductAttribute.objects.filter(product__in=product).distinct('product')
	allProducts=ProductAttribute.get_MaleCategories(category)
	allProducts=allProducts.filter(price__gte=minPrice)
	allProducts=allProducts.filter(price__lte=maxPrice)
	if len(colors)>0:
		allProducts=allProducts.filter(color__id__in=colors).distinct()
	if len(categories)>0:
		allProducts=allProducts.filter(category__id__in=categories).distinct()
	if len(branded)>0:
		allProducts=allProducts.filter(brand__id__in=branded).distinct()
	if len(sizes)>0:
		allProducts=allProducts.filter(size__id__in=sizes).distinct()
	if len(products)>0:
		allProducts=allProducts.filter(product__id__in=products).distinct()
	testing=ProductAttribute.get_Categories(category)
	testing=testing.filter(price__gte=minPrice)
	testing=testing.filter(price__lte=maxPrice)
	if len(colors)>0:
		testing=testing.filter(color__id__in=colors).distinct('product')
	if len(categories)>0:
		testing=testing.filter(category__id__in=categories).distinct('product')
	if len(branded)>0:
		testing=testing.filter(brand__id__in=branded).distinct('product')
	if len(sizes)>0:
		testing=testing.filter(size__id__in=sizes).distinct('product')
	if len(products)>0:
		testing=testing.filter(product__id__in=products).distinct('product')
	t=render_to_string('ajax/category_product_list_ajax.html',{'data':allProducts,'datas':testing})
	return JsonResponse({'data':t})




# Filter Data
def lilthrifty_filter_data_branch_sub1(request):
    
	colors=request.GET.getlist('color[]')
	categories=request.GET.getlist('category[]')
	branded=request.GET.getlist('brand[]')
	products=request.GET.getlist('product[]')
	sizes=request.GET.getlist('size[]')
	minPrice=request.GET['minPrice']
	maxPrice=request.GET['maxPrice']
	product_category_id=request.GET['offset']
	product_id_id=request.GET['total']
	product=Product.objects.all().order_by('-id')
	producted=ProductAttribute.objects.filter(product__in=product).distinct('product')
	allProducts=ProductAttribute.get_list__ajax_Categories(product_id_id)
	allProducts=allProducts.filter(price__gte=minPrice)
	allProducts=allProducts.filter(price__lte=maxPrice)
	if len(colors)>0:
		allProducts=allProducts.filter(color__id__in=colors).distinct('product')
	if len(categories)>0:
		allProducts=allProducts.filter(category__id__in=categories).distinct('product')
	if len(branded)>0:
		allProducts=allProducts.filter(brand__id__in=branded).distinct('product')
	if len(sizes)>0:
		allProducts=allProducts.filter(size__id__in=sizes).distinct('product')
	if len(products)>0:
		allProducts=allProducts.filter(product__id__in=products).distinct('product')
	testing=ProductAttribute.get_all_branch_ajax_listCategories(product_category_id)
	testing=testing.filter(price__gte=minPrice)
	testing=testing.filter(price__lte=maxPrice)
	if len(colors)>0:
		testing=testing.filter(color__id__in=colors).distinct('product')
	if len(categories)>0:
		testing=testing.filter(category__id__in=categories).distinct('product')
	if len(branded)>0:
		testing=testing.filter(brand__id__in=branded).distinct('product')
	if len(sizes)>0:
		testing=testing.filter(size__id__in=sizes).distinct('product')
	if len(products)>0:
		testing=testing.filter(product__id__in=products).distinct('product')
	
	all_products=ProductAttribute.get_list__ajax_Categories_extra(product_id_id)
	all_products=all_products.filter(price__gte=minPrice)
	all_products=all_products.filter(price__lte=maxPrice)
	if len(colors)>0:
		all_products=all_products.filter(color__id__in=colors).distinct('id')
	if len(categories)>0:
		all_products=all_products.filter(category__id__in=categories).distinct('id')
	if len(branded)>0:
		all_products=all_products.filter(brand__id__in=branded).distinct('id')
	if len(sizes)>0:
		all_products=all_products.filter(size__id__in=sizes).distinct('id')
	if len(products)>0:
		all_products=all_products.filter(product__id__in=products).distinct('id')
	
	
	t=render_to_string('ajax/allcategory_branch_ajax.html',{'product_category_id':product_category_id,'product_id_id':product_id_id,'data':allProducts,'datas':testing,'datass':all_products,'product_category_id':product_category_id,'product_id_id':product_id_id})
	return JsonResponse({'data':t})





def lilthrifty_filter_data_allcategory(request):
    
	colors=request.GET.getlist('color[]')
	categories=request.GET.getlist('category[]')
	branded=request.GET.getlist('brand[]')
	products=request.GET.getlist('product[]')
	sizes=request.GET.getlist('size[]')
	minPrice=request.GET['minPrice']
	maxPrice=request.GET['maxPrice']
	product_category_id=request.GET['offset']
	product=Product.objects.all().order_by('-id')
	# producted=ProductAttribute.objects.filter(product__in=product).distinct('product')
	allProducts=ProductAttribute.get_ajax_allCategories(product_category_id)
	allProducts=allProducts.filter(price__gte=minPrice)
	allProducts=allProducts.filter(price__lte=maxPrice)
	if len(colors)>0:
		allProducts=allProducts.filter(color__id__in=colors).distinct('product')
	if len(categories)>0:
		allProducts=allProducts.filter(category__id__in=categories).distinct('product')
	if len(branded)>0:
		allProducts=allProducts.filter(brand__id__in=branded).distinct('product')
	if len(sizes)>0:
		allProducts=allProducts.filter(size__id__in=sizes).distinct('product')
	if len(products)>0:
		allProducts=allProducts.filter(product__id__in=products).distinct('product')
	testing=ProductAttribute.objects.filter(category=product_category_id).order_by('-id')
	testing=testing.filter(price__gte=minPrice)
	testing=testing.filter(price__lte=maxPrice)
	if len(colors)>0:
		testing=testing.filter(color__id__in=colors).distinct()
	if len(categories)>0:
		testing=testing.filter(category__id__in=categories).distinct()
	if len(branded)>0:
		testing=testing.filter(brand__id__in=branded).distinct()
	if len(sizes)>0:
		testing=testing.filter(size__id__in=sizes).distinct()
	if len(products)>0:
		testing=testing.filter(product__id__in=products).distinct()
	

	
	t=render_to_string('ajax/allcategory_ajax.html',{'data':allProducts,'datas':testing,'product_category_id':product_category_id})
	return JsonResponse({'data':t})




# Filter Data
def lilthrifty_filter_data_branch_product(request):
    
	colors=request.GET.getlist('color[]')
	categories=request.GET.getlist('category[]')
	branded=request.GET.getlist('brand[]')
	products=request.GET.getlist('product[]')
	sizes=request.GET.getlist('size[]')
	minPrice=request.GET['minPrice']	
	maxPrice=request.GET['maxPrice']
	product_category_id=request.GET['offset']
	product=Product.objects.all().order_by('-id')
	producted=ProductAttribute.objects.filter(product__in=product).distinct('product')
	allProducts=ProductAttribute.objects.filter(product=product_category_id).distinct('id')
	allProducts=allProducts.filter(price__gte=minPrice)
	allProducts=allProducts.filter(price__lte=maxPrice)
	if len(colors)>0:
		allProducts=allProducts.filter(color__id__in=colors).distinct('id')
	if len(categories)>0:
		allProducts=allProducts.filter(category__id__in=categories).distinct('id')
	if len(branded)>0:
		allProducts=allProducts.filter(brand__id__in=branded).distinct('id')
	if len(sizes)>0:
		allProducts=allProducts.filter(size__id__in=sizes).distinct('id')
	if len(products)>0:
		allProducts=allProducts.filter(product__id__in=products).distinct('id')

	testing=ProductAttribute.objects.filter(product=product_category_id).distinct('product')
	testing=testing.filter(price__gte=minPrice)
	testing=testing.filter(price__lte=maxPrice)
	if len(colors)>0:
		testing=testing.filter(color__id__in=colors).distinct('product')
	if len(categories)>0:
		testing=testing.filter(category__id__in=categories).distinct('product')
	if len(branded)>0:
		testing=testing.filter(brand__id__in=branded).distinct('product')
	if len(sizes)>0:
		testing=testing.filter(size__id__in=sizes).distinct('product')
	if len(products)>0:
		testing=testing.filter(product__id__in=products).distinct('product')


	# all_products=ProductAttribute.objects.filter(product__in=product_id_id).order_by('-id')
	# all_products=all_products.filter(price__gte=minPrice)
	# all_products=all_products.filter(price__lte=maxPrice)
	# if len(colors)>0:
	# 	all_products=all_products.filter(color__id__in=colors).distinct()
	# if len(categories)>0:
	# 	all_products=all_products.filter(category__id__in=categories).distinct()
	# if len(branded)>0:
	# 	all_products=all_products.filter(brand__id__in=branded).distinct()
	# if len(sizes)>0:
	# 	all_products=all_products.filter(size__id__in=sizes).distinct()
	# if len(products)>0:
	# 	all_products=all_products.filter(product__id__in=products).distinct()
	

	t=render_to_string('ajax/allcategory_branch_product_ajax.html',{'data':allProducts,'datas':testing,'product_category_id':product_category_id})
	return JsonResponse({'data':t})

 



	# Filter Data
def lilthrifty_filter_data_branch_brand(request):
    
	colors=request.GET.getlist('color[]')
	categories=request.GET.getlist('category[]')
	branded=request.GET.getlist('brand[]')
	products=request.GET.getlist('product[]')
	sizes=request.GET.getlist('size[]')
	minPrice=request.GET['minPrice']
	maxPrice=request.GET['maxPrice']
	product_brand_id=request.GET['offset']
	product=Product.objects.all().order_by('-id')
	producted=ProductAttribute.objects.filter(product__in=product).distinct('product')
	allProducts=ProductAttribute.objects.filter(brand=product_brand_id).distinct('id')
	allProducts=allProducts.filter(price__gte=minPrice)
	allProducts=allProducts.filter(price__lte=maxPrice)
	if len(colors)>0:
		allProducts=allProducts.filter(color__id__in=colors).distinct('id')
	if len(categories)>0:
		allProducts=allProducts.filter(category__id__in=categories).distinct('id')
	if len(branded)>0:
		allProducts=allProducts.filter(brand__id__in=branded).distinct('id')
	if len(sizes)>0:
		allProducts=allProducts.filter(size__id__in=sizes).distinct('id')
	if len(products)>0:
		allProducts=allProducts.filter(product__id__in=products).distinct('id')

	testing=ProductAttribute.objects.filter(brand=product_brand_id).distinct('brand')
	testing=testing.filter(price__gte=minPrice)
	testing=testing.filter(price__lte=maxPrice)
	if len(colors)>0:
		testing=testing.filter(color__id__in=colors).distinct('brand')
	if len(categories)>0:
		testing=testing.filter(category__id__in=categories).distinct('brand')
	if len(branded)>0:
		testing=testing.filter(brand__id__in=branded).distinct('brand')
	if len(sizes)>0:
		testing=testing.filter(size__id__in=sizes).distinct('brand')
	if len(products)>0:
		testing=testing.filter(product__id__in=products).distinct('brand')
	# testing=ProductAttribute.get_ajax_brand(product_brand_id)
	# testing=testing.filter(price__gte=minPrice)
	# testing=testing.filter(price__lte=maxPrice)
	# if len(colors)>0:
	# 	testing=testing.filter(color__id__in=colors).distinct()
	# if len(categories)>0:
	# 	testing=testing.filter(category__id__in=categories).distinct()
	# if len(branded)>0:
	# 	testing=testing.filter(brand__id__in=branded).distinct()
	# if len(sizes)>0:
	# 	testing=testing.filter(size__id__in=sizes).distinct()
	# if len(products)>0:
	# 	testing=testing.filter(product__id__in=products).distinct()
	
	# all_products=ProductAttribute.objects.filter(product__in=product_id_id).order_by('-id')
	# all_products=all_products.filter(price__gte=minPrice)
	# all_products=all_products.filter(price__lte=maxPrice)
	# if len(colors)>0:
	# 	all_products=all_products.filter(color__id__in=colors).distinct()
	# if len(categories)>0:
	# 	all_products=all_products.filter(category__id__in=categories).distinct()
	# if len(branded)>0:
	# 	all_products=all_products.filter(brand__id__in=branded).distinct()
	# if len(sizes)>0:
	# 	all_products=all_products.filter(size__id__in=sizes).distinct()
	# if len(products)>0:
	# 	all_products=all_products.filter(product__id__in=products).distinct()
	
	
	t=render_to_string('ajax/filter_data_branch_ajax_brand.html',{'data':allProducts,'datas':testing})
	return JsonResponse({'data':t})




# Load More
# def lilthrifty_load_more_data(request):
# 	offset=int(request.GET['offset'])
# 	limit=int(request.GET['limit'])
# 	data=ProductAttribute.objects.all().order_by('-id')[offset:offset+limit]
# 	t=render_to_string('ajax/product-list.html',{'data':data})
# 	return JsonResponse({'data':t}
# )


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

#update Cart Item
def lilthrifty_update_cart_item(request):
	p_id=str(request.GET['id'])
	p_qty=request.GET['qty']
	if 'cartdata' in request.session:
		if p_id in request.session['cartdata']:
			cart_data=request.session['cartdata']
			cart_data[str(request.GET['id'])]['qty']=p_qty
			request.session['cartdata']=cart_data
	total_amt=0
	for p_id,item in request.session['cartdata'].items():
		total_amt+=int(item['qty'])*float(item['price'])
	t=render_to_string('ajax/cart-list.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt})
	return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})








@login_required
def lilthrifty_secure_checkout(request):
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
			Thriftup=Manager.objects.create(
					manager=item['manager'],
							)			
			order=CartOrder.objects.create(
					customer=request.user,
					total_amt=sum_total_amt,
					manager=Thriftup
			)
		total_amt=0
		sum_total_amt=0
		for p_id,item in request.session['cartdata'].items():
			total_amt+=int(item['qty'])*float(item['price'])
			sum_total_amt=total_amt+int(100)
			items=CartOrderItems.objects.create(
				customer=request.user,
				manager=item['manager'],
				order=order,
				invoice_no='INV-'+str(order.id),
				item=item['title'],
				image=item['image'],
				qty=item['qty'],
				price=item['price'],
				color=item['color'],
				size=item['size'],
				G_amount=total_amt,
				total_GSamt=sum_total_amt,
				)
		return render(request, 'cart-checkout.html',{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,'sum_total_amt':sum_total_amt,'datas':datas,'brands':brands,'producted':producted,'dataz':dataz,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen})
	else:
		return render(request, 'cart-checkout.html',{'datas':datas,'brands':brands,'producted':producted,'dataz':dataz,'datamen':datamen,'datazmen':datazmen,'All_category':category_update,'all_datazmen':all_datazmen})


 





