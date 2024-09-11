from rest_framework.serializers import ModelSerializer,ImageField
from .models import Testimonal,About,Work,Experience,Skill,Brand,Contact

class TestimonalSerializer(ModelSerializer):
    class Meta:
        model= Testimonal
        fields = "__all__"

class AboutSerailizer(ModelSerializer):
    image =ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = About
        fields = "__all__"

class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"


class WorkExperianceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"
        depth=1

class SkillsSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"