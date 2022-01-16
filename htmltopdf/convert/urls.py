from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('pdf_view/', views.ViewPdf.as_view(), name='pdf_view'),
    path('pdf_download/', views.DownloadPdf.as_view(), name='pdf_download'),

]