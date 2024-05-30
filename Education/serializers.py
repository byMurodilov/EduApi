from rest_framework import serializers

from .models import Courses, Teachers, Students



class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    subject = serializers.CharField(max_length=11)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    davomiyligi = serializers.IntegerField()


    def create(self, validated_data):
        return Courses.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.price = validated_data.get('price', instance.price)
        instance.davomiyligi = validated_data.get('davomiyligi', instance.davomiyligi)
        instance.save()
        return instance




class TeacherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Courses.objects.all())
    full_name = serializers.CharField(max_length=45)
    status = serializers.CharField(max_length=50)
    tajriba = serializers.CharField()


    def create(self, validated_data):
        return Teachers.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.course = validated_data.get('course', instance.course)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.status = validated_data.get('status', instance.status)
        instance.tajriba = validated_data.get('tajriba', instance.tajriba)
        instance.save()
        return instance





class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(max_length=33)
    phone_num = serializers.DecimalField(max_digits=13, decimal_places=0)
    parents_phone_num = serializers.DecimalField(max_digits=13, decimal_places=0)
    telegram_link = serializers.CharField(max_length=41)
    address = serializers.CharField(max_length=100)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Courses.objects.all())
    teacher_id = serializers.PrimaryKeyRelatedField(queryset=Teachers.objects.all())


    def create(self, validated_data):
        return Students.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.phone_num = validated_data.get('phone_num', instance.phone_num)
        instance.parents_phone_num = validated_data.get('parents_phone_num', instance.parents_phone_num)
        instance.telegram_link = validated_data.get('telegram_link', instance.telegram_link)
        instance.address = validated_data.get('address', instance.address)
        instance.course_id = validated_data.get('course_id', instance.course_id)
        instance.teacher_id = validated_data.get('teacher_id', instance.teacher_id)
        instance.save()
        return instance