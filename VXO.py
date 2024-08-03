# Copyright (c) VXO 
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Settings.Program.Config.Config import *
from Settings.Program.Config.Util import *

try:
   import webbrowser
   import re
   import colorama
except:
   ErrorModule()

colorama.init()

try:
   content = requests.get(url_config).text
   match = re.search(r'version_tool\s*=\s*"([^"]+)"', content)
   current_version = match.group(1)
   if current_version != version_tool:
      print(f"{INFO} Please download the new version of the tool ! {white}{version_tool}{color.LIGHTYELLOW_EX} -> {white}{current_version}{blue}")
      webbrowser.open(github_tool)
      input(f"{INFO} Enter to still use this version -> {reset}")
      popup_version = f"{color.LIGHTYELLOW_EX}Please update the tool: {white}{version_tool}{color.LIGHTYELLOW_EX} -> {white}{current_version}{blue}"
   else:
      popup_version = ""
except:
   popup_version = ""

option_01 = "Tool-Info"
option_02 = "Tool-Website"
option_03 = "Obfuscator-Tool-(Paid)"
option_04 = "Virus-Build-(Stealer,-Malware)"
option_05 = "Sql-Vulnerability"
option_06 = "Phishing-Attack"
option_07 = "Website-Info-Scanner"
option_08 = "Website-Url-Scanner"
option_09 = "Dark-Web-Links"
option_10 = "Search-In-DataBase"
option_11 = "Dox-Create"
option_12 = "Dox-Tracker-(Osint)"
option_13 = "Username-Tracker-(Osint)"
option_14 = "Email-Tracker-(Osint)"
option_15 = "Email-Info-(Lookup)"
option_16 = "Number-Info-(Lookup)"
option_17 = "Ip-Info-(Lookup)"
option_18 = "Ip-Port-Scanner"
option_19 = "Ip-Pinger"
option_20 = "Ip-Generator"
option_21 = "Password-Encrypted"
option_22 = "Password-Decrypted"
option_23 = "Get-Your-Ip"
option_24 = "Discord-Token-Info"
option_25 = "Discord-Token-Nuker"
option_26 = "Discord-Token-Joiner"
option_27 = "Discord-Token-Leaver"
option_28 = "Discord-Token-Login"
option_29 = "Discord-Token-To-Id-And-Brute"
option_32 = "Discord-Token-Server-Raid"
option_33 = "Discord-Token-Spammer"
option_34 = "Discord-Token-Delete-Friends"
option_35 = "Discord-Token-Block-Friends"
option_36 = "Discord-Token-Mass-Dm"
option_37 = "Discord-Token-Delete-Dm"
option_38 = "Discord-Token-Status-Changer"
option_39 = "Discord-Token-Language-Changer"
option_40 = "Discord-Token-House-Changer"
option_41 = "Discord-Token-Theme-Changer"
option_42 = "Discord-Token-Generator"
option_43 = "Discord-Bot-Server-Nuker"
option_44 = "Discord-Bot-Invite-To-Id"
option_45 = "Discord-Server-Info"
option_46 = "Discord-Nitro-Generator"
option_47 = "Discord-Webhook-Info"
option_48 = "Discord-Webhook-Delete"
option_49 = "Discord-Webhook-Spammer"
option_50 = "Discord-Webhook-Generator"
option_51 = "Roblox-Cookie-Login"
option_52 = "Roblox-Cookie-Info"
option_53 = "Roblox-User-Info"
option_54 = "Roblox-Id-Info"
option_55 = "Soon"
option_56 = "Soon"
option_57 = "Soon"
option_58 = "Soon"
option_59 = "Soon"
option_60 = "Soon"
option_61 = "Soon" 
option_62 = "Soon"
option_63 = "Soon"
option_64 = "Soon"
option_65 = "Soon"
option_66 = "Soon"
option_67 = "Soon"
option_68 = "Soon"
option_69 = "Soon"

option_next = "Next Page >>"
option_previous = "<< Previous Page"

