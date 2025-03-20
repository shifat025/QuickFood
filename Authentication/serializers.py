from rest_framework import serializers
from django.contrib.auth.models import User


class RegisteSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)

    class Meta:
        model = User
        fields = ('first_name','last_name','email','password','confirm_password' )

    def save(self):
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        

        if password != confirm_password:
            raise serializers.ValidationError({'error': "Password Doesn't Matched"})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error': "Email Already exits"})
        
        # Custom username generation based on email
        username = email.split('@')[0]
        
        account = User(first_name = first_name, last_name = last_name, email = email,username=username)
        account.set_password(password)
        account.save()
    

        return account


