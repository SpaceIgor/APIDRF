from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import DirectionSerializer, DoctorSerializer
from .models import Direction, Doctor


class DirectionView(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class PaginationDoctor(PageNumberPagination):
    """ Pagination for Doctor"""
    page_size = 2


class DoctorView(viewsets.ModelViewSet, PageNumberPagination):
    queryset = Doctor.objects.all().order_by('name_doctor', 'id')
    serializer_class = DoctorSerializer
    pagination_class = PaginationDoctor
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['direction', 'experience']
    ordering_fields = ['date_of_birth', 'experience']