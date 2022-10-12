
from rest_framework import routers
from django.urls import path, include
from .views import BoardViewSet, TaskViewSet, index, board_page, new_board, new_task, edit_task

router = routers.DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', index, name='homepage'),    
    path('<int:board_id>', board_page, name='boardpage'),
    path('new-board', new_board, name='newboard'),
    path('new-task', new_task, name='newtask'),
    path('edit-task', edit_task, name='edittask'),
    path('api/', include(router.urls))
]