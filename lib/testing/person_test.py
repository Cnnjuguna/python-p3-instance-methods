import io
import sys
import types
import pytest
from person import Person


class TestPerson:
    """Person in person.py"""

    def test_is_class(self):
        '''is a class with the name "Person"'''
        guido = Person("Guido")
        assert isinstance(guido, Person)

    def test_is_method(self):
        """is an instance method"""
        guido = Person("Guido")
        assert isinstance(guido.talk, types.MethodType)

    def test_prints_hello_world(self):
        '''prints "Hello World!"'''
        guido = Person("Guido")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        guido.talk()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello World!\n"

    def test_is_method(self):
        """is an instance method"""
        guido = Person("Guido")
        assert isinstance(guido.walk, types.MethodType)

    def test_prints_the_person_is_walking(self):
        '''prints "The person is walking."'''
        guido = Person("Guido")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        guido.walk()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "The person is walking.\n"


if __name__ == "__main__":
    pytest.main()
