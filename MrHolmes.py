#!/usr/bin/python3
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2022 Lucksi
# License: GNU General Public License v3.0

from Core.Support import Menu
from Core.Support import Font

class Main:

    def Menu():
        Menu.Main.main()

if __name__ == "__main__":
    try:
       Main.Menu()
    except KeyboardInterrupt:
        print(Font.Color.RED + "\n\n[!]" + Font.Color.WHITE + "LOOKS LIKE YOU HIT 'CTRL-C' EXIT...")
        exit()
    except ModuleNotFoundError as Error:
        print(Font.Color.RED + "\n\n[!]" + Font.Color.WHITE + "INTERNAL ERROR MODULE: {} NOT FOUND".format(str(Error)))
        exit()