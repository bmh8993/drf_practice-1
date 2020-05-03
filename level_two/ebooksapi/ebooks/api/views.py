from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import get_object_or_404

from ..models import Ebook, Review
from ..api.serializers import EbookSerializer, ReviewSerializer


class EbookListCreateAPIView(generics.ListCreateAPIView):
    # ListCreateAPIView는 아래의 코드를 모두 상속하고 있다.
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class EbookDetatilAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


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

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)  # CreateAPIView=>mixins가 정의된 부분을 보자


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