option_01_txt = option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = option_05.ljust(30)[:30].replace("-", " ")
option_06_txt = option_06.ljust(30)[:30].replace("-", " ")
option_07_txt = option_07.ljust(30)[:30].replace("-", " ")
option_08_txt = option_08.ljust(30)[:30].replace("-", " ")
option_09_txt = option_09.ljust(30)[:30].replace("-", " ")
option_10_txt = option_10.ljust(30)[:30].replace("-", " ")
option_11_txt = option_11.ljust(30)[:30].replace("-", " ")
option_12_txt = option_12.ljust(30)[:30].replace("-", " ")
option_13_txt = option_13.ljust(30)[:30].replace("-", " ")
option_14_txt = option_14.ljust(30)[:30].replace("-", " ")
option_15_txt = option_15.ljust(30)[:30].replace("-", " ")
option_16_txt = option_16.ljust(30)[:30].replace("-", " ")
option_17_txt = option_17.ljust(30)[:30].replace("-", " ")
option_18_txt = option_18.ljust(30)[:30].replace("-", " ")
option_19_txt = option_19.ljust(30)[:30].replace("-", " ")
option_20_txt = option_20.ljust(30)[:30].replace("-", " ")
option_21_txt = option_21.ljust(30)[:30].replace("-", " ")
option_22_txt = option_22.ljust(30)[:30].replace("-", " ")
option_23_txt = option_23.ljust(30)[:30].replace("-", " ")
option_24_txt = option_24.ljust(30)[:30].replace("-", " ")
option_25_txt = option_25.ljust(30)[:30].replace("-", " ")
option_26_txt = option_26.ljust(30)[:30].replace("-", " ")
option_27_txt = option_27.ljust(30)[:30].replace("-", " ")
option_28_txt = option_28.ljust(30)[:30].replace("-", " ")
option_29_txt = option_29.ljust(30)[:30].replace("-", " ")

option_32_txt = option_32.ljust(30)[:30].replace("-", " ")
option_33_txt = option_33.ljust(30)[:30].replace("-", " ")
option_34_txt = option_34.ljust(30)[:30].replace("-", " ")
option_35_txt = option_35.ljust(30)[:30].replace("-", " ")
option_36_txt = option_36.ljust(30)[:30].replace("-", " ")
option_37_txt = option_37.ljust(30)[:30].replace("-", " ")
option_38_txt = option_38.ljust(30)[:30].replace("-", " ")
option_39_txt = option_39.ljust(30)[:30].replace("-", " ")
option_40_txt = option_40.ljust(30)[:30].replace("-", " ")
option_41_txt = option_41.ljust(30)[:30].replace("-", " ")
option_42_txt = option_42.ljust(30)[:30].replace("-", " ")
option_43_txt = option_43.ljust(30)[:30].replace("-", " ")
option_44_txt = option_44.ljust(30)[:30].replace("-", " ")
option_45_txt = option_45.ljust(30)[:30].replace("-", " ")
option_46_txt = option_46.ljust(30)[:30].replace("-", " ")
option_47_txt = option_47.ljust(30)[:30].replace("-", " ")
option_48_txt = option_48.ljust(30)[:30].replace("-", " ")
option_49_txt = option_49.ljust(30)[:30].replace("-", " ")
option_50_txt = option_50.ljust(30)[:30].replace("-", " ")
option_51_txt = option_51.ljust(30)[:30].replace("-", " ")
option_52_txt = option_52.ljust(30)[:30].replace("-", " ")
option_53_txt = option_53.ljust(30)[:30].replace("-", " ")
option_54_txt = option_54.ljust(30)[:30].replace("-", " ")
option_55_txt = option_55.ljust(30)[:30].replace("-", " ")
option_56_txt = option_56.ljust(30)[:30].replace("-", " ")
option_57_txt = option_57.ljust(30)[:30].replace("-", " ")
option_58_txt = option_58.ljust(30)[:30].replace("-", " ")
option_59_txt = option_59.ljust(30)[:30].replace("-", " ")
option_60_txt = option_60.ljust(30)[:30].replace("-", " ")
option_61_txt = option_61.ljust(30)[:30].replace("-", " ")
option_62_txt = option_62.ljust(30)[:30].replace("-", " ")
option_63_txt = option_63.ljust(30)[:30].replace("-", " ")
option_64_txt = option_64.ljust(30)[:30].replace("-", " ")
option_65_txt = option_65.ljust(30)[:30].replace("-", " ")
option_66_txt = option_66.ljust(30)[:30].replace("-", " ")
option_67_txt = option_67.ljust(30)[:30].replace("-", " ")
option_68_txt = option_68.ljust(30)[:30].replace("-", " ")
option_69_txt = option_69.ljust(30)[:30].replace("-", " ")

