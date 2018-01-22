from app.models import Song

class SongController:
    def getSongList():
        return Song.objects.all()