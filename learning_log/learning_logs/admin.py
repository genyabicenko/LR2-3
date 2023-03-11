from django.contrib import admin

# Register your models here.
from .models import Topic
from django.urls import path, include
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)



urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('learning_logs.urls')),
     path('users/', include('users.urls')),
    
]
