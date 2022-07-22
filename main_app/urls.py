from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses_index, name='index'),
    path('courses/<int:course_id>/', views.courses_detail, name='detail'),
    path('courses/create/', views.CourseCreate.as_view(), name='courses_create'),
    path('courses/<int:pk>/update/', views.CourseUpdate.as_view(), name='courses_update'),
    path('courses/<int:pk>/delete/', views.CourseDelete.as_view(), name='courses_delete'),
    path('courses/<int:course_id>/add_lesson/', views.add_lesson, name='add_lesson'),
    path('courses/<int:course_id>/assoc_student/<int:student_id>/', views.assoc_student, name='assoc_student'),
    path('courses/<int:course_id>/unassoc_student/<int:student_id>/', views.unassoc_student, name='unassoc_student'),
    path('students/', views.StudentList.as_view(), name='students_index'),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name='students_detail'),
    path('students/create/', views.StudentCreate.as_view(), name='students_create'),
    path('students/<int:pk>/update/', views.StudentUpdate.as_view(), name='students_update'),
    path('students/<int:pk>/delete/', views.StudentDelete.as_view(), name='students_delete'),
    path('lessons/<int:pk>/', views.lessons_detail, name='lessons_detail'),
    path('lessons/<int:pk>/update/', views.LessonUpdate.as_view(), name='lessons_update'),
    path('lessons/<int:pk>/delete/', views.LessonDelete.as_view(), name='lessons_delete'),
    path('lesson/<int:pk>/add_homework/', views.add_homework, name='add_homework'),
    path('lessons/<int:pk>/HomeWorkDelete/', views.HomeworkDelete.as_view(), name='homework_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('students/<student_id>/add_photo/', views.add_photo, name='add_photo'),
]
