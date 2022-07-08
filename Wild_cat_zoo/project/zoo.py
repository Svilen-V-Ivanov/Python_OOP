from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        #It can also be: salaries = sum(w.salary for w in self.workers)
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if salaries <= self.__budget:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        # It can also be: care_money = sum(w.money_for_care for w in self.animals)
        care_money = 0
        for animal in self.animals:
            care_money += animal.money_for_care
        if care_money <= self.__budget:
            self.__budget -= care_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        string = ''
        string += f"You have {len(self.animals)} animals\n"

        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        string += f'----- {len(lions)} Lions:\n' + '\n'.join(lions) + '\n'

        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        string += f'----- {len(tigers)} Tigers:\n' + '\n'.join(tigers) + '\n'

        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        string += f'----- {len(cheetahs)} Cheetahs:\n' + '\n'.join(cheetahs)

        return string

    def workers_status(self):
        string = ''
        string += f"You have {len(self.workers)} workers\n"

        keepers = [repr(a) for a in self.workers if isinstance(a, Keeper)]
        string += f'----- {len(keepers)} Keepers:\n' + '\n'.join(keepers) + '\n'

        caretakers = [repr(a) for a in self.workers if isinstance(a, Caretaker)]
        string += f'----- {len(caretakers)} Caretakers:\n' + '\n'.join(caretakers) + '\n'

        vets = [repr(a) for a in self.workers if isinstance(a, Vet)]
        string += f'----- {len(vets)} Vets:\n' + '\n'.join(vets)

        return string



