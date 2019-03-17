#!/usr/bin/env python3

"""This module provides GUI visualisation."""


from pyglet.window import Window
from pyglet.sprite import Sprite
from pyglet import image, app, clock


def preload_image(img='background.jpg'):
    """
    preload_image   -> preload image.

    Required argument:
        img       -- image's name in res/
    """
    img = image.load('res/' + img)
    return img


class VisualisatorWindow(Window):
    """
    This module is used for executing GUI visualisation.
    """

    def __init__(self, *args, **kwargs):
        """
        Generate some default attribute.
        """

        self.background_image = preload_image()
        self.background_sprite = Sprite(self.background_image)

    def on_draw(self):
        self.clear()
        self.background_sprite.draw()
