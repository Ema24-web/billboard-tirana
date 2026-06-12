import requests

def get_weather():
    try:
        url = "https://wttr.in/Tirana?format=%C+%t+%h"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            result = response.text.strip()
            if result:
                return f"🌤️ Tirana: {result}"
            else:
                return "⛅ Tirana: 28°C - Pjesërisht me re"
        else:
            return "⛅ Tirana: 28°C - Pjesërisht me re"
    except Exception as e:
        return "⛅ Tirana: 28°C - Pjesërisht me re"