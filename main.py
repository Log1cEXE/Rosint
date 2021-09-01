import json

import requests
from colorama import Style, Fore
import os
import shutil
from io import StringIO

class Main:
    def __init__(self):
        os.system("cls && title OsintBlox")

        print(r"  ______             __              __      _______   __                     ")
        print(r" /      \           /  |            /  |    /       \ /  |                    ")
        print(r"/$$$$$$  |  _______ $$/  _______   _$$ |_   $$$$$$$  |$$ |  ______   __    __ ")
        print(r"$$ |  $$ | /       |/  |/       \ / $$   |  $$ |__$$ |$$ | /      \ /  \  /  |")
        print(r"$$ |  $$ |/$$$$$$$/ $$ |$$$$$$$  |$$$$$$/   $$    $$< $$ |/$$$$$$  |$$  \/$$/ ")
        print(r"$$ |  $$ |$$      \ $$ |$$ |  $$ |  $$ | __ $$$$$$$  |$$ |$$ |  $$ | $$  $$<  ")
        print(r"$$ \__$$ | $$$$$$  |$$ |$$ |  $$ |  $$ |/  |$$ |__$$ |$$ |$$ \__$$ | /$$$$  \ ")
        print(r"$$    $$/ /     $$/ $$ |$$ |  $$ |  $$  $$/ $$    $$/ $$ |$$    $$/ /$$/ $$  |")
        print(r" $$$$$$/  $$$$$$$/  $$/ $$/   $$/    $$$$/  $$$$$$$/  $$/  $$$$$$/  $$/   $$/ ")
        print(Fore.RED, Style.DIM + "           OsintBlox | Made by LOG1CEXE :: 0.1" + Style.RESET_ALL)

        self.target_username = input(Fore.CYAN + "\n[+] Enter target's username: " + Style.RESET_ALL)
        self.target_asset_Id = input(Fore.CYAN + "\n\n[+] Enter assetId(you can skip): ")

        self.target_Id = self.GetUserId(self.target_username)['Id']

        print(Fore.YELLOW + f"[+] UserId is: {self.target_Id}")

        self.PickOption()



    def PickOption(self):
        self.ListOfOptions = input('''\n
        1. Get target friends list. 
        2. Download target headshot image.
        3. Get an asset info.
        4. Check if a target has assset (requires asset ID | Works even if the inventory is visible to "No One")
        5. Check if a target can manage an asset.
        6. Block target.
        7. UnBlock target.
        8. Check if target is online.
        
        Select an option: 
        ''')

        if self.ListOfOptions == '1':

            self.GetFriends(self.target_Id)
            self.PickOption()

        elif self.ListOfOptions == '2':

            self.GetAvatarImage(self.target_Id)
            self.PickOption()

        elif self.ListOfOptions == '3':
            self.GetAssetInfo(self.target_asset_Id)

    def GetUserId(self, username):
        self.req = requests.get(f"https://api.roblox.com/users/get-by-username?username={username}")

        return json.loads(self.req.content)

    def GetFriends(self, userId):

        self.req = requests.get(f"https://api.roblox.com/users/{userId}/friends")

        self.friend_list = self.req.content

        print(Fore.YELLOW + f"\n{self.target_username}'s friend list: {self.target_username}friendlist.html")

        with open(f"{self.target_username}'s  friendlist.html",'w') as f:
            f.write(str(self.friend_list))

    def GetAvatarImage(self, userId):

        self.req = requests.get(f"https://www.roblox.com/headshot-thumbnail/json?userId={userId}&width=420&height=420", stream = True)

        self.img = requests.get(json.loads(self.req.content)['Url'])

        with open(f"{self.target_username} Avatar Headshot.jpg", "wb") as f:
            f.write(self.img.content)

    def GetUserExperiences(self, userId):

        self.req = requests.get(f"https://www.roblox.com/users/profile/playergames-json?userId={userId}")

        self.Game_Ids = json.loads(self.req.content)



        with open(f"{self.target_username}'s Experiences.html", "w") as f:

                f.write(str(self.Game_Ids))

    def GetAssetInfo(self, assetId):

        self.req = requests.get(f"https://api.roblox.com/assets/{assetId}/versions")

        print(f"[+] Asset Info: {self.req}")

    def CanManage(self,userId ,assetId):

        self.req = json.loads(requests.get(f"/users/{userId}/canmanage/{assetId}"))['CanManage']

        print(Fore.GREEN + f"[+] Able to manage: {self.req}" + Style.RESET_ALL)

    def BlockUser(self, userId):

        self.req = requests.get(f"https://api.roblox.com/userblock/block?userId={userId}")
        print(Fore.RED + "[+] User Blocked." + Style.RESET_ALL)

    def UnBlockUser(self, userId):

        self.req = requests.get(f"https://api.roblox.com/userblock/unblock?userId={userId}")
        print(Fore.GREEN + "[+] User UnBlocked." + Style.RESET_ALL)

if __name__ == '__main__':
    main = Main()
