#  class PictsUserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Picts
#         fields = ('user', 'ipaddress', 'macaddress',)

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     picts = PictsUserSerializer(required=False, many=False)

#     class Meta:
#         model = User
#         fields = ('id','username', 'email', 'first_name', 'last_name', )
#         #write_only_fields = ('password',)

#     def create(self, validated_data):
#         picts_data = validated_data.pop('picts')
#         user = User.objects.create(**validated_data)
#         Picts.objects.create(**picts_data)
#         return user

#     def update(self, instance, validated_data):
#         picts_data = validated_data.pop('picts')
#         # Update User data
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.email = validated_data.get('email', instance.email)
#         # Update UserProfile data
#         if not instance.picts:
#             Picts.objects.create(user=instance, **picts_data)
#         #instance.picts.uid = picts_data.get('uid', instance.picts.uid)
#         instance.picts.ipaddress = picts_data.get('ipaddress', instance.picts.ipaddress)
#         instance.save()
