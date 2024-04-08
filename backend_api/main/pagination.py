from rest_framework.pagination import PageNumberPagination

class CustomPagination1(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10

class CustomPagination2(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5
