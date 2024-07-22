from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers
from pittyapi.models import Adoption
from .dog import DogSerializer
from .adopter import AdopterSerializer


class AdoptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adoption
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["dog_id"] = DogSerializer(instance.dog_id).data
        rep["adopter_id"] = AdopterSerializer(instance.adopter_id).data
        return rep


class AdoptionViewSet(viewsets.ModelViewSet):
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        # Check if 'adopter_id' query parameter is provided
        adopter_id = request.query_params.get("adopter_id", None)
        if adopter_id is not None:
            # Filter the queryset based on the provided 'adopter_id'
            queryset = Adoption.objects.filter(adopter_id=adopter_id)
        else:
            # Default behavior: return all adoptions
            queryset = self.queryset

        # Serialize the queryset
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
