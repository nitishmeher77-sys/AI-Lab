# EXP -8 WATER JUG PROBLEM

from collections import deque

# function to slobve water jug problem using
def water_jug(capcity1,capcity2,target):
    visited=set()
    queue=deque()
    # initial state both jugs are empty
    queue.append((0,0,[]))

    while queue:
        jug1,jug2, path =queue.popleft()

        # ski if the state has alredy been
        if (jug1,jug2)in visited:
            continue
        visited.add((jug1,jug2))

        # add current state to the path
        path=path+[(jug1,jug2)]
        # check if target is reached
        if jug1==target or jug2==target:
            return path
        # generate all possible next states
        next_states=[
            # fill jug 1
            (capcity1,jug2),
            # fill jug 2
            (jug1,capcity2),
            # empty jug 1
            (0,jug2),
            # empty jug 2
            (jug1,0),
        ]
            #  pour jug 1 -> jug 2
        transfer_amount = min(jug1, capcity2 - jug2)
        next_states.append((jug1 - transfer_amount, jug2 + transfer_amount))

            # pour jug 2-> jug 1
        transfer_amount = min(jug2, capcity1 - jug1)
        next_states.append((jug1 + transfer_amount, jug2 - transfer_amount))

        # add univisited state to the queue
        for state in next_states:
            if state not in visited:
                queue.append ((state[0],state[1],path))
    # no solution found
    return None
# main progra,
jug1=int(input("enter capacity of jug1:"))
jug2=int(input("enter capacity of jug2:"))
target=int(input("enter traget number"))


solution=water_jug(jug1,jug2,target)
if solution:
    print("\n steps to reach the target:")

    for step in solution:
        print(step)
else:
    print("no solution")

    '''------OUTPUT-----
enter capacity of jug1:4
enter capacity of jug2:3
enter traget number2

 steps to reach the target:
(0, 0)
(0, 3)
(3, 0)
(3, 3)
(4, 2)


  '''