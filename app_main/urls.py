from django.urls import path

from . import views


urlpatterns = [
    # http://localhost:8000/
    path('', views.projects, name='projects'),  

    # http://localhost:8000/project/1/
    path('project/<int:pk>/', views.project_detail, name='project_detail'),

    # http://localhost:8000/project/create/
    path('project/create/', views.create_project, name='create_project'),

    # http://localhost:8000/project/edit/4/
    path('project/edit/<int:pk>/', views.edit_project, name='edit_project'),
]
