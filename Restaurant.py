class Restaurant:
    open_hour = '8'
    close_hour = '16'

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restarurant(self):
        print(f"Restauracja {self.restaurant_name} serwuje {self.cuisine_type}")

    def open_restarurant(self):
        print(f"Restauracja pracuje w godzinach {self.open_hour}-{self.close_hour}")
