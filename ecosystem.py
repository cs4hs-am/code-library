# -*- coding: utf-8 -*-

# Գայլերի և նապաստակների էկոհամակարգի մոդելավորում
# Youtube-ում - https://youtu.be/IjCTvKkz8pI

from visual import *
from visual.graph import *

nRabbits = 100  # Նապաստակների նախնական քանակը
nWolfs   = 100  # Գայլերի նախնական քանակաը

dt = 1          # Ժամանակի միավոր (տվյալ դեպքում մեկ օր)

# Կենդանիների ծնելիության և մահացության գործակիցները
rabbitBirthRate = 0.012
rabbitDeathRate = 0.0001

wolfBirthRate = 0.0001
wolfDeathRate = 0.012

# Մարդու միջամտություն
p = 0.01

nDays = 365 * 10

# Գրաֆների կորերի համար նախատեսված օբյեկտներ
fRabbit = gcurve(color=color.yellow)
fWolf   = gcurve(color=color.red)

allRabbits = 0.0
allWolfs   = 0.0

for day in range(nDays):
    # Մեկ կենդանուն բաժին հասնող փոփոխությունը օրվա ընթացքում
    deltaRabbits = rabbitBirthRate - rabbitDeathRate * nWolfs - p
    deltaWolfs   = wolfBirthRate * nRabbits - wolfDeathRate

    nRabbits += deltaRabbits * nRabbits
    nWolfs   += deltaWolfs * nWolfs

    fRabbit.plot(pos=(day * dt, nRabbits))
    fWolf.plot(pos=(day * dt, nWolfs))

    allRabbits += nRabbits
    allWolfs   += nWolfs

print "Average # of rabbits: ", float(allRabbits) / nDays
print "Average # of wolfs:   ", float(allWolfs)   / nDays
