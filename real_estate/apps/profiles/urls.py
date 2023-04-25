from django.urls import path

from .views import (
    GetProfileAPIView,
    AgentListAPIView,
    TopAgentListAPIView,
    UpdateProfileAPIView
)


urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path("update/<str:username>/", UpdateProfileAPIView.as_view(), name="update_profile"),
    path("agents/", AgentListAPIView.as_view(), name="all_agents"),
    path("top_agents/", TopAgentListAPIView.as_view(), name="all_top_agents")

]