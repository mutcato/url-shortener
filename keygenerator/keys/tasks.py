from keys.models import Key

from keygenerator.celery import app

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(num, alphabet):
    """Encode a positive number into Base X and return the string.

    Arguments:
    - `num`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    arr_append = arr.append  # Extract bound-method for faster access.
    _divmod = divmod  # Access to locals is faster.
    base = len(alphabet)
    while num:
        num, rem = _divmod(num, base)
        arr_append(alphabet[rem])
    arr.reverse()
    return "".join(arr)


def get_next_id() -> int:
    try:
        return Key.objects.last().id + 1
    except AttributeError:
        return 100_000_000  # ID starts from


@app.task
def generate_keys(number: int = 10) -> None:
    number_of_unused_keys = Key.objects.filter(is_used=False).count()
    if number_of_unused_keys < 10000:
        for _ in range(number):
            Key.objects.create(key=encode(get_next_id(), BASE62))
