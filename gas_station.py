class GasStation:
    def __init__(self, name, fuel_types):
        self.name = name
        self.fuel_types = fuel_types
        self.tank_qtys = {fuel_type: 1000 for fuel_type in fuel_types}
        # self.tank_qty = 1000
        self.cash = 0
        self.get_types()


    def get_types(self):
        for _type in self.fuel_types:
            setattr(self, str(_type), _type)

    def erogate(self, fuel_type, amount):
        tank = self.tank_qtys[fuel_type]
        erogated = tank - amount
        if erogated >= 0:
            self.tank_qtys[fuel_type] -= amount
            return self.get_payed(fuel_type, amount)

    def pay(self, fuel_type, amount):
        pass

    def refill_tank(self, amount):
        pass

    def get_payed(self, fuel_type, amount):
        transaction = fuel_type.sell_per_litre * amount
        self.cash += transaction
        print(f'{fuel_type} sold for {transaction}')


class Diesel:
    cost_per_litre = 1.20
    sell_per_litre = 1.4

    def __repr__(self):
        return 'diesel'

class Gpl:
    cost_per_litre = 0.20
    sell_per_litre = 1

    def __repr__(self):
        return 'Gas'

class Petrol:
    cost_per_litre = 1.30
    sell_per_litre = 1.5

    def __repr__(self):
        return 'petrol'

if __name__ == '__main__':
    diesel = Diesel()
    petrol = Petrol()
    gas_station = GasStation('Q8', [diesel, petrol])
    # GasStation.erogate(GasStation.diesel, 30)
