"""
Media Library Management Class.

Basic properties
- album title, artist, year, genre, cover, track number, disc number.

"""

import mutagen


class Media(object):
    media_db = []

    def __init__(self):
        pass

    def add(self, media_info):
        pass

    def remove(self, media_info):
        pass

    def get_all(self):
        pass

    def add_file(self, file_path):
        ext = file_path.split(".")[-1]

        f = mutagen.File(file_path)

        self.media_db.append({
            "type": ext,
            "info": f
        })