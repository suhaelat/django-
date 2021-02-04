from django.urls import path
from.import views
urlpatterns = [
    path('ass1',views.fun1,name='ass1'),
    path('ass2',views.fun2,name='ass2'),
    path('ass3',views.fun3,name='ass3'),
    path('ass4',views.fun4,name='ass4'),
    path('ass5',views.fun5,name='ass5'),
    path('ass6',views.fun6,name='ass6')
    path('css',views.funcss,name='css'),
    path('bs',views.funbs,name='bs')
]    