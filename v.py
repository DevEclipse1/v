import os
import argparse

parser = argparse.ArgumentParser(
                    prog='V',
                    description='Vi but even worse!'
)

parser.add_argument("filename")

fn = parser.parse_args().filename  

text = None

if os.path.exists(fn):
    text = open(fn).read()
else:
    open(fn,"w")
    text = ""

while True:
    os.system("cls")
    
    for idx, line in enumerate(text.splitlines()):
        print("\033[1;33m" + str(idx) + "\033[1;0m" + f" {line}")

    reading = input("\033[0;32m" + "> ")
    
    # exit
    if reading == ":q":
        break
    
    # save
    if reading == ":s":
        open(fn, "w").write(text)
    
    # newline
    if reading == ":nl":
        text += "\n"
        
    # overwrite
    if reading[:2] == ":o":
        reading = reading[2:].strip()
        if reading:
            try:
                line_number = int(reading)
                for idx, line in enumerate(text.splitlines()):
                    if idx == line_number:
                        print("\033[0;36m")
                        new = input(f"O {idx} ")
                        text = '\n'.join([new if i == idx else line for i, line in enumerate(text.splitlines())])
                        break
            except ValueError:
                pass
        else:
            pass
        
    # help
    if reading == ":h":
        print(":q = quit, :s = save, :nl = new line, :o <int> = overwrite line, :h = show this")
        input("press anything to continue")
                    
    print("\033[0m")
                            
print("Exitting")
os.system("cls")
print("\033[0m")