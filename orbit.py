# -*- coding: utf-8 -*-

# Երկու աստղերի շարժումը տարածությունում

# այս գրադարանը թույլ է տալիս ծրագրային եղանակով ստեղծել երկրաչափական օբյեկտներ, մոդելավորել նրանց շարժումները
from visual import *

G = 6.7e-11

giant = sphere(pos=(-1e11,0,0),   # հսկա աստղի սկզբնական դիրքը
               radius=2e10,       # հսկա աստղի շառավիղը
               color=color.red,   # գույնը սիմուլացիայում
               make_trail=True)   # շարժման հետագիծը

giant.mass = 2e30                 # հսկա աստղի զանգվածը
giant.p = vector(0, 0, -1e4) * giant.mass # և իմուլսը

dwarf = sphere(pos=(1.5e11,0,0),  # թզուկ աստղի սկզբական դիրքը
               radius=1e10,       # շառավիղը
               color=color.yellow,# գույնը սիմուլացիայում
               make_trail=True)   # շարժման հետագիծը

dwarf.mass = 1e30       # թզուկ աստղի զանգվածը
dwarf.p = -giant.p      # իմպուլսը

dt = 1e5  # ժամանակի փոփոխությունը

while True:
  # Ստիպում է Python-ին սպասել 1/200վ. ցիկլի յուրաքանչյուր պտույտի ժամանակ
  rate(200)

  # հաշվենք հսկա (giant) աստղի վրա ազդող ուժը
  dist = dwarf.pos - giant.pos  # վեկտոր է
  force = G * giant.mass * dwarf.mass * dist / mag(dist)**3
  
  giant.p = giant.p + force*dt  # ըստ Նյուտոնի երկրորդ օրենքի
  dwarf.p = dwarf.p - force*dt

  for star in [giant, dwarf]:
    star.pos = star.pos + star.p/star.mass * dt # տեղափոխությունը հավասար է արագության և ժամանակի արտադրյալին

# Օրինակը վերցված է VPython-ի պատրաստի օրինակների գրադարանից
# This example is taken from the sample code library of VPython.
