﻿# forsen_sniper

This is a code grabber for sniping streamer Sebastian Eli Horse "Forsen" in games like jackbox or wtd where the code is always 4 letters. 


You also need TamperMonkey addon for browser to be able to join lobbies, the script will automatically press "Join".

```javascript
// ==UserScript==
// @name         Jackbox_Play_Automation
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Clicks the jackbox join button
// @author       HardeQ
// @match        https://jackbox.tv/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=jackbox.tv
// @grant        none
// ==/UserScript==


(function (){
    window.addEventListener('load', function() {
        if (location.href=="https://jackbox.tv/"){
             function jack_click(){
                 document.getElementById("button-join").click();
                 setTimeout(function() {jack_click()}, 200);
             }
            jack_click();
        }

    }, false);
})();
```
