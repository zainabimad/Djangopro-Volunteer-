from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Images import views
urlpatterns=[
    path('upload/',views.files,name="upload"),
    path('studio/', views.studio, name="studio"),
    path('studio/<int:id>', views.details, name='Details'),

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,image_root=settings.MEDIA_ROOT)


