from pydantic import BaseModel, Field

class Interval(BaseModel):
    name: str = Field(..., title="Name", description="Name of the interval")
    short_name: str = Field(..., title="Short name", description="Short name of the interval")
    distandce: int = Field(..., title="Distance", description="Distance of the interval in semitones")
