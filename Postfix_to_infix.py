# Chris Courville
# Mod2 Day 3
# Example problem 3


from Stack import Stack
from Queue import Queue


def p2i(q):
    s = Stack([])
    while not q.is_empty():
        curr = q.deq()
        if curr.isdigit():
            s.push(curr)
        else:
            op2 = s.pop()
            op1 = s.pop()
            s.push(f"({op1}{curr}{op2})")
    return s.pop()


q = Queue()
q.enq("2")
q.enq("3")
q.enq("*")
q.enq("8")
q.enq("5")
q.enq("*")
q.enq("/")


print(p2i(q))