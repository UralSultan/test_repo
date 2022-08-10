from django.urls import path
from .views import CourseListMixinView, CourseDetailMixinView


urlpatterns = [
    path('courses/', CourseListMixinView.as_view(), name='course-list'),
    path(r'courses/<int:pk>/', CourseDetailMixinView.as_view(), name='courses-detail'),
]
