
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index
from photoalbum import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name="main"),
    path('front/', views.react, name="front"),
    path('blog/', views.blog_view, name='blog'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user-page"),
    path('viewer/', views.viewPage, name="viewer"),
    path('catalog/', views.catalog_view, name='catalog'),
    path('create-post/', views.create_post_view, name='create-post'),
    path('createprem-post/', views.create_prem_view, name="createprem-post"),
    path('createfull-post/', views.create_full_view, name="createfull-post"),
    path('contact/', views.contact_view, name="contact"),
    path('contactadd/', views.AddContact.as_view(), name="add_contact"),
    path('createvip-post/', views.create_vip_view, name="createvip-post"),
    path('detail<int:id>/', views.detail_view, name='detail'),
    path('premdetail<int:id>/', views.premdetail_view, name="premdet"),
    path('vipdetail<int:id>/', views.vipdetail_view, name="vipdetail"),
    path('fulldetail<int:id>/', views.fulldetail_view, name="fulldetail"),
    path('api/', include('photoalbum.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
