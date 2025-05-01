import numpy as np

from pydantic import BaseModel, Field, computed_field

from utils import Utils as utils
from constants.music import STUTTGART_PITCH

class Note(BaseModel, extra="forbid"):
    """
    A class to represent a musical note.
    Attributes:
        frequency (float): The frequency of the pitch in Hertz. Must be greater than or equal to 0.0.
        key (str): The musical key of the pitch.
        accidental (str): The accidental (sharp, flat, natural) of the pitch.
        octave (int): The octave number of the pitch. Must be greater than or equal to 0.
    Methods:
        __init__(frequency: float):
            Initializes the Pitch object using the given frequency.
            Calculates the key, accidental, and octave based on the frequency and STUTTGART_PITCH.
        __init__(key, accidental, octave):
            Initializes the Pitch object using the given key, accidental, and octave.
            Calculates the frequency based on the key, accidental, and octave.
        id() -> int:
            Computes and returns a unique identifier for the pitch based on its frequency.
    """
    frequency: float = Field(ge=0.0, frozen=True)
    key: str = Field(ge=0, frozen=True)
    accidental: str = Field(ge=0, frozen=True)
    accidental_occurrence: int = Field(ge=0, frozen=True)
    octave: int = Field(ge=0, frozen=True)
    reference_pitch: float = Field(default=STUTTGART_PITCH, ge=0, frozen=True)

    @classmethod
    def from_frequency(
        self,
        frequency: float,
        reference_pitch: float|None = None
    ):
        if reference_pitch:
            self.reference_pitch = reference_pitch
        
        self.frequency = frequency
        self.key, self.accidental, self.accidental_occurrence, self.octave = utils.music.calculate_name(frequency, self.reference_pitch)
        return self

    @classmethod
    def from_name(self,
        key: str,
        accidental: str | None = None,
        accidental_occurrence: int | None = None,
        octave: int | None = np.float64(4),
        reference_pitch: float | None = np.float64(STUTTGART_PITCH),
    ):
        self.frequency = utils.music.calculate_frequency(key, accidental, accidental_occurrence, octave, reference_pitch)
        self.key = key
        self.accidental = accidental
        self.octave = octave
        return self

    def __setattr__(self, name: str, value: any) -> None:
        if name == "frequency":
            self.__init__(value, self.reference_pitch)
        elif name == "key" or name == "accidental" or name == "octave":
            self.__init__(self.key, self.accidental, self.octave, self.reference_pitch)
        else:
            return super().__setattr__(name, value)

    @computed_field(return_type=int)
    def id(self):
        return int(12 * (np.log2(self.frequency / self.reference_pitch)))
