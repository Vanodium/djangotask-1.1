def validate_desc(value):
    must_be_in_our_item = {'превосходно', 'роскошно'}
    cleaned_value = set(value.lower().split())
    # r'\bпревосходно\b'
    difference = must_be_in_our_item - cleaned_value
    if len(difference) == len(must_be_in_our_item):
        raise ValueError(
            f'Обязятально нужно использовать {must_be_in_our_item}')
    return value


def validate_slug(value):
    a = 'abcdefghijklmnopqrstuvwxyz'
    for symbol in value:
        terms = symbol.isdigit() or symbol.lower() in a or symbol in ['-', '_']
        if terms and len(value) <= 200:
            return value
        raise ValueError('Длина до 200, только цифры, латиница и - или _')


def validate_weight(value):
    if not 0 < value < 32767:
        raise ValueError('Некорректный вес товара')
    return value
