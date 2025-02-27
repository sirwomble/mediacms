import debug_toolbar
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(title="MediaCMS API", default_version='v1', contact=openapi.Contact(url="https://mediacms.io"), x_logo={"url": "../../static/images/logo_dark.svg"}),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    url(r"^__debug__/", include(debug_toolbar.urls)),
    url(r"^", include("files.urls")),
    url(r"^", include("users.urls")),
    url(r"^accounts/", include("allauth.urls")),
    url(r"^api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/api/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
