from pytest import fixture

from service.gamer import Gamer

@fixture(scope='session', autouse=True)
def gamer():
    yield Gamer('Ivan', 'human')
    print("Чистить ресурсы не нужно, но мы можем, если надо")