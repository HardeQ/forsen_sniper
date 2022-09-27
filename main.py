import discord
import pyautogui
import requests
import json
import os.path
import time
import _thread

pyautogui.PAUSE = 0.01
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

if not os.path.isfile('DATA.ZULOL'):
    f = open('DATA.ZULOL','x')
    f.close()
    f = open('DATA.ZULOL','a')
    f.write("{\n    \"sniper_settings\": [\n    {\n        \"read_me\" : \"WATCH THIS TUTORIAL IF YOU DONT KNOW HOW TO GET DISCORD TOKEN: https://www.youtube.com/watch?v=YEgFvgg7ZPI\",\n        \"read_me_2\" : \"WATCH THIS TUTORIAL IF YOU DONT KNOW HOW TO GET ROOM ID: https://www.youtube.com/watch?v=YjiQ7CajAgg\",\n        \"discord_token\" : \"token\",\n        \"room_id\" : \"placeholder\"\n    }\n    ]\n}")
    f.close()
file = open('DATA.ZULOL')
data = json.load(file)
file.close()

def check_API(code):
    url = "https://ecast.jackboxgames.com/api/v2/rooms/"+code
    f = requests.get(url, headers=HEADERS)
    if f.text[10:14] == "true":
        pyautogui.write(code)

def enter_code(code):
    pyautogui.write(code)
    time.sleep(0.1)
    pyautogui.keyDown('alt')
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.keyUp('alt')
    
checks = [True if (data['sniper_settings'][0]['discord_token'] != 'token') else False, True if (data['sniper_settings'][0]['room_id'] != 'placeholder') else False]

if checks[0] == False:
    print('No token has been provided! Please edit the DATA.ZULOL FILE.')
    time.sleep(4)
    exit(0)
if checks[1] == False:
    print('No RoomID has been provided! Please edit the DATA.ZULOL FILE.')
    time.sleep(4)
    exit(0)
print("Starting...")

print("Pick method:\n   1. Check each code with their API (WORKS ONLY FOR JACKBOX) (Slower, but only requires you to focus on the text input).\n   2. Try every code on jackbox page (Fastest, but requires you to set up)")

decision_pick = input()
if decision_pick == "2":
    print("Open atleast 4 jackbox or wtd pages in different windows. Then press the text input box where you write code (it has to be empty), and press alt+tab to the next window with page. On alt+tab the pages windows need to be first.")


class frozen_sniper(discord.Client):
    async def on_ready(self):
        print("Sniping as:")
        print(self.user)
        print("Ready to snipe!")

    async def on_message(user, message):
        spaces = 0
        letters = 0
        code_arr=["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        code_end = False
        code_arr_iter = 0
        if message.channel.id == int(data['sniper_settings'][0]['room_id']):
            async for message in message.channel.history(limit=1):
                for i in message.content:
                    if code_end == False:
                        if i == " ":
                            spaces += 1
                        else:
                            letters +=1
                            code_arr[code_arr_iter]+=i
                    else:
                        code_end = False
                    if letters == 4:
                        code_end = True
                        letters = 0
                        spaces = 0
                        code_arr_iter+=1
                print(code_arr)
                for i in code_arr:
                    if decision_pick == "1":
                        _thread.start_new_thread(check_API, (i,))
                    else:
                        if len(i) == 4:
                            enter_code(i)
            
client = frozen_sniper()
client.run(data['sniper_settings'][0]['discord_token'], bot=False)
