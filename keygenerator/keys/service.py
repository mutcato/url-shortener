from keys.helpers import lock_table
from keys.models import Key


class KeyService:
    def get_key(self):
        with lock_table(Key):
            obj = Key.objects.filter(is_used=False).first()
            obj.is_used = True
            obj.save()
            return obj.key
