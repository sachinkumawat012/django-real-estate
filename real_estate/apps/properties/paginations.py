from rest_framework.pagination import PageNumberPagination


class PropertyPagiantion(PageNumberPagination):
    page_size = 5
