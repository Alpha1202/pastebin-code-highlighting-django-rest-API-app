from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from snippets import views

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# snippet_detail = SnippetViewSet.as_view({
#     'get':'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# user_list = UserViewSet.as_view({
#     'get': 'list'
# })

# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = [
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('users/', user_list, name='user-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('users/<int:pk>', user_detail, name='user-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight')
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)