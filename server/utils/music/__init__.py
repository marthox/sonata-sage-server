from .calculate_frequency import calculate_frequency
from .calculate_name import calculate_name

from constants.music import STUTTGART_PITCH

class MusicUtils:
  @classmethod
  def calculate_frequency(cls, key: str, accidental: str|None = None, accidental_occurrence: int = 0, octave: int = 4, precision: int = 4, pitch_reference: float = STUTTGART_PITCH) -> float:
    """
    Given a key, accidental, octave, and reference pitch, calculate the frequency of the note.

    Params:
        key: str: The musical key of the note.
        accidental: str|None: The accidental (sharp, flat, natural) of the note. Default is None.
        accidental_occurrence: int: The number of times the accidental occurs. Default is 0, meaning no accidental or natural.
        octave: int: The octave number of the note.
        precision: int: The number of decimal places to round the frequency to.
        pitch_reference: float: The reference pitch in Hz. Default is 440.0 Hz.

    Returns:
        float: The frequency of the note in Hz.
    """
    return calculate_frequency(key, accidental, accidental_occurrence, octave, precision, pitch_reference)

  @classmethod
  def calculate_name(cls, frequency: float, pitch_reference: float = STUTTGART_PITCH) -> tuple:
    """
    Given a frequency and a reference pitch, calculate the key, accidental, and octave of the note.

    Params:
        frequency: float: The frequency of the note in Hz.
        pitch_reference: float: The reference pitch in Hz. Default is 440.0 Hz.

    Returns:
        tuple: A tuple containing the key, accidental, and octave of the note.
    """
    return calculate_name(frequency, pitch_reference)
