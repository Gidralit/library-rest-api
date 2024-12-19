from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>', views.AuthorDetail.as_view()),
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>', views.BookDetail.as_view()),
]