option_previous_txt = option_previous.ljust(30)[:30]
option_next_txt = option_next.ljust(30)[:30]

menu1 = f"""{white}[{blue}Menu n°1{white}]
   {white}[{blue}01{white}] {blue}->{white} {option_01_txt} {white}[{blue}11{white}] {blue}->{white} {option_11_txt} {white}[{blue}21{white}] {blue}->{white} {option_21_txt}
   {white}[{blue}02{white}] {blue}->{white} {option_02_txt} {white}[{blue}12{white}] {blue}->{white} {option_12_txt} {white}[{blue}22{white}] {blue}->{white} {option_22_txt}
   {white}[{blue}03{white}] {blue}->{white} {option_03_txt} {white}[{blue}13{white}] {blue}->{white} {option_13_txt} {white}[{blue}23{white}] {blue}->{white} {option_23_txt}
   {white}[{blue}04{white}] {blue}->{white} {option_04_txt} {white}[{blue}14{white}] {blue}->{white} {option_14_txt} {white}[{blue}24{white}] {blue}->{white} {option_24_txt}
   {white}[{blue}05{white}] {blue}->{white} {option_05_txt} {white}[{blue}15{white}] {blue}->{white} {option_15_txt} {white}[{blue}25{white}] {blue}->{white} {option_25_txt}
   {white}[{blue}06{white}] {blue}->{white} {option_06_txt} {white}[{blue}16{white}] {blue}->{white} {option_16_txt} {white}[{blue}26{white}] {blue}->{white} {option_26_txt}
   {white}[{blue}07{white}] {blue}->{white} {option_07_txt} {white}[{blue}17{white}] {blue}->{white} {option_17_txt} {white}[{blue}27{white}] {blue}->{white} {option_27_txt}
   {white}[{blue}08{white}] {blue}->{white} {option_08_txt} {white}[{blue}18{white}] {blue}->{white} {option_18_txt} {white}[{blue}28{white}] {blue}->{white} {option_28_txt}
   {white}[{blue}09{white}] {blue}->{white} {option_09_txt} {white}[{blue}19{white}] {blue}->{white} {option_19_txt} {white}[{blue}29{white}] {blue}->{white} {option_29_txt}
   {white}[{blue}10{white}] {blue}->{white} {option_10_txt} {white}[{blue}20{white}] {blue}->{white} {option_20_txt} {white}[{blue}30{white}] {blue}-> {option_next_txt}

{blue}┌───({white}{username_pc}@vxotools{blue})─[{white}~/vxotools/Menu-1{blue}]""".replace("(Osint)", f"{blue}(Osint){white}").replace("(Lookup)", f"{blue}(Lookup){white}").replace("(Stealer, Malware)", f"{blue}(Stealer, Malware){white}").replace("(Paid)", f"{blue}(Paid){white}")

menu2 = f"""{white}[{blue}Menu n°2{white}]
   {white}[{blue}31{white}] {blue}-> {option_previous_txt} {white}[{blue}41{white}] {blue}->{white} {option_41_txt} {white}[{blue}51{white}] {blue}->{white} {option_51_txt}
   {white}[{blue}32{white}] {blue}->{white} {option_32_txt} {white}[{blue}42{white}] {blue}->{white} {option_42_txt} {white}[{blue}52{white}] {blue}->{white} {option_52_txt}
   {white}[{blue}33{white}] {blue}->{white} {option_33_txt} {white}[{blue}43{white}] {blue}->{white} {option_43_txt} {white}[{blue}53{white}] {blue}->{white} {option_53_txt}
   {white}[{blue}34{white}] {blue}->{white} {option_34_txt} {white}[{blue}44{white}] {blue}->{white} {option_44_txt} {white}[{blue}54{white}] {blue}->{white} {option_54_txt}
   {white}[{blue}35{white}] {blue}->{white} {option_35_txt} {white}[{blue}45{white}] {blue}->{white} {option_45_txt} {white}[{blue}55{white}] {blue}->{white} {option_55_txt}
   {white}[{blue}36{white}] {blue}->{white} {option_36_txt} {white}[{blue}46{white}] {blue}->{white} {option_46_txt} {white}[{blue}56{white}] {blue}->{white} {option_56_txt}
   {white}[{blue}37{white}] {blue}->{white} {option_37_txt} {white}[{blue}47{white}] {blue}->{white} {option_47_txt} {white}[{blue}57{white}] {blue}->{white} {option_57_txt}
   {white}[{blue}38{white}] {blue}->{white} {option_38_txt} {white}[{blue}48{white}] {blue}->{white} {option_48_txt} {white}[{blue}58{white}] {blue}->{white} {option_58_txt}
   {white}[{blue}39{white}] {blue}->{white} {option_39_txt} {white}[{blue}49{white}] {blue}->{white} {option_49_txt} {white}[{blue}59{white}] {blue}->{white} {option_59_txt}
   {white}[{blue}40{white}] {blue}->{white} {option_40_txt} {white}[{blue}50{white}] {blue}->{white} {option_50_txt} {white}[{blue}60{white}] {blue}-> {option_next_txt}

{blue}┌───({white}{username_pc}@vxotools{blue})─[{white}~/vxotools/Menu-2{blue}]""".replace("(Osint)", f"{blue}(Osint){white}").replace("(Lookup)", f"{blue}(Lookup){white}").replace("(Stealer, Malware)", f"{blue}(Stealer, Malware){white}").replace("(Paid)", f"{blue}(Paid){white}")

