from django.urls import path, include
from rest_framework import routers

from partners.views import PartnerViewSet, PartnerContactPersonViewSet

app_name = 'projects'

# partners_router = routers.DefaultRouter()
router = routers.DefaultRouter()
router.register('', PartnerViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),

]