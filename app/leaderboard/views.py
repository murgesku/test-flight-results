from typing import Final

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Results
from .serializers import RequestSerializer, ResponseSerializer


NUM_RESULTS : Final = 9


class ResultsView(APIView):
    def post(self, request):
        request_data = RequestSerializer(data=request.data)
        request_data.is_valid(raise_exception=True)

        results = Results.best(num=NUM_RESULTS, **request_data.validated_data)
        if results:
            response_data = ResponseSerializer({
                'user_result': results[0],
                'other_results': results[1:]
            })
            return Response(response_data.data)
        else:
            response_data = {
                'user_result': None,
                'other_results': [],
            }
            return Response(response_data)
