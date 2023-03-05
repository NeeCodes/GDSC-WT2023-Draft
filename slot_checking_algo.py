from collections import deque

subjects = deque([{1 : ["A1", "L31"],
              2 : ["B1", "L33"],
              3 : ["C1", "L35"]},

              {1 : ["D1", "L37"], 
              2 : ["F1", "L31"],
              3 : ["G1", "L33"]},

              {1 : ["A1", "L39"],
              2 : ["D1", "L37"],
              3 : ["G1", "L5"]}])

valid_timetables = list()

def print_tt():
    # print("subjects left = ", subjects)

    print(*(theory_slots.items()), sep="\n")
    print()
    print(*(lab_slots.items()), sep="\n")
    print("\n\n")

theory_slots = {"A1" : 0,
                "B1" : 0,
                "C1" : 0,
                "D1" : 0,
                "E1" : 0,
                "F1" : 0,
                "G1" : 0}

lab_slots = {"L31" : 0,
            "L33" : 0,
            "L35" : 0,
            "L37" : 0,
            "L39" : 0}

def valid():
    if(subjects):
        return False
    
    return True


def allocate():
    if valid():
        # valid_timetables.append(timetable)
        print_tt()
        return True
    
    while(subjects):
        subject = subjects[0]


        for teacher, slots in subject.items():
            if theory_slots[slots[0]] == 0 and lab_slots[slots[1]] == 0:
                theory_slots[slots[0]] = (teacher)
                lab_slots[slots[1]] = (teacher)

                print_tt()

                subjects.popleft()

                if allocate():
                    print("allocated!")
                    return True
                
                theory_slots[slots[0]] = 0
                lab_slots[slots[1]] = 0
                subjects.appendleft(subject)
                



    return False


allocate()

