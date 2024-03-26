from basic_bot import Bot

# Create a Bot instance
delivery_bot = Bot("Deliverer", "delivering packages")
delivery_bot.delivery_address = "123 Python Lane"

# Adding a method dynamically
def deliver_package(self):
    return f"{self.name} delivered a package to {self.delivery_address}"

Bot.deliver_package = deliver_package
print(delivery_bot.deliver_package())
