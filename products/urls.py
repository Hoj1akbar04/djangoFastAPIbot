from django.urls import path
from . import views
from .views import ShopPageView, ContactPageView, CartView, CheckoutView, ProductDetail, ProductUpdateView, DeleteProductView, AboutView, BlogView, ServicesView, ThankyouView, UserProfileView

urlpatterns = [
    path('shop/', ShopPageView.as_view(), name='shop'),
    path('shop/detail/<slug:slug>', ProductDetail.as_view(), name='detail'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('thankyou/', ThankyouView.as_view(), name='thankyou'),
    path('cart/', CartView.as_view(), name='cart'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    # path('shop/detail/<int:id>', ProductDetail.as_view(), name='detail'),
    path('update/<slug:slug>', ProductUpdateView.as_view(), name='product-update'),
    path('delete/<slug:slug>', DeleteProductView.as_view(), name='product-delete')
]