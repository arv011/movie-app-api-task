from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from accounts.models import User
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterUserSerializer(serializers.ModelSerializer):
    '''register validation return hashed password'''
    
    class Meta:
        model = User
        fields = ('id','username','password','email')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return make_password(value)
    
    # def create(self, validated_data):
    #     obj = super().create(validated_data)
    #     obj.email = obj.username
    #     obj.save()
    #     refresh = RefreshToken.for_user(obj)
    #     data = {'access_token': str(refresh), 'username': obj.get_username()}
    #     return data


class LoginUserSerializer(serializers.Serializer):
    '''login validate | return token'''
    username = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    access_token = serializers.CharField(max_length=500, read_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)
        
        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password is not found'
            )
        try:
            refresh = RefreshToken.for_user(user)
            login(self.context['request'], user)
            
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does not exists or incorrect'
            )
        validated_data = {'access_token': str(refresh.access_token), 'username': user.get_username()}
        return validated_data