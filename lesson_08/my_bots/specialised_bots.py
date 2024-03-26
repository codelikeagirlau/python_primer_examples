import basic_bot

vacuum_bot = basic_bot.Bot("Vacuum Bot", "vacuuming the carpet")
maintenance_bot = basic_bot.Bot("Maintenance Bot", "changing light globes")
cooking_bot = basic_bot.Bot("Cooking Bot", "preparing lunch")

print("Tasks in progress ")
print(vacuum_bot.perform_task())
print(maintenance_bot.perform_task())
print(cooking_bot.perform_task())
