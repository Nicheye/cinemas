

from django.urls import path
from .views import *
urlpatterns = [
	path('main',Main_View.as_view()),
	path('main/<int:id>',Main_View.as_view()),
	path('search',Search_View.as_view()),
    
]
