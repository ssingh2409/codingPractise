# You are given a class MovingAverage that receives a stream of integers. 
# Initialize the object with an integer size, representing the size of a moving window. 
# Implement the next(val) method, which accepts an integer val and returns the moving average of the last size values in the stream (including the current val). 
# If the number of elements seen so far is less than size, compute the average of all elements received so far.
# Return the moving average as a floating point number after each call to next(val).

# Example 1:  {"constructor_args": [3], "operations": ["next", "next", "next"], "arguments": [[1], [10], [3]]}
# [1.0, 5.5, 4.666666666666667]

# Example 2: {"constructor_args": [2], "operations": ["next", "next", "next"], "arguments": [[5], [-1], [7]]}
# [5.0, 2.0, 3.0]

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.sum = 0
        self.internal_array = []

    def next(self, val):
        self.internal_array.append(val)
        self.sum += val 
        if len(self.internal_array) > self.size:
            out = self.internal_array.pop(0)
            self.sum -= out
        print(self.internal_array)
        return self.sum/len(self.internal_array)
    

a = MovingAverage(3)

print(a.next(4))
print(a.next(0))
print(a.next(-4))
print(a.next(8))
print(a.next(12))


