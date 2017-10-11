print('\n\n' + '#' * 36)
print("""
    Welcome! Give me a collection of pitches in positive numerical format
    separated by spaces and I will give you their prime form!
    """)

class Pitch_Class_Set(object):

    def __init__(self, pitches):
        self.pitches = pitches
        # Identify pitch classes, remove redundant piches, sort and bring into
        # typical range
        self.pitch_classes = sorted(list(set([int(i) % 12 for i in self.pitches.split()])))
        print(self.pitch_classes)
    
    def prime_form(self):
        i = 0
        working_set = self.pitch_classes
        number_of_sets = len(working_set)
        list_of_sets = [[] for y in range(number_of_sets)]
        list_of_invers = [[] for y in range(number_of_sets)]
        #print(list_of_sets, list_of_invers)

        while i < number_of_sets:
            #Create list of sets to compare
            for z in working_set:
                z = (z + 12 - working_set[i]) % 12
                list_of_sets[i].append(z)
            #Create list of inverted sets
            for x in working_set:
                x = (x + 12 - working_set[i]) % 12
                x = abs(x-12) % 12
                list_of_invers[i].append(x)
            #print(list_of_sets)
            i += 1
            #Sort sets
            for n in list_of_sets:
                n.sort()
            for n in list_of_invers:
                n.sort()
                
        #Python does the most left packed set automatically for us.
        l_of_sets_sorted = sorted(list_of_sets + list_of_invers)

        #Tell console the prime form
        result = ', '.join(str(no) for no in l_of_sets_sorted[0])

        print("The prime form is: (" + result + ")!")

        
        self.prime_form_of_set = l_of_sets_sorted[0]

    def interval_vector(self):

        prime_form = self.prime_form_of_set
        interval_vector_init = [0, 0, 0, 0, 0, 0]
        iterate = 0

        while iterate < len(prime_form):

            iterated_pitch_set = prime_form[iterate:]
            n = 0

            for i in iterated_pitch_set:
                
                diff = i - iterated_pitch_set[n]

                if diff == 1 or diff == 11:
                    interval_vector_init[0] += 1
                elif diff == 2 or diff == 10:
                    interval_vector_init[1] += 1
                elif diff == 3 or diff == 9:
                    interval_vector_init[2] += 1
                elif diff == 4 or diff == 8:
                    interval_vector_init[3] += 1
                elif diff == 5 or diff == 7:
                    interval_vector_init[4] += 1
                elif diff == 6:
                    interval_vector_init[5] += 1
                else:
                    pass

            n += 1
            iterate += 1

        interval_vector_result = [str(i) for i in interval_vector_init]
        interval_vector_result = ', '.join(interval_vector_result)

        print('The interval vector is: ' + '<' + interval_vector_result + '>')

    def forte_number_function(self):

        from ForteNumberFinal import forte_number
        prime_form = self.prime_form_of_set

        forte = str(forte_number[tuple(prime_form)][0])

        print('The Forte Number for this set is ' + forte + '.')

                
setterino = Pitch_Class_Set(input('> '))

setterino.prime_form()

setterino.interval_vector()

setterino.forte_number_function()
