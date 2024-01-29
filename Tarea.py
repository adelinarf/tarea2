from typing import *
from enum import Enum


Query = tuple[int, int]
State = tuple[int, int, List[Query]]

SubsetTest = Enum('SubsetTest', ['SUBSETEQ', 'EMPTY_CAP', 'NONEMPTY_CAP'])

def _p(q : Query) -> int:
    return q[0]

def _t(q : Query) -> int:
    return q[1]

def upper_bound(q : Query) -> int:
    return _p(q) + _t(q)

def lower_bound(q : Query) -> int:
    return _p(q)

def st_upper_bound(st : State) -> int:
    return st[1]

def increment(st: State) -> State:
    (count,upper_bound,mem) = st
    return (count + 1, upper_bound,mem)

def st_set_upper_bound(st : State, q : Query) -> State:
    (count,_,mem) = st
    mem.pop()
    mem.append(q)
    return (count, upper_bound(q),mem)

def st_add(st : State, q : Query) -> State:
    (count,_,mem) = st
    mem.append(q)
    return (count + 1, upper_bound(q),mem)

def st_mem(st : State) -> List[Query]:
    return st[2]

def min_state() -> State:
    return (-1,-1,[])

def cap_test(st : State, q: Query) -> SubsetTest:
    if (st_upper_bound(st) >= upper_bound(q)):
        return SubsetTest.SUBSETEQ
    if (lower_bound(q) < st_upper_bound(st)):
        return SubsetTest.EMPTY_CAP
    return SubsetTest.NONEMPTY_CAP

def sol(queries : List[Query]) -> List[Query]:
    st : State = min_state()
    for query in sorted(queries,key=_p):
        
        case_t =  cap_test(st,query)
        #print(f"st: {st}")
        #print(f"query: {query}")
        #print(f"case_t: {case_t}")
        #print(f"=====================")
        if (case_t == SubsetTest.SUBSETEQ):
            st = st_set_upper_bound(st,query)
        elif (case_t == SubsetTest.NONEMPTY_CAP):
            st = st_add(st,query)
            st = increment(st)
    #print(f"st final: {st}")
    return st_mem(st)

def main():
    q1 = [(1,4),(2,1),(3,3)]
    s1 = sol(q1)
    print(f"q1: {q1}")
    print(f"s1: {s1}")
    print("=================") 
    q2 = [(1,9),(2,1),(3,1),(4,46),(5,1),(5,7)]
    s2 = sol(q2)
    print(f"q2: {q2}")
    print(f"s2: {s2}")
    print("=================")
        
if __name__ == "__main__":
    main()
