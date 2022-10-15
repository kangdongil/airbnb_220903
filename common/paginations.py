from collections import OrderedDict
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination

class ListPagination(PageNumberPagination):
    
    page_query_param = "page"
    page_size_query_param = "limit"
    page_size = 5
    max_page_size = 10000
    
    
    def get_page_number(self, request):
        try:
        	page_number = int(request.query_params.get(self.page_query_param, 1))
        except ValueError:
            page_number = 1
        return page_number
    
    def get_page_size(self, request):
        try:
            page_size = int(request.query_params.get(self.page_size_query_param, self.page_size))
            if not page_size > 0:
                page_size = self.page_size_query_param
        except ValueError:
            page_size = self.page_size_query_param
        return page_size

    def paginate(self, queryset, request):
        page_number = self.get_page_number(request)
        page_size = self.get_page_size(request)
        
        paginated_queryset = Paginator(queryset, page_size)
        self.page = paginated_queryset.get_page(page_number)
        return list(self.page)