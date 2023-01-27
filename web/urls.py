from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("course-list/<str:id>", views.courseList, name="course-list"),
    path("course-detail/", views.courseDetail, name="course-detail"),
    path("updates/", views.updates, name="updates"),
    path("update-detail/<str:id>", views.update_detail, name="update-detail"),
    path("event/", views.event, name="event"),
    path("event-detail/<str:id>", views.event_detail, name="event-detail"),
    path("university/<str:id>", views.university, name="university"),
    path("university-detail/<str:id>", views.university_detail, name="university-detail"),
    path("contact/", views.contact, name="contact"),
    path("service/<str:id>", views.service, name="service"),
    path("service-detail/<str:id>", views.service_detail, name="service-detail"),

    path("career/", views.career, name="career"),
    path("career-detail/<str:id>", views.career_detail, name="career-detail"),


    path("domestic/", views.domestic, name="domestic"),
    path("international", views.international, name="international"),

]