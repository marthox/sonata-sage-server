import numpy as np

from utils.validators import Validators
from constants.music import NATURAL_NOTES_INDEX, A4_INDEX, BEMOL, SHARP
    
def get_key_from_index(key_index: int) -> tuple:
    if key_index in NATURAL_NOTES_INDEX:
        return NATURAL_NOTES_INDEX[key_index], None, 0 # No accidental needed
    
    if key_index + 1 in NATURAL_NOTES_INDEX:
        return NATURAL_NOTES_INDEX[key_index - 1], SHARP, 1

    if key_index - 1 in NATURAL_NOTES_INDEX:
        return NATURAL_NOTES_INDEX[key_index - 1], BEMOL, 1
    

@Validators.validate_frequency
def calculate_name(frequency: float, pitch_reference: float) -> tuple:
    semitone_difference = np.round(12 * np.log2(frequency / pitch_reference))  # Calculate the difference in semitones from A4
    pitch = A4_INDEX + semitone_difference  # Calculate the total pitch value
    octave = pitch // 12  # Calculate the octave

    key_index = np.round(pitch % 12)  # Calculate the pitch value
    key, accidental, accidental_occurrence = get_key_from_index(key_index)  # Get the key from the pitch value
    
    return key, accidental, accidental_occurrence, octave
