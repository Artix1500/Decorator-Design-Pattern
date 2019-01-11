import abc


class Pizza(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pizza_type(self):
        pass

    @abc.abstractmethod
    def cost(self):
        pass


class ToppingsDecorator(Pizza):
    @abc.abstractmethod
    def pizza_type(self):
        pass


class MakePizza(Pizza):
    def cost(self):
        pass

    def pizza_type(self):
        pass


# PIZZAS
class Margherita(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def cost(self):
        return 12.90

    def pizza_type(self):
        print("Margherita", end='')


class FarmHouse(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def cost(self):
        return 17.90

    def pizza_type(self):
        print("FarmHouse", end='')


# TOPPINGS
class FreshTomato(ToppingsDecorator):
    def __init__(self, pizza):
        self.pizza = pizza

    def cost(self):
        return self.pizza.cost() + 2

    def pizza_type(self):
        self.pizza.pizza_type()
        print(" fresh tomato", end='')


class ExtraCheese(ToppingsDecorator):
    def __init__(self, pizza):
        self.pizza = pizza

    def cost(self):
        return self.pizza.cost() + 2.5

    def pizza_type(self):
        self.pizza.pizza_type()
        print(" extra cheese", end='')


class Mushrooms(ToppingsDecorator):
    def __init__(self, pizza):
        self.pizza = pizza

    def cost(self):
        return self.pizza.cost() + 4

    def pizza_type(self):
        self.pizza.pizza_type()
        print(" mushrooms", end='')




def main():
    margherita = Margherita(MakePizza())
    margherita = FreshTomato(margherita)
    margherita.pizza_type()
    print("\nPrice: {}".format(margherita.cost()))

    farm_house = FarmHouse(MakePizza())
    farm_house = FreshTomato(farm_house)
    farm_house = ExtraCheese(farm_house)
    farm_house = Mushrooms(farm_house)
    farm_house.pizza_type()
    print("\nPrice: {}".format(farm_house.cost()))


if __name__ == "__main__":
    main()
