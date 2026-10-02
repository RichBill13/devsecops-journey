from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
# all the available fonts
list_font = figlet.getFonts()

# verification if there's 3 arguments 
if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    font_name = sys.argv[2]

    # check if the font exist
    if font_name in list_font:
        figlet.setFont(font = font_name)
    else:
        print(" the font doesn't exit. try again")
        sys.exit(1)
# verification if there's only one argument
elif len(sys.argv) == 1:
    font1 = choice(list_font)
    figlet.setFont(font = font1)
else:
    sys.exit(1)

x = input("Input: ")
print(figlet.renderText(x))


    
    




