import uuid, base64

base64.urlsafe_b64encode(uuid.uuid4().bytes)
