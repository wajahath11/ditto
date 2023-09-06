from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Policy, Comment
from .serializers import PolicySerializer, CommentSerializer
from .utils import IsAdminOrReadOnly

"""
NOTE: Level - 1
Please try to build Admin Views (or) Only APIs to perform the following actions.
● Allow admin to create, edit & delete the policy.
● List out all the policies (with pagination).
● Filter policies using the following things
    ○ Policy Status
    ○ Customer Name
    ○ Created date
"""


class PolicyListView(generics.ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'policy_status': ['exact'],
        'customer_name': ['icontains'],
        'created_at': ['date__range'],
    }
    search_fields = ['customer_name', 'application_number']
    ordering_fields = ['created_at']
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAdminOrReadOnly]  # Used custom permission class

    # Add pagination settings
    pagination_class = PageNumberPagination
    page_size = 5  # Adjust the number of items per page as needed

    def perform_create(self, serializer):
        policy = serializer.save()
        """
        NOTE: Level - 2
        ● When a policy is issued send an automated email to the customer email, saying his
            policy has been issued. Do not forget to include the policy number in the email (feel free
            to decide the mail body yourself).
        """
        policy.trigger_email()


class PolicyDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]  # Used custom permission class
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


"""
Level - 3
● Allow Admins to add comments to any policy.
● List out all comments of a specific policy.
"""


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]


class CommentRetrieveByPolicyView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        policy_id = self.kwargs.get('policy_id')
        return Comment.objects.filter(policy_id=policy_id)
