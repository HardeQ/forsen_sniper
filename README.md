# forsen_sniper

This is a discord code grabber for sniping streamer Sebastian Eli Horse "Forsen" in games like jackbox or wtd where the code is always 4 letters. 

When you first launch the script the settings file will be generated. You have to edit this file in order to make it work. Everything should be explained inside.

Remember that selfbotting is against discord TOS and could get you banned. I don't recommend selfbotting. If you get banned, it's not my fault.

You also need TamperMonkey addon for browser to be able to join lobbies, the script will automatically press "Join".

You also need to install Discord.py version 1.7.3, not the latest one.

You need to also install pyautogui, requests, json, _thread.


<h1>CHANGE YOUR NICKNAME IN THE SCRIPT BELOW IF YOU USE IT FOR "USE YOUR WORDS" GAME!</h1>

```python

pip install pyautogui
pip install requests
pip install json
pip install _thread

```


```javascript
// ==UserScript==
// @name         Jackbox_Play_Automation
// @namespace    http://tampermonkey.net/
// @version      0.4
// @description  Clicks the jackbox join button
// @author       HardeQ
// @match        https://jackbox.tv/
// @match        https://playwtd.com/
// @match        https://wordsgame.lol/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=jackbox.tv
// @grant        none
// ==/UserScript==


(function (){
    function delay(time) {
        return new Promise(resolve => setTimeout(resolve, time));
    }
    this.alert=function() {};
    window.addEventListener('load', function() {
        if (location.href=="https://jackbox.tv/"){
             function jack_click(){

                 if(document.getElementById("button-join") != null && !document.getElementById("button-join").disabled){
                     console.log("ZULUL NO CRASHES MUGAAAA POGGERS");
                     document.getElementById("button-join").click();
                 }
                 setTimeout(function(){jack_click()}, 200);
             }
            jack_click();
        }
        else if (location.href=="https://playwtd.com/"){
            document.getElementById("room").value = "";
            function wtd_click(){
                if(document.getElementById('room').value.length == 4){
                    document.getElementsByClassName("btn")[0].click();
                    document.getElementById("room").value = "";
                }
                setTimeout(function(){wtd_click()}, 200);
            }
            wtd_click();
        }
        else if (location.href=="https://wordsgame.lol/" || location.href=="https://wordsgame.lol/index.html"){
                function uyw_click(){

                    if(document.getElementById('roomcode') && document.getElementById('roomcode').value.length == 4){
                        setTimeout(function(){
                            document.getElementById("connect").click();
                            document.getElementById("roomcode").value = "";
                                                         }, 200);

                    }
                    else if(document.getElementById('name')){
                        setTimeout(
                            function(){
                                       document.getElementById('name').value = "NAME1"; //EDIT THE "NAME1" TO YOUR NICKNAME OR YOURE PEPEJA
                                document.getElementById('join').disabled = false;
                                       document.getElementById('join').click();
                                             }, 100);
                    }
               setTimeout(function(){uyw_click()}, 200);
             }
            delay(200).then(() => uyw_click());
        }

    }, false);
})();
```
