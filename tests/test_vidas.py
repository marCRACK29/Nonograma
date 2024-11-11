from src.vidas import *

def test_createHealthCounter():
    hp = HP_counter(3,50,(100,200))
    assert hp.maxLives == 3
    assert hp.lives == 3
    assert hp.scale == 50
    assert hp.pos[0] == 100
    assert hp.pos[1] == 200


def test_healthCounter():
    hp = HP_counter(4,30,(50,50))
    assert hp.lives == hp.maxLives
    hp.loseLife()
    assert hp.lives == 3
    assert hp.alive()
    hp.loseLife()
    hp.loseLife()
    hp.loseLife()
    assert hp.alive()==False


