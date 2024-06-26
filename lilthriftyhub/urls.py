from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns=[
    path('',views.lilthrifty_index,name='index'),
    path('index',views.lilthrifty_index,name='index'),
    path('category-list',views.lilthrifty_category_list,name='category-list'),
    path('brand-list',views.lilthrifty_brand_list,name='brand-list'),
    path('category_product_list',views.lilthrifty_category_product_list,name='category_product_list'),
    path('category_product_list_male',views.lilthrifty_category_product_list_male,name='category_product_list_male'),
    path('product_list',views.lilthrifty_product_list,name='product_list'),
    path('product_available_list/<int:product_id>',views.lilthrifty_product_available_list,name='product_available_list'),
    path('allcategory/<int:category_id>',views.lilthrifty_allcategory,name='allcategory'),
    path('allcategory_branch/<int:category_id>/<int:product_id>',views.lilthrifty_allcategory_branch,name='allcategory_branch'),
    path('product_detail/<int:id>',views.lilthrifty_product_detail,name='product_detail'),
    path('product_available',views.lilthrifty_product_available,name='product_available'),
    path('cart',views.lilthrifty_cart_list,name='cart'),
    path('add-to-cart',views.lilthrifty_add_to_cart,name='add_to_cart'),
    path('brand-product-list/<int:brand_id>',views.lilthrifty_brand_product_list,name='brand_product_list'),
    path('delete-from-cart',views.lilthrifty_delete_cart_item,name='delete-from-cart'),
    path('update-cart',views.lilthrifty_update_cart_item,name='update-cart'),
    path('cart-checkout',views.lilthrifty_secure_checkout,name='cart-checkout'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]


