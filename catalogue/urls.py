from django.urls import path

from catalogue.views import Products, ProductCreate, ProductDelete, PurchaseCreate, PurchaseError, PurchaseList, \
    ReturnCreate

urlpatterns = [
    path('', Products.as_view(), name="list"),
    path('product/create/', ProductCreate.as_view(), name="product_create"),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name="product_delete"),
    path('product/bay/<int:pk>/', PurchaseCreate.as_view(), name='purchase_create'),
    path('purchase/error/', PurchaseError.as_view(), name='purchase_error'),
    path('purchase/list/', PurchaseList.as_view(), name='purchase_list'),
    path('return/create/', ReturnCreate.as_view(), name='return_create')
]
