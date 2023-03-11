from django.urls import path
from .views import index, topics ,Topic, new_topic, new_entry , edit_entry
from .import views
app_name = 'learning_logs'

urlpatterns = [
     path('', index, name='index'),
     path('topics/',topics, name='topics'),
     path('topics/<int:topic_id>/', views.Topic, name='topic'),
     path('new_topic/',new_topic , name='new_topic'),
     path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
     path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
     ]
