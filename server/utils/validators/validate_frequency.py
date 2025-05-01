def validate_frequency(func):
    """
    Decorator to validate the frequency of a note.
    """
    def wrapper(*args, **kwargs):
        # Get the two first arguments of the decorated function
        frequency, pitch_reference = args[:2]
        if frequency < 0.0 or pitch_reference < 0.0:
            raise ValueError("Frequency and pitch reference must be greater than or equal to 0.0.")
        return func(*args, **kwargs)
    return wrapper
