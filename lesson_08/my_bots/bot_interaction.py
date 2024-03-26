from advanced_bot import AdvancedBot

class RepairBot(AdvancedBot):
    def recharge_bot(self, other_bot):
        other_bot.recharge()
        return f"{self.name} recharged {other_bot.name}"

# Assume the Bot and Robot classes are defined as before
repair_bot = RepairBot("Recharging Bot", "repairing")
cleaning_bot = AdvancedBot("Cleaning Bot", "cleaning")  
print(repair_bot.recharge_bot(cleaning_bot))
