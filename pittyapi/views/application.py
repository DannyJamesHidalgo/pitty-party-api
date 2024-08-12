from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers
from pittyapi.models import Application
from .dog import DogSerializer
from .adopter import AdopterSerializer


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["dog"] = DogSerializer(instance.dog).data
        rep["adopter"] = AdopterSerializer(instance.adopter).data
        return rep


class ApplicationViewSet(viewsets.ModelViewSet):

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        dog_id = request.data.get("dog")
        adopter_id = request.data.get("adopter")

        # Check if an application already exists for this dog and adopter
        existing_application = Application.objects.filter(
            dog_id=dog_id, adopter_id=adopter_id
        ).first()

        if existing_application:
            return Response(
                {"error": "An application already exists for this dog and adopter."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Proceed with creating a new application if none exists
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

    def list(
        self,
        request,
    ):
        # Check if 'adopter_id' query parameter is provided
        adopter_id = request.query_params.get("adopter_id", None)
        if adopter_id is not None:
            # Filter the queryset based on the provided 'adopter_id'
            queryset = Application.objects.filter(adopter_id=adopter_id)
        else:
            # Default behavior: return all adoptions
            queryset = self.queryset

        # Serialize the queryset
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
