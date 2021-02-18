from django.urls import path
from .import views
from .views import LinkDeleteView , update_links
app_name='urls'

urlpatterns=[
	path('',views.home,name='home'),
	path('update/',views.update_links,name='update_links'),
	path('delete/<pk>/',LinkDeleteView.as_view(),name='deleteview'),

]