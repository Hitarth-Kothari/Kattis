import string

line = list(input())
all_c = len(line)
w_c = 0
AL = list(string.ascii_uppercase)
AL_c = 0
al = list(string.ascii_lowercase)
al_c = 0
sym = list(string.punctuation)
sym_c = 0

for x in line:
    if x == '_':
        w_c = w_c + 1
    elif x in AL:
        AL_c = AL_c + 1
    elif x in al:
        al_c = al_c + 1
    else:
        sym_c = sym_c + 1

print(w_c / all_c)
print(al_c / all_c)
print(AL_c / all_c)
print(sym_c / all_c)