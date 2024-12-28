# опрацювання помилок

class FiveDivisionError(Exception):
    # клас для демонстрації опрацювання помилок
    def __init__(self, message, error_code):
        super().__init__(message)
        # додаємо власне поле
        self.error_code = error_code




def devide_number(a,b):
    if b == 5:
        raise FiveDivisionError('ділення на 5 неможливе!!!', 400)
    return a / b


try:
    result = devide_number(12, 2)
    print(result)
except FiveDivisionError as e:
    print(e)
    print(f'код помилки{e.error_code}')