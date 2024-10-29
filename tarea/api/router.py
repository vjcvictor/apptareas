from rest_framework.routers import DefaultRouter
from tarea.api.views import TareaApiViewset

router_tareas = DefaultRouter()
router_tareas.register(prefix='tareas', basename='tareas', viewset=TareaApiViewset)