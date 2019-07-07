from pixo import __version__, get_images, find_image


example = 'paper1'


def test_version():
    assert __version__ is not None


def test_get_images():
    images = get_images()

    assert type(images) is list
    assert len(images) >= 1

    for image in images:
        assert 'key' in image

    assert any(i['key'] == example for i in images)


def test_find_image():
    image = find_image(example)

    assert type(image) is dict

    assert 'key' in image
    assert 'tags' in image

    assert image['key'] == example


def test_perform_image():
    assert 1 == 1
