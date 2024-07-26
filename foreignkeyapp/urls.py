from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('addcoursedb',views.addcoursedb,name='addcoursedb'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('addstudentdb',views.addstudentdb,name='addstudentdb'),
    path('showstd',views.showstd,name='showstd'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editdb/<int:pk>',views.editdb,name='editdb'),
    path('delete/<int:pk>',views.delete,name='delete'),
]