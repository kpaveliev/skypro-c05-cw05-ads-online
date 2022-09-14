from rest_framework import serializers

from ads.models import Comment
from users.models import User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):

    # User information
    author_first_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='first_name'
    )

    author_last_name = serializers.SlugRelatedField(
        source='author',
        many=False,
        queryset=User.objects.all(),
        slug_field='last_name'
    )

    # author_image = serializers.SlugRelatedField(
    #     source='author',
    #     many=False,
    #     queryset=User.objects.all(),
    #     slug_field='image'
    # )

    class Meta:
        model = Comment
        fields = ['pk', 'text', 'created_at',
                  'author_id', 'author_first_name', 'author_last_name',
                  # 'author_image',
                  'ad_id']