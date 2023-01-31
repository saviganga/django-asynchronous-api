from django.shortcuts import render
from rest_framework.views import APIView


from rest_framework.response import Response
from rest_framework import status

from . import utils as async_utils

# Create your views here.

class AsyncViewSet(APIView):

    def get(self, request):

        is_quotes, quotes = async_utils.ExternalAPI().quotable_api()
        if not is_quotes:
            return Response(
                data={
                    "status": "FAILED",
                    "message": "Unable to get quotes"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # randomuser api has a problem
        # is_randouser, randomuser = async_utils.ExternalAPI().random_user()
        # if not is_randouser:
        #     return Response(
        #         data={
        #             "status": "FAILED",
        #             "message": "Unable to get random user"
        #         },
        #         status=status.HTTP_400_BAD_REQUEST
        #     )

        return Response(
            data={
                "status": "SUCCESS",
                "message": "Successfully fetched quotes and random user",
                "data": {
                    "quotes": quotes,
                    # "randomuser": randomuser
                }
            },
            status=status.HTTP_200_OK
        )




