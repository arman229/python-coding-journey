class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        self.number_served=0
    def describe_restaurant(self) -> None:
        print(f'Restaurant Name: {self.restaurant}')
        print(f'Cuisine Type: {self.cuisine}')
    def open_restaurant(self) -> str:
        return f'{self.restaurant} is open'
    def set_number_served(self, number_served: int) -> None:
        self.number_served = number_served

    def increment_number_served(self, increment: int) -> None:
        self.number_served += increment  