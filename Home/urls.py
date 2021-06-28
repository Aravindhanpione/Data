from django.urls import path, re_path
from . import views

urlpatterns =[
    path('', views.index_view, name='index'),
    path('Services/<str:name>', views.services, name = 'Services'),
    path('faq', views.faq, name='faq'),
    path('donate-for-cause', views.dfc, name = "donate-for-cause"),
    path('puja-online', views.PujaOnline, name = 'puja-online'),
    path('terms-and-conditions', views.TandC, name = 'terms-and-conditions'),
    path('privacy-policy', views.Privacy, name='privacy-policy')
]