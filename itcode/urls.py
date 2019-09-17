from django.contrib import admin
from django.urls import path, include
from users import views as userView
from django.contrib.auth import views as AuthViews
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', userView.register, name = 'reg'),
    path('profile/', userView.profile, name='profile'),
    path('user/', AuthViews.LoginView.as_view(template_name = 'users/user.html'), name = 'user'),
    path('exit/', AuthViews.LogoutView.as_view(template_name = 'users/exit.html'), name = 'exit'),
    path('blog/', include('blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)