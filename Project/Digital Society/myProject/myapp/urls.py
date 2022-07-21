from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='aboutus'),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('change-password/',views.change_password,name="change-password"),
    path('update-profile/',views.update_profile,name="update-profile"),
    path('add-member/',views.add_member,name="add-member"),
    path('view-member/',views.view_member,name="view-member"),
    path('add-notice/',views.add_notice,name="add-notice"),
    path('view-notice/',views.view_notice,name="view-notice"),
    path('add-event/',views.add_event,name="add-event"),
    path('view-event/',views.view_event,name="view-event"),

    path('update-password/',views.update_password,name="update-password"),
]
