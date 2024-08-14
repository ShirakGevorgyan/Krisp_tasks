import io

class ChecksumStorage(io.BufferedWriter):
    def __init__(self, raw):
        super().__init__(raw)
        self.checksum = 0

    def write(self, b):

        self.checksum += sum(b)
        return super().write(b)

def get_payments_storage():
  
    return open('/dev/null', 'wb')

def stream_payments_to_storage(storage):

    for i in range(10):
        storage.write(bytes([1, 2, 3, 4, 5]))

def process_payments():

    with get_payments_storage() as raw_storage:
        checksum_storage = ChecksumStorage(raw_storage)
        
        stream_payments_to_storage(checksum_storage)

        print("Checksum of bytes written:", checksum_storage.checksum)


process_payments()
