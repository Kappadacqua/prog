from django.urls import path
from django.contrib.auth import views as auth_views

from account.form import loginUtenteForm
from account.views import registrazione, user_edit, profilo

appname = "account"

urlpatterns = [
    path("registrazione/", registrazione, name="registrazione"),
    path("login/", auth_views.LoginView.as_view(template_name='account/login.html', form_class=loginUtenteForm),
         name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path("edit/", user_edit, name="edit"),
    path("profilo/", profilo, name="profilo"),
]

# erase_db()
# init_db()
