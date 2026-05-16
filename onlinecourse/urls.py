from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # 1. The popular course list view (onlinecourse/)
    path(route='', view=views.popular_course_list, name='popular_course_list'),
    
    # 🚨 2. ADD THIS LINE: The course details view (onlinecourse/course/1/)
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    
    # 3. The enroll view (onlinecourse/course/1/enroll/)
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)