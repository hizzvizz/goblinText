import random
import math

# initialize string lists
sub = "ₐbcdₑfgₕᵢⱼₖₗₘₙₒₚqᵣₛₜᵤᵥwₓyz"
sup = "ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖqʳˢᵗᵘᵛʷˣʸᶻ"
trx = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25
]

# two lists for the output string and the randomized "coin" flip that
# determines what character to change to subscript or superscript

newst = []
coins = []


# list of letters
al = "abcdefghijklmnopqrstuvwxyz"

# prompt to get string to convert

print("Enter text to be goblinized: ")
print()
vals = input()


# create a random list of numbers 0 -> 2 that control what character
# are changed

for n in range(0, len(vals), 1):
    coins.append(math.floor(random.random() * 3))


# Go through each character and find a matching character in the al list
# based on coin list convert to subscript, superscript, or do nothing

for m in range(0, len(vals), 1):
    if vals[m] == " ":
        newst.append(" ")
    else:
        for n in range(0, len(trx), 1):
            if vals[m] == al[n]:
                if coins[m] == 1:
                    newst.append(sub[trx[n]])
                elif coins[m] == 2:
                    newst.append(sup[trx[n]])
                else:
                    newst.append(vals[m])

# convert the list to a string

newst = "".join(str(x) for x in newst)

# print the output string

print(newst)
