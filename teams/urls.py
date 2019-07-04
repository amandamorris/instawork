from django.urls import path

from . import views

app_name = 'teams'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),

    path('add/', views.AddView.as_view(), name='add'),

    path('<int:pk>/edit/', views.UpdateView.as_view(), name='edit'),

    path('<int:member_id>/save/', views.save, name='save'),

    path('<int:member_id>/delete/', views.delete, name='delete'),

]
