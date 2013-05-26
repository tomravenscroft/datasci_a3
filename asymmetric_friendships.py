import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[0]
    value = record[1]

    sorted_pair = sorted([key,value])

    mr.emit_intermediate((sorted_pair[0], sorted_pair[1]), value)

def reducer(key, list_of_values):

    #print "K: " + key_list
    #print list_of_values

    friends = []

    # Add new names to the list.
    for v in list_of_values:
        friends += [v]

    if len(friends) == 1:
        mr.emit(key)
        mr.emit((key[1],key[0]))

    #print key
    #print friends
    #print "-----"

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
