from django.urls import path
from .views import ArticleAPIView, ArticleDetails, GenericAPIView
from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter
from .views import article_list,article_detail

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')


urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),

 
]


# from django.urls import path
# from .views import article_list,article_detail

# urlpatterns = [

#     path('article/', article_list),
#     path('detail/<int:pk>/', article_detail),
#     path('article/', ArticleAPIView.as_view()),
#     path('detail/<int:id>/', ArticleDetails.as_view()),
#     path('generic/article/<int:id>/', GenericAPIView.as_view()),

# ]