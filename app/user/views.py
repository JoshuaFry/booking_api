from rest_framework import generics, permissions
from rest_framework.response import Response
from user.serializers import UserSerializer
from core.models import User


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user

    def patch(self, request, *args, **kwargs):
        """Update users information"""
        serializer = self.serializer_class(self.request.user, data=request.data,
                                         partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
        return Response(status=200, data=serializer.data)

        # self.request.data._mutable = True

        # if self.request.data.get('username', False):
        #     self.request.data['username'] = self.request.data['username'].lower()
        # if self.request.data.get('email', False):
        #     self.request.data['email'] = self.request.data['email'].lower()
