from app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('question/<int:question_id>', views.question, name='question'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('ask/', views.ask, name='ask'),
    path('setting/', views.setting, name='setting'),
    path('admin/', admin.site.urls),
    path('tag/<tag_name>/', views.tag, name='search_by_tag')
]