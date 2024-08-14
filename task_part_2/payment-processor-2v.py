import io

def stream_payments(callback_fn):
    """
    Reads payments from a payment processor and calls `callback_fn(amount)` for each payment.
    Returns when there is no more payments.
    """
    for amount in range(1, 11):
        callback_fn(amount)

def store_payments(amount_iterator):
    """
    Iterates over the payment amounts from amount_iterator and stores them to a remote system.
    """

    for amount in amount_iterator:
        print(f"Stored payment amount: {amount}")

def process_payments_2():
    """
    Glue code to connect stream_payments and store_payments using a generator.
    """
    def payment_generator():
        """
        Generator function to adapt streamed payments for storing.
        """
        payments = []
        def callback(amount):
            payments.append(amount)
            return True
        
        stream_payments(callback)
        

        for payment in payments:
            yield payment
    

    store_payments(payment_generator())


process_payments_2()
