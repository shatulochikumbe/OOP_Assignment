class Gadget:  # Base class for common gadget features
    def __init__(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price
        self.is_on = False  # Default state is off

    def turn_on(self):
        if not self.is_on:
            print(f"{self.brand} {self.model} is turning on...")
            self.is_on = True
        else:
            print(f"{self.brand} {self.model} is already on.")

    def turn_off(self):
        if self.is_on:
            print(f"{self.brand} {self.model} is turning off...")
            self.is_on = False
        else:
            print(f"{self.brand} {self.model} is already off.")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ZMK{self.price}")
        print(f"Status: {'On' if self.is_on else 'Off'}")

class Smartphone(Gadget):  # Inherits from Gadget
    def __init__(self, model, brand, price, operating_system, storage_capacity):
        # Call the parent class's constructor
        super().__init__(model, brand, price)
        self.operating_system = operating_system
        self.storage_capacity = storage_capacity  # in GB
        self.apps = []  # List to store installed apps

    def install_app(self, app_name):
        print(f"Installing {app_name}...")
        self.apps.append(app_name)
        print(f"{app_name} installed successfully.")

    def uninstall_app(self, app_name):
        if app_name in self.apps:
            print(f"Uninstalling {app_name}...")
            self.apps.remove(app_name)
            print(f"{app_name} uninstalled.")
        else:
            print(f"{app_name} is not installed on this phone.")

    def display_info(self):
        # Override parent class display_info to add Smartphone specific info
        super().display_info()  # Call the parent's method first
        print(f"Operating System: {self.operating_system}")
        print(f"Storage: {self.storage_capacity} GB")
        print(f"Installed Apps: {', '.join(self.apps) or 'None'}")  #Nicely prints the list of apps.


# Example usage:
my_phone = Smartphone("Galaxy S23", "Samsung", 21699, "Android", 256)
my_phone.display_info()
print("\n")
my_phone.turn_on()
my_phone.install_app("WhatsApp")
my_phone.install_app("Instagram")
my_phone.display_info()
print("\n")
my_phone.uninstall_app("Instagram")
my_phone.display_info()
print("\n")
my_phone.turn_off()