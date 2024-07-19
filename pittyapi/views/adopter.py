from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from pittyapi.models import Adopter


class AdopterSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Adopters"""

    class Meta:
        model = Adopter
        url = serializers.HyperlinkedIdentityField(
            view_name="adopter", lookup_field="id"
        )
        fields = ("id", "url", "user", "email", "first_name", "last_name")
        depth = 1


class AdoptersViewSet(ViewSet):

    def update(self, request, pk=None):
        """
        @api {PUT} /adopters/:id PUT changes to Adopter profile
        @apiName UpdateAdopter
        @apiGroup Adopter

        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611

        @apiParam {id} id Adopter Id to update
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        adopter = Adopter.objects.get(user=request.auth.user)
        adopter.user.last_name = request.data["last_name"]
        adopter.last_name = request.data["last_name"]
        adopter.user.first_name = request.data["first_name"]
        adopter.first_name = request.data["first_name"]
        adopter.user.email = request.data["email"]
        adopter.email = request.data["email"]
        adopter.user.save()
        adopter.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
