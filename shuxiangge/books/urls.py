from django.conf.urls import url, include
from rest_framework import routers
from .views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)

# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]