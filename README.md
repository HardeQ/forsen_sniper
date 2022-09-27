# forsen_sniper

This is a discord code grabber for sniping streamer Sebastian Eli Horse "Forsen" in games like jackbox or wtd where the code is always 4 letters. 

When you first launch the script the settings file will be generated. You have to edit this file in order to make it work. Everything should be explained inside.

Remember that selfbotting is against discord TOS and could get you banned. I don't recommend selfbotting. If you get banned, it's not my fault.

You also need TamperMonkey addon for browser to be able to join lobbies, the script will automatically press "Join".

```javascript
// ==UserScript==
// @name         Jackbox_Play_Automation
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  Clicks the jackbox join button
// @author       HardeQ
// @match        https://jackbox.tv/
// @match        https://playwtd.com/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=jackbox.tv
// @grant        none
// ==/UserScript==


(function (){
    window.addEventListener('load', function() {
        if (location.href=="https://jackbox.tv/"){
             function jack_click(){
                 document.getElementById("button-join").click();
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

    }, false);
})();
```
