from pathlib import Path
from mutagen import File
from mutagen.easyid3 import EasyID3

METADATA_FIELDS = {'title', 'artist', 'album', 'date', 'tracknumber', 'genre'}

def check_metadata(audio_file: Path) -> bool:
    if audio_file.endswith('.mp3'):
        audio = EasyID3(audio_file)
    else:
        audio = File(audio_file)

    for field in METADATA_FIELDS:
        if field not in audio or not audio[field] or not audio[field][0].strip():
            return False
    
    return True
