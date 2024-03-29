from pydantic import BaseModel


class ImageSize(BaseModel):
    w: int
    h: int


class MaskCoords(BaseModel):
    n: int
    x: float
    y: float
    zoom: float


class Sticker(BaseModel):
    alt: str
    mask: bool | None
    # TODO: Implament sickersets and maybe more data from there on.
    mask_coords: MaskCoords | None

class Video(BaseModel):
    round_message: bool | None
    supports_streaming: bool | None
    duration: int
    w: int
    h: int


class Audio(BaseModel):
    voice: bool | None
    duration: int
    title: str | None
    performer: str | None
    waveform: bytes | None


class Filename(BaseModel):
    file_name: str



class CustomEmoji(BaseModel):
    free: bool | None
    alt: str


DocumentAttribute = \
    ImageSize | \
    Sticker | \
    Video | \
    Audio | \
    Filename | \
    CustomEmoji
