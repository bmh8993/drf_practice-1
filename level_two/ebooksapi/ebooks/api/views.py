from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from ..models import Ebook, Review
from ..api.serializers import EbookSerializer, ReviewSerializer
from ..api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly


class EbookListCreateAPIView(generics.ListCreateAPIView):
    # ListCreateAPIView는 아래의 코드를 모두 상속하고 있다.
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # 개별로 설정하면 view마다 다른 권한을 설정할 수 있다.
    permission_classes = [IsAdminUserOrReadOnly]


class EbookDetatilAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsAdminUserOrReadOnly]


#class EbookListCreateAPIView(
#        mixins.ListModelMixin,
#        mixins.CreateModelMixin,
#        generics.GenericAPIView):
#    queryset = Ebook.objects.all()
#    serializer_class = EbookSerializer
#
#    def get(self, request, *args, **kwargs):
#        return self.list(request, *args, **kwargs)
#
#    def post(self, request, *args, **kwargs):
#        return self.create(request, *args, **kwargs)


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)

        review_author = self.request.user

        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)

        if review_queryset.exists():
            raise ValidationError("You Have Already Reviewed this Ebook!")

        serializer.save(ebook=ebook, review_author=review_author)  # CreateAPIView=>mixins가 정의된 부분을 보자


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = IsReviewAuthorOrReadOnly
