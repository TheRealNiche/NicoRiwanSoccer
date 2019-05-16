import soccersimulator
from soccersimulator import Vector2D



def compute_move(positionjoueur, vectjoueur, turfu):
    vect = turfu - positionjoueur
    vect.normalize()
    return  vect

def compute_shoot(positionjoueur, turfu, strength):
    vect = turfu - positionjoueur
    return vect