from django.urls import re_path, path
from rest_framework import routers
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="接口文档",
        default_version='v1',
        license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'login/', Login.as_view()),
    re_path(r'signup/', Signup.as_view()),
    path('info/', userInfo.as_view({'get': 'list', 'post': 'create'})),
    re_path(r'^info/(?P<pk>\d+)/', userInfo.as_view({'get': 'retrieve', 'put': 'update'})),
    path('topic/', userTopic.as_view({'get': 'list','post': 'create'})),
    re_path(r'^topic/(?P<pk>\d+)/', userTopic.as_view({'get': 'retrieve', 'put': 'update'})),
    path('reply/', useReply.as_view({'get': 'list', 'post': 'create'})),
    re_path(r'reply/(?P<pk>\d+)/', useReply.as_view({'get': 'retrieve', 'put': 'update'})),
    path('remind/', useRemind.as_view({'get': 'list', 'post': 'create'})),
    re_path(r'msgs/(?P<pk>\d+)/', getMsgsFromUser.as_view({'get': 'retrieve', })),
    path('focususer/', useFocusFromUser.as_view({'get': 'list', 'post': 'create'})),
    re_path(r'collect/', collectReply.as_view({'post': 'create'})),
    re_path(r'c1/', createCategory1.as_view({'get': 'list', 'post': 'create'})),
    re_path(r'c2/', createCategory2.as_view({'get': 'list', 'post': 'create'})),
    re_path(r'userremind/', getRemindFromUser.as_view({'get': 'list', })),
    re_path(r'category/', getCategory.as_view({'get': 'list', })),
    re_path(r'categorytopic/', getTopicFromCategory.as_view({'get': 'list', })),
    # re_path(r'topicc/', createTopic.as_view()),
    re_path(r'focusc/', createFocusFromTopic.as_view({'post': 'create'})),
    re_path(r'reportc/', createReportFromMsg.as_view({'post': 'create'})),
    re_path(r'attitude/', createAttitudeFromMsg.as_view({'post': 'create'})),
    re_path(r'msgreply/', getReplyFromMsg.as_view({'get': 'list', })),
    re_path(r'reportdeal/', dealReport.as_view({'post': 'create'})),
    re_path(r'super/', Super.as_view({'post': 'create'}))
]

router = routers.DefaultRouter()
# router.register('infou', updateUserInfo)
# router.register('topicu', updateTopic)
# router.register('replyu', updateReply)
# urlpatterns += router.urls
