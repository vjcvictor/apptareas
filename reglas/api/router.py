from rest_framework.routers import DefaultRouter
from reglas.api.views import ReglaApiViewset

router_reglas = DefaultRouter()
router_reglas.register(prefix='reglas', basename='reglas', viewset=ReglaApiViewset)