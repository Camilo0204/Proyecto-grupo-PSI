from django.urls import path
from . import views
# asigna las abreviaturas para llamar las views creadas
urlpatterns =[
    path('hello/',views.hello),
    path('about/', views.about)
    
]