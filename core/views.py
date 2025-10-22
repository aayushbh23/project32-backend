from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import datetime


class HealthCheckView(APIView):
    """
    A lightweight endpoint to verify that the API server is running.
    It does NOT touch the database or require authentication.
    """

    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "status": "ok",
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "service": "project32-api"
        })
