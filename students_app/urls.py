# from django.urls import path
# from .views import student_list, students_detail # views сделаны на функциях
# from .views import StudentsListAPIView, StudentDetailAPIView # views сделан на классах
# from .views import StudentListMixinView, StudentDetailMixinView  # views сделан миксинами
# from .views import StudentListCreateView, StudentDetailView  # views сделан на генериках
# from .views import StudentCreateView, StudentCourseView
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"students", StudentViewSet, basename='students')
urlpatterns = router.urls


"""
urlpatterns = [
    # path('', StudentCreateView.as_view(), name='student_create'), # views сделан на классах
    # path('student_course/', StudentCourseView.as_view(), name='student_course_create'), # views сделан на классах
    # path('students/', student_list, name='student-list'), # views сделаны на функциях
    # path('students/', StudentsListAPIView.as_view(), name='student-list'), # views сделан на классах
    # path('students/', StudentListMixinView.as_view(), name='student-list'),  # views сделан миксинами
    # path('students/', StudentListCreateView.as_view(), name='student-list'),  # views сделан генериках
    path('students/', StudentViewSet.as_view({'get': 'list'}), name='student-list'),  # views сделан на viewSet
    # path('students/<int:pk>/', students_detail, name='student-detail'),# views сделаны на функциях
    # path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'), # views сделан на классах
    # path('students/<int:pk>/', StudentDetailMixinView.as_view(), name='student-detail'),  # views сделан миксинами
    # path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),  # views сделан генериках
    path('students/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve'}), name='student-detail'),  # views 
                                                                                                    # сделан на viewSet
]
"""