class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    def __init__(self):
        super().__init__('Buffer is empty. Please write some data into the buffer')


class CircularBuffer(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = list(range(0, capacity))
        self.written_data = []

    def read(self):
        if len(self.written_data) == 0:
            raise BufferEmptyException

    def write(self, data):
        self.written_data.append(data)

    def overwrite(self, data):
        pass

    def clear(self):
        pass
