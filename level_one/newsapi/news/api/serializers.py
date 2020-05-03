from datetime import datetime
from django.utils.timesince import timesince

from rest_framework import serializers
from ..models import Article, Journalist


#class JournalistSerializer(serializers.ModelSerializer):
#
#    class Meta:
#        model = Journalist
#        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    #author = JournalistSerializer(read_only=True)
    #author는 필수 null=True가 아니라서 필수 항목이다.
    # 더 나은 구조는 분명한 관계를 만드는 것이다. 아래를 보자
    #author = serializers.StringRelatedField()  # 해당 serializers field의 str 값을 리턴한다. default는 foreignkey의 id 값이다.

    class Meta:
        model = Article
        #exclude = ("id",)  # 모델의 일부 필드를 제외하겠다.
        fields = "__all__"  # 모델의 모든 필드를 사용하기를 원한다.
        #fields = ("title", "description", "body")  # 모델의 일부 필드만 선택적으로 사용하겠다

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, data):
        """ check that description and title are different """
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description must be different from one another!")
        return data

    def validate_title(self, value):
        if len(value) < 30:
            raise serializers.ValidationError("The title has to be at least 30 chars long!")
        return value


class JournalistSerializer(serializers.ModelSerializer):

    #articles = ArticleSerializer(many=True, read_only=True)  # Journalist에 해당하는 artarticles list가 함께 나온다
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article-detail")  # get a direct link to the proper endpoint for a specific resource

    class Meta:
        model = Journalist
        fields = "__all__"


#class ArticleSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    author = serializers.CharField()
#    title = serializers.CharField()
#    description = serializers.CharField()
#    body = serializers.CharField()
#    location = serializers.CharField()
#    publication_date = serializers.DateField()
#    active = serializers.BooleanField()
#    created_at = serializers.DateTimeField(read_only=True)
#    updated_at = serializers.DateTimeField(read_only=True)
#
#    def create(self, validated_data):
#        print(validated_data)
#        return Article.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#        instance.author = validated_data.get("author", instance.author)
#        instance.title = validated_data.get("title", instance.title)
#        instance.description = validated_data.get("description", instance.description)
#        instance.body = validated_data.get("body", instance.body)
#        instance.location = validated_data.get("location", instance.location)
#        instance.publication_date = validated_data.get("publication_date", instance.publication_date)
#        instance.active = validated_data.get("active", instance.active)
#        instance.save()
#        return instance
#
#    def validate(self, data):
#        """ check that description and title are different """
#        if data["title"] == data["description"]:
#            raise serializers.ValidationError("Title and Description must be different from one another!")
#        return data
#
#    def validate_title(self, value):
#        if len(value) < 60:
#            raise serializers.ValidationError("The title has to be at least 60 chars long!")
#        return value
