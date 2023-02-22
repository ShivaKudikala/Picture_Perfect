from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# SET THE NAMESPACE!
app_name = 'basic_app'


urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('',views.YourEnvironmentListView.as_view(),name='list'),
    path('<int:pk>/',views.YourEnvironmentDetailView.as_view(),name='detail'),
    path('create/',views.YourEnvironmentCreateView.as_view(),name='create'),
    path('createpic/',views.YourPicsCreateView.as_view(),name='createpic'),
    # path('update/<int:pk>/',views.YourPicsUpdateView.as_view(),name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
