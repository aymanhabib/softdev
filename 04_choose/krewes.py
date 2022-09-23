"""
TNPG: VAT, Vivian Graeber, Ayman Habib, Talia Hsia

DISCO:

QCC:

OPS SUMMARY:

"""
import random
krewes = {2: ["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 8:[aalnasser30  byang30   frafee30  jli31       mmori30    sho30        wli30}
pd_list = [2, 7, 8]
pd = random.choice(pd_list)

name = random.choice(krewes[pd])

print(str(pd) + ' ' + name)

