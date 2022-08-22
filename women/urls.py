from django.urls import path, include
from .views import *
from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):
    routers = [
        routers.Route(url=r'^{prefix}$',
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'}),
    ]


# router = MyCustomRouter()
router = routers.SimpleRouter()
router.register(r'women', WomenViewSet, basename='women')
print(router.urls)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # path('api/v1/womenapi/', WomenAPIListCreate.as_view()),
    # path('api/v1/womenapi/<int:pk>/', WomenAPIRetrieveUpdateDestroy.as_view()),
    # path('api/v1/womenapi2/', WomenAPIView2.as_view()),
    # path('api/v1/womenapi2/<int:pk>/', WomenAPIView2.as_view()),
]
