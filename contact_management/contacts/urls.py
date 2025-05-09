from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('add/', views.add_contact, name='add_contact'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('', views.landing_page, name='landing_page'),  # Landing page
    path('contacts/', views.contact_list, name='contact_list'),  # Contact list
    # Other routes
]
 
