print('\n\n' + '#' * 36)
print("""
    Welcome! Give me a collection of pitches in positive numerical format
    separated by spaces and I will give you their prime form!
    """)

class Pitch_Class_Set(object):

    def __init__(self, pitches):
        self.pitches = pitches
        self.pitch_classes = sorted(list(set([int(i) % 12 for i in self.pitches.split()])))
    
    def prime_form(self):
        i = 0
        transposed_to_zero = self.pitch_classes
        number_of_sets = len(transposed_to_zero)
        list_of_sets = [[] for y in range(number_of_sets)]

        while i < number_of_sets:
            for z in transposed_to_zero:
                z = (z + 12 - transposed_to_zero[i]) % 12
                list_of_sets[i].append(z)
            i = i + 1

        for i in list_of_sets:
            i.sort()

        sorted(list_of_sets)

        result = ', '.join(str(no) for no in list_of_sets[0])

        print("The prime form is: (" + result + ")!")

        return result

setterino = Pitch_Class_Set(input('> '))

setterino.prime_form()
