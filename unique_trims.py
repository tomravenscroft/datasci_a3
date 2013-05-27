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

    # Trim 10 nucleotides off end.
    trimmed_val = value[0:len(value)-10]

    mr.emit_intermediate(trimmed_val, key)

def reducer(key, list_of_values):

    # Emit the string if it is unique.
    if len(list_of_values) > 0:
        mr.emit(key)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
