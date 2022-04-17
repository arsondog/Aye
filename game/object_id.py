import pygame
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton

from game.clientexe import manager

...  # other code ommitted here -
# see quick start guide for how to get up and running with a single button

hello_button = UIButton(relative_rect=pygame.Rect((350, 280), (-1, -1)),
                        text='Hello',
                        manager=manager,
                        object_id=ObjectID(class_id='@friendly_buttons',
                                           object_id='#hello_button'))
