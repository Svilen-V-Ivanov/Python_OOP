from project.mammal import Mammal
from unittest import TestCase, main


class MammalTests(TestCase):
    NAME = 'Snow'
    TYPE = 'Cat'
    SOUND = 'Meow'

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.TYPE, self.SOUND)

    def test__init__when_valid__expect_valid_class(self):
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound__when_used__returns_correct_sound(self):
        produced_sound = self.mammal.make_sound()
        expected_sound = f"{self.NAME} makes {self.SOUND}"

        self.assertEqual(expected_sound, produced_sound)

    def test_get_kingdom__when_called__returns_correct_value(self):
        called_value = self.mammal.get_kingdom()
        expected_value = 'animals'

        self.assertEqual(expected_value, called_value)

    def test_get_info__when_called__returns_correct_information(self):
        called_value = self.mammal.info()
        expected_value = f"{self.NAME} is of type {self.TYPE}"

        self.assertEqual(expected_value, called_value)


if __name__ == '__main__':
    main()
