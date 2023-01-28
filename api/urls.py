from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import PostList, PostDetail
#urlpatterns44 = [
 #    path("posts/", PostList.as_view(), name="api_post_list"),
  #   path("posts/<int:p k>", PostDetail.as_view(), name="api_post_detail"),
#]
#urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
   path("auth/", include("rest_framework.urls")),
   path("token-auth/", views.obtain_auth_token)
]
