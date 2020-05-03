from django.urls import path
from ..api.views import (
        EbookListCreateAPIView,
        EbookDetatilAPIView,
        ReviewCreateAPIView,
        ReviewDetailAPIView
        )

urlpatterns = [
        path("ebooks/",
            EbookListCreateAPIView.as_view(),
            name="ebook-list"),
        path("ebooks/<int:pk>/",
            EbookDetatilAPIView.as_view(),
            name="ebook-detail"),
        path("ebooks/<int:ebook_pk>/review/",
            ReviewCreateAPIView.as_view(),
            name="ebook-review"),
        path("reviews/<int:pk>/",
            ReviewDetailAPIView.as_view(),
            name="review-detail"),
        ]
