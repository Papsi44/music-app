from django import forms


from music_project.albums.models import Album
from music_project.mixins import PlaceholderMixin, ReadOnlyMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ("owner",)


class AlbumAddForm(PlaceholderMixin, AlbumBaseForm):
    pass


class AlbumEditForm(PlaceholderMixin, AlbumBaseForm):
    pass


class AlbumDeleteForm(ReadOnlyMixin, AlbumBaseForm):
    readonly_fields = ['album_name', 'artist', 'genre', 'description', 'image_url', 'price']
