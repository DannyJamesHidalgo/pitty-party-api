from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import action


from pittyapi.models import Adopter
from rest_framework import serializers, viewsets, status


class AdopterSerializer(serializers.ModelSerializer):
    """JSON serializer for Adopters"""

    class Meta:
        model = Adopter
        fields = "__all__"


class AdoptersViewSet(ViewSet):

    queryset = Adopter.objects.all()
    serializer_class = AdopterSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """
        Retrieve a single adopter instance.
        """
        try:
            adopter = Adopter.objects.get(pk=pk)
        except Adopter.DoesNotExist:
            return Response(
                {"error": "Adopter not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AdopterSerializer(adopter)
        return Response(serializer.data)

    def list(self, request):
        """
        Return a list of all adopters.
        """
        adopters = Adopter.objects.all()
        serializer = AdopterSerializer(adopters, many=True)
        return Response(serializer.data)
