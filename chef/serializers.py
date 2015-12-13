from rest_framework import serializers
from chef.models import Chef

class CreateChefSerializer(serializers.Serializer):

    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    CHINEASE = "Chinease"
    ITALIAN = "Italian"
    SOUTH_INDIAN = "South_Indian"
    MAXICAN = "Maxican"

    specialization = (
    (CHINEASE, "Chinease"),
    (ITALIAN, "Italian"),
    (SOUTH_INDIAN, "South_Indian"),
    (MAXICAN, "Maxican"))

    specialization = serializers.ChoiceField(choices=specialization)



class RecipeSerializer(serializers.Serializer):

    name = serializers.CharField()
    chef = serializers.CharField()
    steps_to_make = serializers.CharField()
    meta_data = serializers.CharField(allow_blank=True, allow_null=True)


    def create(self, validated_data):
        """
        Create and return a new `Recipe` instance, given the validated data.
        """
        return Recipe.objects.create(**validated_data)
