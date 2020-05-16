from django.urls import path
from pets.views import PageListView, PageDetailView, PageCreateView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('create/', PageCreateView.as_view(), name='wiki-new-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]