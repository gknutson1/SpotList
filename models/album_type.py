from enum import Enum


class AlbumType(str, Enum):
    album = "album"
    single = "single"
    compilation = "compilation"
    appears_on = "appears_on"
