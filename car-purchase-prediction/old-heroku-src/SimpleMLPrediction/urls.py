from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('carBuyDecision.urls')),
    path('admin/', admin.site.urls),
    path('carBuyDecision/', include("carBuyDecision.urls"), name="index"),
]
