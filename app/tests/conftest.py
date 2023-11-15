from pytest import fixture

from service.gamer import Gamer

@fixture(scope='session')
def gamer():
    return Gamer('Ivan', 'human')