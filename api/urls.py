from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('todos', views.TodoViewSet, basename='todo')

todo_router = routers.NestedDefaultRouter(router, 'todos', lookup='todo')
todo_router.register('items', views.TodoItemViewset, basename='todo-items')

urlpatterns = router.urls + todo_router.urls

# urlpatterns = [
#     path('todos/<int:todo_id>/items/', views.TodoItemList.as_view(),),
#     path('todos/<int:todo_id>/items/<int:item_id>/', views.TodoItemDetail.as_view(),),
#   ]
