from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from Tagent.views import CustomerViewSet
router = routers.DefaultRouter()
router.register(r'customer',CustomerViewSet)
urlpatterns = [
    url(r'^',include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    ]

