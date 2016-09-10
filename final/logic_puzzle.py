"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop. #
2. The programmer is not Wilkes. #
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. #
4. The writer is not Minsky. #
5. Neither Knuth nor the person who bought the tablet is the manager. #

6. Knuth arrived the day after Simon. #

7. The person who arrived on Thursday is not the designer. #
8. The person who arrived on Friday didn't buy the tablet. #
9. The designer didn't buy the droid. #

10. Knuth arrived the day after the manager. #

11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer. #
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday. #

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""
# item : laptop, droid, tablet, iphone
# day : Wednesday, (day after), Thursday, Friday, Monday
# name : Wilkes, Hamming, Minsky, Knuth, Simon
# job : programmer, person, writer, manager, designer

import itertools

def day_after(f1, f2):
    return f1 + 1 == f2
    
def add_names(t):
    names = ['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']
    return map(lambda x: x[1], sorted(zip(t, names)))


def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    days = Monday, Tuesday, Wednesday, Thursday, Friday = [1,2,3,4,5]
    orderings = list(itertools.permutations(days))
    return add_names(next((Hamming, Knuth, Minsky, Simon, Wilkes)
                for (Hamming, Knuth, Minsky, Simon, Wilkes) in orderings
                if day_after(Simon, Knuth)
                for (programmer, person, writer, manager, designer) in orderings
                if (designer is not Thursday)
                and (manager is not Knuth)
                and (programmer is not Wilkes)
                and (writer is not Minsky)
                and (day_after(manager, Knuth))
                for (laptop, droid, tablet, iphone, _) in orderings
                if ((Wilkes is Monday) or (Wilkes is writer))
                and ((laptop is Monday) or (laptop is writer))
                and (laptop is Wednesday)
                and (tablet is not Friday)
                and ((iphone is Tuesday) or (tablet is Tuesday))
                and (droid is not designer)
                and (tablet is not manager)
                and (((programmer is Wilkes) and (droid is Hamming) ) or ( (programmer is Hamming) and (droid is Wilkes)))
               ))
    
    

def test():
    assert logic_puzzle() == ['Wilkes', 'Simon', 'Knuth', 'Hamming', 'Minsky']
    print "test pass"

test()
