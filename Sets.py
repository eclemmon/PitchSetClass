print('\n\n' + '#' * 36)
print("""
Welcome! Give me a collection of pitches in positive numerical format
separated by spaces and I will give you their prime form!
""")

pitches = input('> ')

list_pitches = [int(i) % 12 for i in pitches.split()]

octave_equiv_pitches = list(set(list_pitches))

######################

octave_equiv_pitches.sort()

###################

print("\n\n" + '#' * 36)

print("Here are your pitches now transposed to 0 and sorted:")

transposed = octave_equiv_pitches

for i in transposed:
    i = i - transposed[0]
    print(i, sep=', ', end=' ', flush = True)

size_transposed = len(transposed)

i = 0

print('\n\n' + '#' * 36)

def SetsToCompare():
    i = 0
    number_of_sets = len(transposed)
    set_set = [[] for y in range(number_of_sets)]
    
    while i < number_of_sets:
        for z in transposed:
            z = (z + 12 - transposed[i]) % 12
            set_set[i].append(z)
        i = i + 1

    for i in set_set:
        i.sort()

    set_set.sort()

    result = ', '.join(str(no) for no in set_set[0])

    print("The prime form is: (" + result + ")!")
    print("The possible rotations transposed to 0 are: " + str(set_set))

SetsToCompare()

