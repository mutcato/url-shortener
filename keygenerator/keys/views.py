from keys.service import KeyService
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class KeyApiView(APIView):
    service = KeyService()

    def get(self, request, *args, **kwargs):
        key = self.service.get_key()
        return Response(data={"key": key}, status=status.HTTP_200_OK)
