from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('organization', views.OrganizationList.as_view(), name='organization'),
    path('organization/<int:pk>', views.OrganizationDetail.as_view(), name='organization_detail'),
]
