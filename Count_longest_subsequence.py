# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         FIXME
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty
def count_longest(q):

    if q.is_empty():
        return 0

    curr_len = 1  # current and aggregator
    max_len = 1
    prev_char = q.deq()

    while not q.is_empty():
        curr_char = q.deq()

        if curr_char == prev_char:
            curr_len += 1

        else:
            curr_len = 1

        if curr_len > max_len:
            max_len = curr_len

        prev_char = curr_char

    return max_len

def main():
    print("out 2:", count_longest( Queue( [ l for l in "hello" ] ) ))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee"])))


# Don't run main on import
if __name__ == "__main__":
    main()
