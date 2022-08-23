from rest_framework.routers import DefaultRouter
from .views import TodoViewset

router = DefaultRouter()
router.register('todo', TodoViewset,basename="todo")
urlpatterns = router.urls