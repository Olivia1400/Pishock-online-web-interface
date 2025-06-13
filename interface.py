from pishock import PiShockAPI
from app import intensity, duration

username = "OliviaAnders"   # from pishock.com
api_key = "b3375484-fb05-491c-817b-a9a504ced77e"    # https://pishock.com/#/account
sharecode = "1C655979510"  # https://pishock.com/#/control (share button)

def get_values(intensity, duration):
    #! Get the intensity and duration values from the user.
    
    try:
        intensity = int(intensity)
        duration = int(duration)
    except ValueError as e:
        print(f"Error Within app.py sending to interface.py: {e}")
        return None, None
    return intensity, duration


def main(intensity, duration):
    get_values(intensity, duration)
    api = PiShockAPI(username, api_key)
    shocker = api.shocker(sharecode)
    shocker.shock(duration=1, intensity=10)