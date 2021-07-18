# 16.2.2 mrjob Library

# Enter the following code to import mrjob
from mrjob.job import MRJob

# Create a class called Bacon_count, which inherits, or takes properties, from the MRJob class
class Bacon_count(MRJob):

# Create a mapper()function that will take (self, _, line) as parameters
    def mapper(self, _, line):

# The line parameter will be the line of text taken from the raw input file
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1

# Reducer function takes three parameters: self, key, and values
    def reducer(self, key, values):
        yield key, sum(values)

# Code for running the program:
if __name__ == "__main__":
   Bacon_count.run()