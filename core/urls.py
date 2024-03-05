from django.contrib import admin
from django.urls import path

admin.site.site_title = "TicketsPlus site admin"
admin.site.site_header = "TicketsPlus administration"
admin.site.index_title = "Site administration"
# https://github.com/django/django/blob/main/django/contrib/admin/sites.py

urlpatterns = [
    path("secretadmin/", admin.site.urls),
]
