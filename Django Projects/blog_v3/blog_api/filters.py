import django_filters
from blog_api.models import Post

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    book_author = django_filters.CharFilter(field_name='book_author', lookup_expr='icontains')
    
    # category numeric filter
    category = django_filters.NumberFilter(field_name='category_id')

    created_by = django_filters.CharFilter(field_name='created_by__username', lookup_expr='icontains')
    created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['title', 'book_author', 'category', 'created_by', 'created_after', 'created_before']
