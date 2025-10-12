from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.serializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSummarySerializer

User = get_user_model()


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """
        Follow user with id=user_id
        """
        try:
            target = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        if target == request.user:
            return Response({'detail': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(target)
        request.user.save()
        return Response({'detail': f'You are now following {target.username}.'}, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """
        Unfollow user with id=user_id
        (using POST so client doesn't need to send body; can use DELETE if you prefer)
        """
        try:
            target = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        if target == request.user:
            return Response({'detail': "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(target)
        request.user.save()
        return Response({'detail': f'You have unfollowed {target.username}.'}, status=status.HTTP_200_OK)


class FollowingListView(generics.ListAPIView):
    """
    List users that the request.user is following.
    """
    serializer_class = UserSummarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.following.all()


class FollowersListView(generics.ListAPIView):
    """
    List users that follow the request.user.
    """
    serializer_class = UserSummarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.followers.all()



class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=response.data['username'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': response.data})


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data})


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
