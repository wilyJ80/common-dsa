import pytest
from main import Editor


@pytest.fixture
def editor():
    return Editor('edits.txt')


def test_add(editor):
    editor.text = 'foo'
    editor.add('bar')
    assert editor.text == 'foobar'


def test_replace(editor):
    editor.text = 'foo'
    editor.replace(2, 'foob')
    assert editor.text == 'ffoob'


def test_delete(editor):
    editor.text = 'foobar'
    editor.delete(2)
    assert editor.text == 'foob'


def test_undo(editor):
    editor.text = 'foobar'
    editor.add('something')
    editor.add('else')
    editor.add('andmore')

    editor.undo()
    assert editor.text == 'foobarsomethingelse'

    editor.undo()
    assert editor.text == 'foobarsomething'

    editor.undo()
    assert editor.text == ''

    def test_redo(editor):
        editor.text = 'foobar'
        editor.add('something')
        editor.add('else')
        editor.add('andmore')

        editor.undo()
        assert editor.text == 'foobarsomethingelseandmore'

        editor.undo()
        editor.undo()
        assert editor.text == 'foobarsomething'

    def test_clean(editor):
        editor.text = 'foobar'
        editor.clean()
        assert editor.text == ''
