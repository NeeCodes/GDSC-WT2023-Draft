import pandas as pd

subjects=[[["A1", "L31"],
              ["B1", "L33"],
              ["C1", "L35"]],

              [["D1", "L37"], 
              ["F1", "L31"],
              ["G1", "L33"]],

              [["A1", "L39"],
              ["D1", "L37"],
            ["G1", "L50"]]]

totalsubs=len(subjects)
def totaltimetables(totalsubs):#n is length of list where all subjects are stored
    labslots=set()
    theoryslots=set()
    onetimetable=[]

    timetables=[]

    def backtrack(subjectpriority):#r is the current index of the list
        if subjectpriority==totalsubs+1:
            copy1=onetimetable.copy()
            timetables.append(copy1)

            return True
        
        
        for teacherpriority in range(1,4):
            
            if subjects[subjectpriority-1][teacherpriority-1][1]in labslots or subjects[subjectpriority-1][teacherpriority-1][0] in theoryslots:
                continue

            labslots.add(subjects[subjectpriority-1][teacherpriority-1][1])
            theoryslots.add(subjects[subjectpriority-1][teacherpriority-1][0])
            onetimetable.append(teacherpriority)

            backtrack(subjectpriority+1)

            #if solution doesnt exist

            labslots.remove(subjects[subjectpriority-1][teacherpriority-1][1])
            theoryslots.remove(subjects[subjectpriority-1][teacherpriority-1][0])
            onetimetable.remove(teacherpriority)

    backtrack(1)
    return timetables
        
print(totaltimetables(totalsubs))

                

 