def Menu():
   try:
      with open("./Settings/Program/Config/Menu.txt", "r") as file:
         menu = file.read()
      if menu in ["1"]:
         menu = menu1
         Title("Menu 1")
      elif menu in ["2"]:
         menu = menu2
         Title("Menu 2")
      else:
         menu = menu1
         Title("Menu 1")
   except:
      menu = menu1
      Title("Menu 1")

   banner = f"""{popup_version}{blue}                                                                                                  
                              



                     ██▒   █▓▒██   ██▒ ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
                    ▓██░   █▒▒▒ █ █ ▒░▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
                     ▓██  █▒░░░  █   ░▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
                      ▒██ █░░ ░ █ █ ▒ ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
                       ▒▀█░  ▒██▒ ▒██▒░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
                       ░ ▐░  ▒▒ ░ ░▓ ░░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
                       ░ ░░  ░░   ░▒ ░  ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
                         ░░   ░    ░  ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
                          ░   ░    ░      ░ ░                  ░ ░      ░ ░      ░  ░      ░  
                         ░                                                                    
                            
                              
                                                     {white}╔════════════╗
                                                     {white}║ {blue}Multi-Tool{white} ║
                                                     {white}╚════════════╝
   {menu}"""
   return banner


while True:
   try:
      Clear()
      Slow(Menu())
      choice = input(f"""└──{white}$ {reset}""")

      options = {
         '1': option_01, '2': option_02, '3': option_03, '4': option_04,
         '5': option_05, '6': option_06, '7': option_07, '8': option_08,
         '9': option_09, '10': option_10, '11': option_11, '12': option_12,
         '13': option_13, '14': option_14, '15': option_15, '16': option_16,
         '17': option_17, '18': option_18, '19': option_19, '20': option_20,
         '21': option_21, '22': option_22, '23': option_23, '24': option_24,
         '25': option_25, '26': option_26, '27': option_27, '28': option_28,
         '29': option_29, '30': option_next, '31': option_previous, '32': option_32,
         '33': option_33, '34': option_34, '35': option_35, '36': option_36,
         '37': option_37, '38': option_38, '39': option_39, '40': option_40,
         '41': option_41, '42': option_42, '43': option_43, '44': option_44,
         '45': option_45, '46': option_46, '47': option_47, '48': option_48,
         '49': option_49, '50': option_50, '51': option_51, '52': option_52,
         '53': option_53, '54': option_54, '55': option_55, '56': option_56,
         '57': option_57, '58': option_58
      }

      if choice in options:
         if choice in ['30']:
            menu = menu2
            with open("./Settings/Program/Config/Menu.txt", "w") as file:
               file.write("2")
               Title("Menu 2")
         elif choice in ['31']:
            menu = menu1
            with open("./Settings/Program/Config/Menu.txt", "w") as file:
               file.write("1")
               Title("Menu 1")
         else:  
            StartProgram(f"{options[choice]}.py")
      else:
         ErrorChoiceStart()
         
   except Exception as e:
      Error(e)