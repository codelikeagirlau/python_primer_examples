class SmartDevice:
  def __init__(self,
               device_name,
               model_number,
               brand,
               screen_size,
               app_list=None):
    self.device_name = device_name
    self.model_number = model_number
    self.brand = brand
    self.screen_size = screen_size
    self.app_list = app_list if app_list is not None else []

  def install_app(self, app_name="Default App"):
    print(f"Preparing to install {app_name}...")
    if app_name in self.app_list:
      print(f"{app_name} is already installed")
      return self.app_list
    else:
      print(f"{app_name} has been installed.")
      self.app_list.append(app_name)
      return self.app_list

  def delete_app(self, app_name):
    print(f"Preparing to delete {app_name}...")
    if app_name in self.app_list:
      self.app_list.remove(app_name)
      print(f"{app_name} has been deleted")
    else:
      print(f"{app_name} is not installed")


# Instances
smartphone = SmartDevice("smartphone", 5000, 'CLG', 5.7)
smartwatch = SmartDevice("smartwatch", 1000, 'CLG', 2)

# Test the install_app method
print("\nInstalling apps...")
smartphone.install_app()  # Should install the default app
smartphone.install_app('Music Player')
smartphone.install_app('Calculator')
smartphone.install_app(
    'Music Player')  # Attempt to install  same app again

# Test the delete_app method
smartphone.delete_app('Music Player')
smartphone.delete_app(
    'Video Player')  # Attempt to delete an app that isn't installed

# Use the function to print app lists for both devices
def print_app_list(device):
    print(f"\nApps installed on {device.device_name}:\n")
    if len(device.app_list) > 0:
        for app in device.app_list:
            print(f"- {app}")
    else:
        print("- No apps found")

print_app_list(smartphone)
print_app_list(smartwatch)
