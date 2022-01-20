from rest_framework import serializers
from .models import contactmodel , uploadmodel
from django.contrib.auth.models import User

class contactmodelserializer(serializers.ModelSerializer):
    class Meta:
        model = contactmodel
        fields = "__all__"


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class uploadserializer(serializers.ModelSerializer):
    class Meta:
        model = uploadmodel
        fields = "__all__"

