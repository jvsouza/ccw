from .common import *
import debug_toolbar


urlpatterns = [
    path( 'admin/',     admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
