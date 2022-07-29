from unittest import main, TestCase

from project.vehicle import Vehicle


class VehicleTests(TestCase):
    FUEL = 100
    CAPACITY = 100
    HORSE_POWER = 150
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test__init__when_valid_input__expect_valid_class(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test__drive__if_insufficient_fuel_is_required__raise_exception(self):
        test_kilometers = 200
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(test_kilometers)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test__drive__if_sufficient_fuel_is_required__subtract_correct_quantity_from_tank(self):
        test_kilometers = 10
        expected_fuel_quantity = self.FUEL - test_kilometers * self.DEFAULT_FUEL_CONSUMPTION
        self.vehicle.drive(test_kilometers)
        self.assertEqual(expected_fuel_quantity, self.vehicle.fuel)

    def test__drive__if_max_fuel_is_required__fuel_is_empty(self):
        max_distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION
        self.vehicle.drive(max_distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test__refuel__if_too_much_fuel_is_added__raise_exception(self):
        added_quantity = 50
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(added_quantity)
        self.assertEqual("Too much fuel", str(error.exception))

    def test__refuel__if_valid_quantity_is_added__correctly_increases_fuel(self):
        added_quantity = 10
        expected_quantity = self.FUEL - 10 * self.DEFAULT_FUEL_CONSUMPTION + added_quantity
        self.vehicle.drive(10)
        self.vehicle.refuel(added_quantity)
        self.assertEqual(expected_quantity, self.vehicle.fuel)

    def test__str__if_called__returns_correct_str(self):
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        returned_result = str(self.vehicle)
        self.assertEqual(expected_result, returned_result)


if __name__ == '__main__':
    main()
