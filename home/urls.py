from django.conf.urls import url
from home import views

urlpatterns = [
 url(r"^authenticate/$", views.login_page, name="login_page"),
 url(r"^youshallnotpass/$", views.fence_page, name="fence_page"),
 url(r"^logout/$", views.logout_page, name="logout_page"),
 url(r"^edit/(.+)/$", views.edit_page, name="edit_page"),
 url(r"^about/$", views.about_page, name="about_page"),
 url(r"^research/$", views.research_page, name="research_page"),
 url(r"^projects/$", views.project_page, name="project_page"),
 url(r"^$", views.home_page, name="home_page")
]
