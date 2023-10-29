from django.urls import path

from . import views

urlpatterns = [
    # https://localhos:8000/profiles/
    path('', views.profiles, name='profiles'),

    # https://localhos:8000/profiles/profiles/1/
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),

    # https://localhos:8000/profiles/account/
    path('account/', views.account, name='account'),

    # http://localhost:8000/profiles/account-edit/
    path('account-edit/', views.profile_edit, name='profile_edit'),

    # http://localhost:8000/profiles/create-skill/
    path('create-skill/', views.create_skill, name='create_skill'),

    # http://localhost:8000/profiles/edit-skill/1/
    path('edit-skill/<int:pk>/', views.edit_skill, name='edit_skill'),

    # http://localhost:8000/profiles/delete-skill/2/
    path('delete-skill/<int:pk>/', views.delete_skill, name='delete_skill'),

    # http://localhost:8000/profiles/inbox/
    path('inbox/', views.inbox, name='inbox'),

    # http://localhost:8000/profiles/send-message/2/
    path('send-message/<int:pk>/', views.send_message, name='send_message'),

    # http://localhost:8000/profiles/message/2/
    path('message/<int:pk>/', views.message_detail, name='message_detail'),

    # http://localhost:8000/profiles/signup/
    path('signup/', views.signup, name='signup'),

    # http://localhost:8000/profiles/signin/
    path('signin/', views.signin, name='signin'),

    # http://localhost:8000/profiles/signout/
    path('signout/', views.signout, name='signout')
]
