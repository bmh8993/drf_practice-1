from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    # page_size(page_size_query_param으로 지정한)라는 파라미터에 원하는 page_size를
    # 지정할 수 있다. = front 쪽에서 컨트롤 가능
