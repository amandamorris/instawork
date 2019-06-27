from django.urls import path

from . import views

app_name = 'teams'
urlpatterns = [
    # ex: /teams/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /teams/add/
    path('add/', views.AddView.as_view(), name='add'),
    # ex: /teams/5/edit/
    path('<int:pk>/edit/', views.UpdateView.as_view(), name='edit'),

    path('<int:member_id>/save/', views.save, name='save'),
    # path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),

]
