from django.urls import  path
# traemos views que vienen de contrib.auth LoginView, LogoutView
# from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [ #indicamos el metodo que usaremos
   path('post_list/',views.post_list, name='post_list' ),
    # path('home/', views.home, name='home'),
    #  path('panchito/', views.panchito, name='panchito'),
    #  path('home/', views.welcome, name='home'),
#      path('users/', views.home, name='users'),
#      path('clients/', views.view_clients, name='clients'),
#      path('formulario_profesor/', views.crear_profesor, name='formulario_profesor'),
#     #  path('register_user/', views.register_user, name='register_user'),
# #path(punto de acceso, vista que se crea y renderiza en views,)
#      path('register_user/', views.register_user, name='register_user'),
#      path('formulario/', views.formulario, name='formulario'),
#      path('mostrar_escuela/', views.mostrar_escuela, name='mostrar_escuela'),
# # comentamos esto por que haremos otras formas login y logout
#     #  path('login/', views.login, name='login'),
#     #  path('logout/', views.logout, name='logout'),
#      path('login/', LoginView.as_view(template_name='aplicacion/login.html'), name='login'),
#      path('logout/', LogoutView.as_view(template_name='aplicacion/logout.html'), name='logout'),
    #  al colocar esto fuimos a setting a colocar una variable LOGIN_REDIRECT_URL='home'
]