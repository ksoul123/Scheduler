from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('schedule/<int:schedule_id>', views.detail, name = 'detail'),
    path('schedule/new/', views.new_schedule, name = 'new'),
    path('schedule/<int:schedule_id>/edit',views.edit_schedule, name = 'edit'),
    path('schedule/<int:schedule_id>/delete',views.delete_schedule, name = 'delete'),
]