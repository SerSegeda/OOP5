import unittest
from clas import *


class TestAirplaneCreation(unittest.TestCase):
    def test_correct_initialization(self):
        # Перевірка коректного створення базового об'єкта
        plane = Airplane("Airbus A320", 150, 15000.0, 6000.0, 2200.0)
        self.assertEqual(plane.model, "Airbus A320")
        self.assertEqual(plane.capacity, 150)
        self.assertEqual(plane.payload, 15000.0)

    def test_invalid_types(self):
        # Перевірка виклику помилок при некоректних типах даних
        with self.assertRaises(TypeError):
            Airplane(123, 150, 15000, 6000, 2200)  # Модель не є рядком

        with self.assertRaises(ValueError):
            Airplane("Boeing", -5, 15000, 6000, 2200)  # Місткість від'ємна


class TestAirlineOperations(unittest.TestCase):
    def setUp(self):
        # Створення тестового набору даних перед кожним тестом
        self.company = Airline("TestAir")
        self.p_plane = PassengerPlane("Boeing 737", 180, 20000, 5000, 2500, True)
        self.c_plane = CargoPlane("An-124", 8, 120000, 11000, 15000, 2)
        self.m_plane = MilitaryPlane("F-16", 1, 7000, 4000, 1200, "Missiles")

        self.company.add_plane(self.p_plane)
        self.company.add_plane(self.c_plane)
        self.company.add_plane(self.m_plane)

    def test_total_calculations(self):
        # Перевірка підрахунку загальної місткості та вантажопідйомності
        expected_capacity = 180 + 8 + 1
        expected_payload = 20000.0 + 120000.0 + 7000.0

        self.assertEqual(self.company.get_total_capacity(), expected_capacity)
        self.assertEqual(self.company.get_total_payload(), expected_payload)

    def test_sorting_by_range(self):
        # Перевірка сортування за дальністю польоту
        self.company.sort_by_flight_range()
        ranges = [plane.flight_range for plane in self.company.fleet]
        self.assertEqual(ranges, [11000.0, 5000.0, 4000.0])

    def test_finding_by_fuel(self):
        # Перевірка пошуку за діапазоном споживання пального
        result = self.company.find_by_fuel_consumption(1000, 3000)
        self.assertIn(self.p_plane, result)
        self.assertIn(self.m_plane, result)
        self.assertNotIn(self.c_plane, result)


if __name__ == "__main__":
    unittest.main()