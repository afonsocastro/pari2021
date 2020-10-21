#!/usr/bin/env python

from objeto import Objeto

if __name__=="__main__":
    vaso=Objeto(32,25,"azul",79)
    vaso.addProp("Afonso")
    vaso.addProp("Ze")
    vaso.addProp("Ze1")
    vaso.addProp("Ze3")
    vaso.addProp("Ze4")
    vaso.addProp("Ze5")

    vaso.remProp("Ze15")

    print vaso