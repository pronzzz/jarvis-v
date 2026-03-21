import platform
import psutil

def get_system_info() -> str:
    """Returns basic information about the operating system."""
    system = platform.system()
    release = platform.release()
    return f"I am running on a {system} system, release {release}."

def get_battery_status() -> str:
    """Returns battery percentage if available."""
    battery = psutil.sensors_battery()
    if battery:
        plugged = "Plugged in" if battery.power_plugged else "Running on battery"
        return f"Battery is at {battery.percent}%. Status: {plugged}."
    return "Battery information is not available."
