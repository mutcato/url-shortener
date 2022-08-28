import random
import string


class UrlService:
    def get_key(self):
        letters = string.ascii_letters + "0123456789"
        result_str = "".join(random.choice(letters) for _ in range(7))
        return result_str
