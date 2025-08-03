from pishock import PiShockAPI


username = ""   # from pishock.com
api_key = ""    # Enter API key here https://pishock.com/#/account
sharecode = ""  # https://pishock.com/#/control (share button)

def main(intensity, duration):
    dur = duration
    inten = intensity
    api = PiShockAPI(username, api_key)
    shocker = api.shocker(sharecode)
    shocker.shock(duration=dur, intensity=inten)
    return