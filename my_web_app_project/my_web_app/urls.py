from django.urls import path
from . import views
app_name = 'my_web_app'

urlpatterns =[
    path('',views.index,name='index'),
    path('detail/<int:id>/',views.detail,name='detail'),

]