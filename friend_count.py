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
    words = value.split()

    for w in words:
        mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):

    total = 0

    # Add new names to the list.
    for v in list_of_values:
        total += v

    # Emit the result.
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
