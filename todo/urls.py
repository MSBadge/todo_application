from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('add/', views.add_task, name='add_task'),
    path('details/<int:item_id>', views.details, name='details'),
    path('delete/<int:item_id>', views.delete_task, name='delete_task'),
    path('complite/<int:item_id>', views.complite_task, name='complite_task'),
]