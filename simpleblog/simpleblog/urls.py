from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('jet/', include('jet.urls', 'jet')),
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

]

admin.site.index_title = "Social Book"
admin.site.site_header = "Admin"
admin.site.site_title = "Admin Page"