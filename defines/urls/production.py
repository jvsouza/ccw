from .common import *


urlpatterns = [
    path("@dm1n/", admin.site.urls),
] + urlpatterns
