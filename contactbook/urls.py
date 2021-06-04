from django.urls import path
from .views import ContactListView, ContactDetailView, PersonListView, PersonDetailView, ListAddressesView


urlpatterns = [
    path('api/contacts', ContactListView.as_view(), name='contact_list'),
    path('api/contacts/<int:id>', ContactDetailView.as_view(), name='contact_detail'),
    path('api/addresses', ListAddressesView.as_view(), name='list_addresses')
]