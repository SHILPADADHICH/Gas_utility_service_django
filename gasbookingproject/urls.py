from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

# Redirect homepage to service requests list
def home_redirect(request):
    return redirect('list_service_requests')  # Ensure this view name exists

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service-requests/', include('service_requests.urls')),  # Include your app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # 🔥 ADD THIS LINE

    # Optional: Define login/logout explicitly
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', home_redirect),  # Homepage redirect
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
