from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import *


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class LoginSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['nickname', 'password']


class SignupSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'nickname',
            'password',
            'avatar',
            'background',
            'signature'
        ]


class SuperSignupSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'nickname',
            'password',
            'avatar',
            'background',
            'signature'
        ]

    def create(self, validated_data):
        validated_data['type'] = 'super'
        return Account.objects.create(**validated_data)


class InfoSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'account_id',
            'nickname',
            'avatar',
            'background',
            'signature'
        ]


class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = ['token', 'date']


class TopicSerializer(ModelSerializer):
    accountname = SerializerMethodField()
    categoryname = SerializerMethodField()

    class Meta:
        model = Topic
        fields = '__all__'

    # def create(self, validated_data):
    #     new_id = Id.objects.create()
    #     validated_data['topic_id'] = new_id
    #     return Topic.objects.create(**validated_data)
    def get_accountname(self, instance):
        name = instance.account.nickname
        queryset = str(name)
        if queryset is not None:
            return queryset
        else:
            return "未知"

    def get_categoryname(self, instance):
        category2 = instance.category2.category2_name
        queryset = str(category2)
        if queryset is not None:
            return queryset
        else:
            return "未知"


class TopicCreateSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = ['category2_id', 'account_id', 'content', 'tags']

    # def create(self, validated_data):
    #     new_id = Id.objects.create()
    #     validated_data['topic_id'] = new_id
    #     return Topic.objects.create(**validated_data)


class RePlyTopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = ['topic_title', ]



class ReplySerializer(ModelSerializer):
    id = SerializerMethodField()
    commentUser = SerializerMethodField()
    targetUser = SerializerMethodField()
    createDate = SerializerMethodField()
    childrenList = SerializerMethodField()

    def get_id(self, data):
        result = data.reply_id
        if result:
            return result
        else:
            return ""

    def get_commentUser(self, data):
        accountData= data.account
        if accountData:
            return {
                "id":accountData.account_id,
                "nickName":accountData.nickname,
                "avator":""
            }
        else:
            return ""

    def get_targetUser(self, data):
        parentData = data.parent_reply
        if parentData:
            accountData= parentData.account
        else:
            accountData= data.topic.account
        if accountData:
            return {
                "id":accountData.account_id,
                "nickName":accountData.nickname,
                "avator":""
            }
        else:
            return ""

    def get_createDate(self, data):
        result = data.create_time
        if result:
            return result
        else:
            return ""

    def get_childrenList(self, data):
        queryset = Reply.objects.filter(parent_reply=data.reply_id, topic_id=data.topic_id).all()
        children = ReplySerializer(queryset, many=True).data
        if children:
            return children
        else:
            return []

    class Meta:
        model = Reply
        fields = "__all__"
    # def create(self, validated_data):
    #     new_id = Id.objects.create()
    #     validated_data['reply_id'] = new_id
    #     return Reply.objects.create(**validated_data)


class ReplyCreateSerializer(ModelSerializer):
    class Meta:
        model = Reply
        fields = ['master_id', 'account_id', 'content']

    # def create(self, validated_data):
    #     new_id = Id.objects.create()
    #     validated_data['reply_id'] = new_id
    #     return Reply.objects.create(**validated_data)


class RemindSerializer(ModelSerializer):
    class Meta:
        model = Remind
        fields = '__all__'


class FocusAccountSerializer(ModelSerializer):
    class Meta:
        model = FocusAccount
        fields = '__all__'


class FocusTopicSerializer(ModelSerializer):
    class Meta:
        model = FocusTopic
        fields = '__all__'


class ReplyCollectSerializer(ModelSerializer):
    class Meta:
        model = ReplyCollect
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category1
        fields = '__all__'


class Category2Serializer(ModelSerializer):
    class Meta:
        model = Category2
        fields = '__all__'


class ReportSerializer(ModelSerializer):
    messagetitle = SerializerMethodField()

    class Meta:
        model = Report
        fields = '__all__'

    def get_messagetitle(self, instance):
        title = instance.message_id.topic_title
        queryset = str(title)
        print(title)
        if queryset is not None:
            return queryset
        else:
            return "未知"


class TopicAttitudeSerializer(ModelSerializer):
    class Meta:
        model = TopicAttitude
        fields = '__all__'
