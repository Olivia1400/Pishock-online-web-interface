from pishock import PiShockAPI


username = "OliviaAnders"   # from pishock.com
api_key = "b3375484-fb05-491c-817b-a9a504ced77e"    # https://pishock.com/#/account
sharecode = "1C655979510"  # https://pishock.com/#/control (share button)

def main(intensity, duration):
    dur = duration
    inten = intensity
    api = PiShockAPI(username, api_key)
    shocker = api.shocker(sharecode)
    shocker.shock(duration=dur, intensity=inten)
    return