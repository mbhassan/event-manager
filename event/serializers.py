from rest_framework import serializers
from organisation.serializer import OrganisationSerializer
from user.serializer import UserSerializer
from .models import Event, EventLocation, EventSponser, EventComment, EventTag, Submission, Form
from jsonschema import validate, exceptions as jsonschema_exceptions
from event_manager.errors import ERORRS


# Event location Serializers
class EventLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventLocation
        fields = ('id', 'name', 'address', 'logo')

# Event sponsers serializers
class EventSponserSerializer(serializers.ModelSerializer):


    class Meta:
        model = EventSponser
        fields = ('id', 'name', 'logo')

class EventCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventComment
        fields = ('id', 'comment', 'commented_by', 'comment_datetime')

class EventTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventTag
        fields = ('id', 'name')

class EventCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('__all__')


class EventSerializer(serializers.ModelSerializer):

    organisation = OrganisationSerializer()
    location = EventLocationSerializer()
    sponsers = EventSponserSerializer(many=True)
    comments = EventCommentSerializer(many=True)
    tags = EventTagSerializer(many=True)
    attendees = UserSerializer(many=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'start_datetime',
                  'end_datetime', 'organisation', 'cover', 'location', 'sponsers', 'attendees', 'tags', 'comments')

class EventUserAddSerializer(serializers.Serializer):
    userid = serializers.UUIDField()
    eventid = serializers.IntegerField()

    class Meta:
        model = Event
        fields = ['__all__']

    @classmethod
    def update(self, instance, validated_data):
        event = Event.objects.get(id=validated_data['eventid'])
        event.attendees.add(validated_data['userid'])
        event.save()
        return event

class EventCommentAddSerializer(serializers.Serializer):
    commentid = serializers.UUIDField()
    eventid = serializers.IntegerField()

    class Meta:
        model = Event
        fields = ['__all__']

    @classmethod
    def update(self, instance, validated_data):
        event = Event.objects.get(id=validated_data['eventid'])
        event.comments.add(validated_data['commentid'])
        event.save()
        return event


class SubmissionSerializer(serializers.ModelSerializer):
    submission = serializers.JSONField()
    form = serializers.PrimaryKeyRelatedField(queryset=Form.objects.all(), required=False)

    def validate(self, attrs):
        questions = attrs.get('form').fields
        replies = attrs.get('submission')

        required_questions = set([x.get('position') for x in questions if x.get('required')])

        valid_replies = set([x.get('position') for x in replies if (x.get('reply') and x.get('position'))])
        submitted_questions = required_questions.intersection(valid_replies)

        if len(required_questions) != len(submitted_questions):
            raise serializers.ValidationError(ERORRS.get('ERROR_INCOMPLETE_FORM'))

        return attrs

    def create(self, validated_data):

        replies = validated_data.get('submission')
        fields = validated_data.get('form').fields

        for index, value in enumerate(replies):
            value.update(fields[index])

        validated_data['submission'] = replies

        return super().create(validated_data)

    class Meta:
        model = Submission
        fields = ('id', 'submission', 'form')


class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form
        fields = '__all__'
