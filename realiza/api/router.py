from rest_framework.routers import DefaultRouter
from realiza.api.views import RealizaApiViewset

router_realiza = DefaultRouter()
router_realiza.register(prefix='realiza', basename='realiza', viewset=RealizaApiViewset)