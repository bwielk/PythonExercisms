class Phone(object):
    def __init__(self, phone_number):
        self.number = self.number(phone_number)

    def number(self, phone_number):
        result = list(filter(lambda x: x.isnumeric(), phone_number))
        if len(result) != 10:
            raise ValueError('The argument must have 10 digits')
        return ''.join(result)
