import numpy as np

from constants.music import NATURAL_NOTES_KEY, ACCIDENTALS, A4_INDEX, STUTTGART_PITCH

def calculate_frequency(key: str, accidental: str|None = None, accidental_occurrence: int = 0, octave: int = 4, precision: int = 4, pitch_reference: float = STUTTGART_PITCH) -> float:
    if accidental is not None and accidental_occurrence is not None:
        accidental_value = ACCIDENTALS[accidental] * accidental_occurrence  # Get the pitch adjustment for the accidental
    else:
        accidental_value = 0  # No accidental provided
    
    pitch_value = NATURAL_NOTES_KEY[key]  # Get the pitch value of the natural note

    pitch = pitch_value + accidental_value + (octave * 12)  # Calculate the total pitch value
    semitone_difference = pitch - A4_INDEX  # Calculate the difference in semitones from A4
    frequency = np.round(pitch_reference * np.power(2, (semitone_difference / 12.0)), precision)  # Calculate the frequency
    return frequency
