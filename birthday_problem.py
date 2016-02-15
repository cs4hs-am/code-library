# -*- coding: utf-8 -*-

# Ծննդյան օրերի խնդիրը - https://en.wikipedia.org/wiki/Birthday_problem
# Youtube-ում - https://www.youtube.com/watch?v=yRv2Zhr15GE

import random # պատահական թվեր գեներացնելու գրադարան

M = 100     # փորձերի (դասարանների) քանակը

def same_day_birthday(N):
    """
    Վերադարձնում է հավանականությունը, որ դասարանի N աշակերտներից
    երկուսը ունեն նույն ծննդյան օրը
    """
    c = 0 # այն դասարանների քանակը, որտեղ այդպիսի զույգ գոյություն ունի
    for classroom in range(M):
        # ցուցակ, որը տրված դասարանի համար պարունակում է աշակերտների ծննդյան օրերը
        # այդ օրերը բնութագրվում են 1..365 թվերով
        birthdays = [random.randint(1, 365) for s in range(N) ]

        for birthday in birthdays:
            if birthdays.count(birthday) > 1: # Եթե այս էլեմենտը հանդիպում է մեկից ավելի անգամ
                c += 1
                break

    return float(c) / M

print same_day_birthday(20)

# գծում ենք գրաֆիկ, որի X առանցքը ցույց է տալիս թե քանի աշակերտ կա դասարանում
# Y առանցքը ցույց է տալիս թե տվյալ N-ի դեպքում որքան է հավանականությունը, որ
# երկու աշակերտ կունենան նույն ծննդյան օրը տարվա մեջ

from visual import *
from visual.graph import *

gdisplay(xtitle='day', ytitle='p')
curve = gcurve(color=color.yellow)

for n in range(1, 366, 1):
    curve.plot(pos=(n, same_day_birthday(n)))

