from basic_bot import Bot

class AdvancedBot(Bot):
    def __init__(self, name, task, battery_level=70):
        super().__init__(name, task)
        self.battery_level = battery_level

    def recharge(self):
        self.battery_level = 100
        return f"{self.name}'s battery recharged to 100%"

    def check_battery(self):
        return f"{self.name}'s battery level is {self.battery_level}%"

if __name__ == "__main__":
    # Create a advanced_cleaning_bot instance
    advanced_bot = AdvancedBot("Vacuum bot", "vacuuming the floor")

    # Perform task and show battery usage
    print(advanced_bot.perform_task())
    print(advanced_bot.check_battery())

    # Recharge the advanced_bot and show battery level
    print(advanced_bot.recharge())
    print(advanced_bot.check_battery())
