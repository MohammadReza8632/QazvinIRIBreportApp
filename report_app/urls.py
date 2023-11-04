from django.urls import path
from .views import home, create_activity, detail_activity, delete_activity, edit_activity, export, detail_activity_download, PasswordsChangeView, password_success
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path("", home, name="home"),
    path("create_activity/", create_activity, name="create_activity"),
    # path("change_password/", auth_views.PasswordChangeView.as_view(template_name='change_password.html')),
    path('change_password/', login_required(PasswordsChangeView.as_view()), name="change_password"),
    path('password_success', password_success, name="password_success"),
    path("detail_activity/<int:id>", detail_activity, name="detail_activity"),
    path('<int:id>/delete-activity', delete_activity, name='delete_activity'),
    path('detail_activity/<int:id>/edit-activity', edit_activity, name='edit_activity'),
    path('detail_activity/<int:id>/detail_activity_download', detail_activity_download, name='detail_activity_download'),
    path("export", export, name="export"),

]
