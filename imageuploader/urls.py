from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from myapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('image/<int:image_id>/delete/', views.delete_image, name='delete_image'),
    path('api/', include('api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
