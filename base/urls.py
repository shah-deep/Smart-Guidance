from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    # path('topics/',views.topics, name='posts'),
    path('topic/<slug:slug>',views.topic_part, name='topic'),
    path('chemistry/',views.topic_chemistry, name='chemistry'),
    path('default/',views.topic_default, name='default'),
    path('fauna/',views.topic_fauna, name='fauna'),
    path('flora/',views.topic_flora, name='flora'),
    path('machinery/',views.topic_machinery, name='machinery'),
    path('biology/',views.topic_biology, name='biology'),
    path('astronomy/',views.topic_astronomy, name='astronomy'),
    # path('',views.home, name='home'),
]