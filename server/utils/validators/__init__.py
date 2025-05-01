from .validate_frequency import validate_frequency

class Validators:
    @classmethod
    def validate_frequency(cls, func) -> None:
        """
        Decorator to validate the frequency of a note.

        Params:
            func: function: The function to be decorated.

        Returns:
            func: The decorated function.
        """
        return validate_frequency(func)
