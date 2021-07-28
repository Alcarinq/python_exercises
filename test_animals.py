from unittest import TestCase
from Animal import Animal


class TestAnimal(TestCase):
    def setUp(self):
        self.animal = Animal('crocodile', 18)

    def test_animal_creating(self):
        test_animal = Animal('crocodile', 18)
        self.assertEqual(self.animal.__dict__, test_animal.__dict__)

    def test_animal_hungry(self):
        self.assertTrue(self.animal.is_food_needed())

    def test_animal_feed(self):
        self.animal.feed_animal()
        self.assertFalse(self.animal.is_food_needed())