from django.contrib import admin
from django.urls import include, path
from idx.views import home
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns =[
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(    
    path('', include('idx.urls')),
)