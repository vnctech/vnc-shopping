from django.urls import path
from . import views

app_name = 'product_management'

urlpatterns = [
    
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category-list/<int:cat_id>/', views.category_list, name='category_list'),
    path('sub-category-list/<int:subcat_id>/', views.sub_category_list, name='sub_category_list'),


    ]

