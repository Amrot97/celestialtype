from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class NatalChartView(APIView):
    def post(self, request):
        try:
            data = request.data
            # Here you would process the data and generate the natal chart
            # For now, we'll just return the received data
            return Response({
                'message': 'Natal chart data received',
                'data': data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST) 