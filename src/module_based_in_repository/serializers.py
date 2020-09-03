from rest_framework.serializers import Serializer, IntegerField, CharField


class ItemMiddlewareSerializer(Serializer):
    id = IntegerField()
    name = CharField(max_length=200)
