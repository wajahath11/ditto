from django.urls import path
from .views import PolicyListView, PolicyDetailView, CommentCreateView, CommentRetrieveByPolicyView

urlpatterns = [
    path('policies/', PolicyListView.as_view(), name='policy-list'),
    path('policies/<int:pk>/', PolicyDetailView.as_view(), name='policy-detail'),

    path('comments/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/policy/<int:policy_id>/', CommentRetrieveByPolicyView.as_view(), name='comment-retrieve-by-policy'),

]
