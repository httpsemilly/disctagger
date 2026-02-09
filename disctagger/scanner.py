from pathlib import Path
from typing import Iterator

def find_audio_files(path: Path) -> Iterator[Path]:
    path = Path(path)
    if not path.is_dir():
        raise FileNotFoundError(f"Directory not found: {path}")
    
    file_extensions = ['*.mp3', '*.flac', '*.opus', '*.ogg']

    for ext in file_extensions:
        yield from path.rglob(ext, case_sensitive=False)