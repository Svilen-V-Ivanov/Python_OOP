from unittest import main, TestCase

from project.hero import Hero


class HeroTests(TestCase):
    USERNAME = 'John'
    LEVEL = 10
    HEALTH = 100
    DAMAGE = 20
    LEVEL_GAIN = 1
    HEALTH_GAIN = 5
    DAMAGE_GAIN = 5

    def setUp(self) -> None:
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test__init__when_valid_input__creates_valid_class(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test__battle__when_enemy_has_the_same_name_as_hero__raise_exception(self):
        enemy = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)
        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test__battle__when_hero_has_zero_or_less_health__raise_exception(self):
        zero_hero = Hero(self.USERNAME, self.LEVEL, 0, self.DAMAGE)
        enemy = Hero('Peter', self.LEVEL, self.HEALTH, self.DAMAGE)
        with self.assertRaises(ValueError) as error:
            zero_hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test__battle__when_enemy_has_zero_or_less_health__raise_exception(self):
        enemy = Hero('Peter', self.LEVEL, 0, self.DAMAGE)
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(error.exception))

    def test__battle__when_enemy_and_hero_have_zero_or_less_health_after_battle__battle_draws(self):
        enemy = Hero('Peter', self.LEVEL, self.HEALTH, self.DAMAGE)
        expected_hero_health = self.hero.health - enemy.damage * enemy.level
        expected_enemy_health = enemy.health - self.hero.damage * self.hero.level
        expected_result = 'Draw'
        actual_result = self.hero.battle(enemy)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_enemy_health, enemy.health)

    def test__battle__when_enemy_has_zero_or_less_health_after_battle__hero_wins(self):
        enemy = Hero('Peter', 5, self.HEALTH, 10)
        expected_hero_health = self.hero.health - enemy.damage * enemy.level + self.HEALTH_GAIN
        expected_hero_level = self.hero.level + self.LEVEL_GAIN
        expected_hero_damage = self.hero.damage + self.DAMAGE_GAIN
        expected_enemy_health = enemy.health - self.hero.damage * self.hero.level
        expected_result = "You win"
        actual_result = self.hero.battle(enemy)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_enemy_health, enemy.health)
        self.assertEqual(expected_hero_level, self.hero.level)
        self.assertEqual(expected_hero_damage, self.hero.damage)

    def test__battle__when_hero_has_zero_or_less_health_after_battle__enemy_wins(self):
        enemy = Hero('Peter', 10, 300, 30)
        expected_hero_health = self.hero.health - enemy.damage * enemy.level
        expected_enemy_level = enemy.level + self.LEVEL_GAIN
        expected_enemy_damage = enemy.damage + self.DAMAGE_GAIN
        expected_enemy_health = enemy.health - self.hero.damage * self.hero.level + self.HEALTH_GAIN
        expected_result = "You lose"
        actual_result = self.hero.battle(enemy)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_enemy_health, enemy.health)
        self.assertEqual(expected_enemy_level, enemy.level)
        self.assertEqual(expected_enemy_damage, enemy.damage)

    def test_str__when_called__returns_correct_information(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        actual_result = str(self.hero)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()