from dynaconf import settings


def test_should_recognize_settings():
    world = settings.get('WORLD')
    assert world == 'World'

