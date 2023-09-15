# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         FIXME
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# generate & return a queue of binary number strings from 1 to N
# front of queue begins @ '1', returns empty Queue otherwise
def generate_binary_numbers(N):
    if N < 1:
        return Queue()

    numbers = Queue([])
    numbers.enq(1)

    while (N > 1):
        temp = str(numbers.deq())
        temp2 = temp
        print(temp)
        numbers.enq(temp + "0")
        numbers.enq(temp2 + "1")
        N -= 1
    return numbers
    




def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()


# Don't run main on import
if __name__ == "__main__":
    main()
