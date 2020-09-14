from django.urls import path
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views

# from .views import polls_list, polls_detail

# schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("loginn/", views.obtain_auth_token, name="login"),
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote", CreateVote.as_view(), name="create_vote"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
    path("user/", UserCreate.as_view(), name="user_create"),
    path('docs/', include_docs_urls(title='Polls API')),
   
]

urlpatterns += router.urls