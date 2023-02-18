from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()

router.register(r'result', views.ResultViewSet, 'Result')
router.register(r'event', views.EventViewSet, 'Event')
router.register(r'eventcategory', views.EventCategoryViewSet, 'EventCategory')

urlpatterns = router.urls
