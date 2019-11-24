#from django.urls import path
#from . import views
#from .models import Counsellor
#app_name = "cons"
#urlpatterns = [
#    #path('admin/', ,
#    path('rest_api/', views.Cons.as_view({'get': 'list'})),
#    #path('rest_api/<pk>', views.Cons.as_view()),
#    path('rest_api/create',views.ConsCreateView.as_view({'get': 'retrieve'}))
#]

from rest_framework.routers import DefaultRouter
from .views import Cons

router = DefaultRouter()
router.register('rest_api', Cons, basename='user')
urlpatterns = router.urls