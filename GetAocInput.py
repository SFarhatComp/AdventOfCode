import requests
SESSION_COOKIE = "sessionCookie"
YEAR = 2024
def get_aoc_input(day, year=YEAR, session_cookie=SESSION_COOKIE):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session_cookie}
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch input: {response.status_code}")
        return None
