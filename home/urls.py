
from django.contrib import admin
from django.urls import path, include
from home import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('home.urls'))
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
   path('', views.home, name='home'),
   path('orderMeals', views.orderMeals, name='orderMeals'),
   path('buyGrocerries', views.buyGrocerries, name='buyGrocerries'),
   path('orderMeals/search/', views.search, name='search'),
  

   
]

