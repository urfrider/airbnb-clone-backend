from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Service
from .serializers import ServiceSerializer


class Services(APIView):
    def get(self, request):
        all_services = Service.objects.all()
        serializer = ServiceSerializer(all_services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            service = serializer.save()
            return Response(ServiceSerializer(service).data)
        else:
            return Response(serializer.errors)


class ServiceDetail(APIView):
    def get_object(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    def put(self, request, pk):
        service = self.get_object(pk)
        serializer = ServiceSerializer(
            service,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_service = serializer.save()
            return Response(ServiceSerializer(updated_service).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        service = self.get_object(pk)
        service.delete()
        return Response(status=HTTP_204_NO_CONTENT)
