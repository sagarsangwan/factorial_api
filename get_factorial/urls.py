from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('factorial/<int:num>', views.factorial, name='factorial'),
]

