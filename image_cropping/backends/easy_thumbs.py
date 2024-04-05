"""
Backend for easy_thumbnails_ package. This module can't be named
"easy_thumbnails" in order to avoid Python import conflicts.

.. _easy_thumbnails: https://github.com/SmileyChris/easy-thumbnails
"""

from easy_thumbnails.exceptions import InvalidImageFormatError
from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.source_generators import pil_image

from .base import ImageBackend


class EasyThumbnailsBackend(ImageBackend):
    exceptions_to_catch = (InvalidImageFormatError, IOError)

    def get_thumbnail_url(self, image_path, thumbnail_options):
        thumbnailer = get_thumbnailer(image_path)
        thumbnailer.thumbnail_storage = thumbnailer.source_storage # use the same storage for thumbnails
        return thumbnailer.get_thumbnail(thumbnail_options).url

    def get_size(self, image):
        return pil_image(image).size
