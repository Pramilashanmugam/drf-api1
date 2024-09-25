from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my drf API!"
    })

@api_view(['POST'])
def logout_route(request):
    # You can customize this logic for logging out, e.g., deleting a token or session.
    return Response({
        "message": "Logged out successfully"
    }, status=status.HTTP_200_OK)