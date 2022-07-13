from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if customer not in self.customers and len(self.customers) < 10:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if dvd not in self.dvds and len(self.dvds) < 15:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        return f"{customer.name} has already rented {dvd.name}"
                for dvd in self.dvds:
                    if dvd.id == dvd_id and dvd.is_rented:
                        return "DVD is already rented"
                    if dvd.id == dvd_id and dvd.age_restriction > customer.age:
                        return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                    if dvd.id == dvd_id:
                        customer.rented_dvds.append(dvd)
                        dvd.is_rented = True
                        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        customer.rented_dvds.remove(dvd)
                        for d_v_d in self.dvds:
                            if d_v_d.id == dvd_id:
                                d_v_d.is_rented = False
                        return f"{customer.name} has successfully returned {dvd.name}"
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        string = ''
        for customer in self.customers:
            string += customer.__repr__() + '\n'
        for dvd in self.dvds:
            string += dvd.__repr__() + '\n'

        return string.strip()

