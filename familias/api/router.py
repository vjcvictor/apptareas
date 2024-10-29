from rest_framework.routers import DefaultRouter
from familias.api.views import FamiliaApiViewset

router_familias = DefaultRouter()
router_familias.register(prefix='familias', basename='familias', viewset=FamiliaApiViewset)