import mongoengine

class Tweets(mongoengine.Document):
    id = mongoengine.LongField(required=True, unique=True)
    text = mongoengine.StringField(max_length=200, required=True)
    created_at = mongoengine.DateTimeField(required=False)
    screenname = mongoengine.StringField(required=False)