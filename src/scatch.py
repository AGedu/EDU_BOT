from Fanpage import fanpage_main
from Focus import focus_main
from LaRepubblica import larepubblica_main
from PuntoInformatico import puntoinformatico_main
from TomsHardware import tomshw_main
from Wired import wired_main
import configparser

def main():
    config = configparser.ConfigParser()
    larepubblica = larepubblica_main()
    focus = focus_main()
    wired= wired_main()
    tomshw = tomshw_main()
    puntoinformatico = puntoinformatico_main()
    fanpage = fanpage_main()
    urls = []
    row = 0
    while len(urls) < 6:
        try:
            urls.append(larepubblica[row][0])
        except:
            continue
        try:
            urls.append(focus[row][0])
        except:
            continue
        try:
            urls.append(wired[row][0])
        except:
            continue
        try:
            urls.append(tomshw[row][0])
        except:
            continue
        try:
            urls.append(puntoinformatico[row][0])
        except:
            continue
        try:
            urls.append(fanpage[row][0])
        except:
            continue
        row += 1
    print(urls)

if __name__ == "__main__":
    main()
