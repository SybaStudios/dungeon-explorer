import pygame
import pygame.mixer

from app.common import settings
import app.db.music as music_db


pygame.mixer.init()
pygame.mixer.set_num_channels(8)

misc_sfx_channel = pygame.mixer.Channel(1)

pygame.mixer.music.set_volume(settings.get_bgm())

current_bgm = None


def set_bgm(new_bgm: int):
    global current_bgm
    if current_bgm is new_bgm:
        return
    if current_bgm is not None:
        pygame.mixer.music.fadeout(500)
    current_bgm = new_bgm
    if new_bgm is not None:
        pygame.mixer.music.load(music_db.load(new_bgm))
        pygame.mixer.music.play(-1)
