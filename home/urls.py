from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
urlpatterns =[
    path('',views.index,name='index'),
    path('addbookfun',views.addbookfun,name='addbookfun'),
    path('addstudentfun',views.addstudentfun,name='addstudentfun'),
    path('borrow/<int:myid>',views.borrow,name='borrow'),
    path('updatebook/<int:myid>',views.updatebook,name='updatebook'),
    path('bookdelete/<int:myid>',views.bookdelete,name='bookdelete'),
    path('learnmore/<int:myid>',views.learnmore,name='learnmore'),
    path('showstudent/update/<int:myid>',views.studentupdate,name='studentupdate'),
    path('showstudent/delete/<int:myid>',views.studentdelete,name='studentdelete'),
    path('showstudent',views.showstudent,name='showstudent'),
]