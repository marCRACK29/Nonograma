import pytest
from src.vidas import *

def test_createHealthCounter():
    hp = HP_counter(3)
    assert hp.maxLives == 3
    assert hp.lives == 3


def test_healthCounter():
    hp = HP_counter(4)
    assert hp.lives == hp.maxLives
    hp.loseLife()
    assert hp.lives == 3
    assert hp.alive()
    hp.loseLife()
    hp.loseLife()
    hp.loseLife()
    assert hp.alive()==False


