
import json
import requests as reqs
 
 

print('''


 _   _            _    _    _ _ _   _    ______                   _     
| | | |          | |  | |  | (_) | | |   | ___ \                 | |    
| |_| | __ _  ___| | _| |  | |_| |_| |__ | |_/ /_ _ _ __ ___  ___| |__  
|  _  |/ _` |/ __| |/ / |/\| | | __| '_ \|  __/ _` | '__/ _ \/ __| '_ \ 
| | | | (_| | (__|   <\  /\  / | |_| | | | | | (_| | | |  __/\__ \ | | |
\_| |_/\__,_|\___|_|\_\\/  \/|_|\__|_| |_\_|  \__,_|_|  \___||___/_| |_|
                                                                        
                                                                        

*****************************************************
  Created By Paresh Maheshwari
  
*****************************************************
              📺 ZEE5 Streamer 😉
⚒ It can Stream The ZEE5 Movies , TV SHows and Series All content
In Online HLS Player !!

*****************************************************

===================================
How to play on desktop

Paste the link.
When you get the button "copy link", click on that.
Open VLC player in your desktop
Press control + N and then paste the link
Press Ok and enjoy your video.

===================================
''')

key = input(' Enter Zee5 Link :')

url = 'http://zee5api.tk/?q=%s' % (key)

response = reqs.get('http://zee5api.tk/?q=%s' % (key))

response_dict = json.loads(response.text)
response.json()


for i in response_dict:
    print(" \n ", i, "val: ", response_dict[i])
    
print('''

Thank For Using This Tool
 
 '''
 )
