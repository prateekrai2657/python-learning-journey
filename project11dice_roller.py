import random

# print("\u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518" )
# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dic_art = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘",),
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│      ●  │",
       "└─────────┘",),
    3:("┌─────────┐",
       "│ ●       │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘",),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘",),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘",),
    6:("┌─────────┐",
       "│ ●    ●  │",
       "│ ●    ●  │",
       "│ ●    ●  │",
       "└─────────┘",),
}
dice =[]
total = 0
num_of_dice= int(input("how many dice?:  "))

for die in range(num_of_dice):
     dice.append(random.randint(1,6))

for die in range(num_of_dice):
    for line in dic_art.get(dice[die]):
        print(line)
for die in dice:
    total +=die
print(f"total:{total}")


    
    



 