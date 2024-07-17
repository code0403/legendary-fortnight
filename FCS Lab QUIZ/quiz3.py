"""
In this lab, you will be given a set of processes with their arrival times and burst times. Your task is to
implement the Non-preemptive SJF scheduling algorithm to schedule these processes and calculate the Gantt
chart, completion time (CT), turnaround time (TAT), waiting time (WT), average waiting time (AWT), and
average turnaround time (ATAT). [10 points]

-:Instructions:-
1. Implement the Non-preemptive SJF scheduling algorithm in C/C++/Python. [save as 1.c/cpp/py]
2. Read the input from the user. The input should include the number of processes, their arrival times, and
burst times.
3. Construct a Gantt chart to visualize the execution order of the processes.
4. Calculate the CT, TAT, and WT for each process.
5. Calculate the AWT and ATAT for the set of processes.
6. Print the Gantt chart, CT, TAT, WT, AWT, and ATAT as the output.

-:Sample Input [1] :-
Number of processes: 5
Process Arrival Time Burst Time
P1 3 1
P2 1 4
P3 4 2
P4 0 6
P5 2 3
1.0.3 Sample Output [1]
Gantt Chart:
| P4 | P1 | P3 | P5 | P2 |
0   6    7    9    12   16
Process | CT | TAT | WT
       P1 | 7 | 4 | 3
       P2 | 16 | 15 | 11
       P3 | 9 | 5 | 3
       P4 | 6 | 6 | 0
       P5 | 12 | 10 | 7

Average Turnaround Time (ATAT): 8
Average Waiting Time (AWT): 4.8
Throughput: 0.312


-YS5iaGF0dGFjaGFyamVl

"""

from collections import OrderedDict


# Process class with attributes
class Process:
    def __init__(self, PID, arrivalTime, burstTime, isTerminated, startTime, endTime, turnAroundTime, waitingTime):
        self.PID = PID
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.isTerminated = isTerminated
        self.startTime = startTime
        self.endTime = endTime
        self.turnAroundTime = turnAroundTime
        self.waitingTime = waitingTime

    def __repr__(self):
        return str(self)


# Validate inputs
def validateinput(inp, desc):
    if inp.isnumeric() and int(inp) >= 0:
        return True
    else:
        raise Exception("Invalid input: " + desc)


# This method finds the shortest jobs at a particular point of time considering the arrival time
def findReadyJobs(inpProcesses, timeObj):
    jobs = []
    ifFlag = False
    elseifFlag = False
    currentTimeMakeUpFlag = False
    for d in inpProcesses:
        if not d.isTerminated:
            if int(d.arrivalTime) > timeObj and not currentTimeMakeUpFlag:
                timeObj = timeObj + (int(d.arrivalTime) - timeObj)
                currentTimeMakeUpFlag = True

            if int(d.arrivalTime) <= int(timeObj) and not elseifFlag:
                jobs.append(d)
                currentTimeMakeUpFlag = True
                ifFlag = True
            elif int(d.arrivalTime) > int(timeObj) and not ifFlag:
                if len(jobs) > 0:
                    if jobs[len(jobs) - 1].arrivalTime == d.arrivalTime:
                        jobs.append(d)
                        currentTimeMakeUpFlag = True
                        elseifFlag = True
                else:
                    jobs.append(d)
                    currentTimeMakeUpFlag = True
                    elseifFlag = True

    jobs.sort(key=lambda l: l.burstTime, reverse=False)
    return jobs


# This method implements to 'Shortest Job First' Algorithm
def applySJFAlgorithm(inpProcesses):
    revisedList = []
    currentBTime = 0
    completedProcesses = 0
    while completedProcesses < len(inpProcesses):
        innerList = findReadyJobs(inpProcesses, currentBTime)
        currentBTimeRevision = False
        for pr in innerList:
            if not pr.isTerminated:
                if int(pr.arrivalTime) > currentBTime and not currentBTimeRevision:
                    currentBTime = currentBTime + (int(pr.arrivalTime) - currentBTime)
                    currentBTimeRevision = True

                pr.startTime = currentBTime
                currentBTime = currentBTime + int(pr.burstTime)
                pr.endTime = currentBTime
                pr.waitingTime = int(pr.startTime) - int(pr.arrivalTime)
                pr.turnAroundTime = int(pr.endTime) - int(pr.arrivalTime)
                pr.isTerminated = True
                currentBTimeRevision = True
                revisedList.append(pr)
                completedProcesses = completedProcesses + 1
    return revisedList


# MAIN program starts
val = input("Enter the total number of processes: ")
if val.isnumeric() and int(val) > 0:
    noOfProcesses = int(val)
    processList = []
    for i in range(noOfProcesses):
        pid = "P" + str(i + 1)
        aTime = 0
        bTime = 1
        val = input("Enter the arrival time of process " + str(i + 1) + ": ")
        if validateinput(val, "arrival time of process " + str(i + 1)):
            aTime = val
        val = input("Enter the burst time of process " + str(i + 1) + ": ")
        if validateinput(val, "burst time of process " + str(i + 1)):
            bTime = val
        process = Process(pid, aTime, bTime, False, 0, 0, 0, 0)
        processList.append(process)

    # sort the list on arrival time
    sortedList = sorted(processList, key=lambda l: int(l.arrivalTime), reverse=False)
    sortedList = applySJFAlgorithm(sortedList)

    totalTurnArTime = 0
    totalWaitingTime = 0
    gnattChart = OrderedDict()
    lastEndTime = 0
    notInitialized = True
    for p in sortedList:
        if int(p.startTime) > lastEndTime:
            gnattChart["-"] = int(p.startTime) - lastEndTime

        if notInitialized:
            gnattChart[p.PID] = p.startTime
            notInitialized = False

        gnattChart[p.PID] = p.endTime
        lastEndTime = p.endTime

    print("Gnatt Chart")
    print("| ", end="")
    for k in gnattChart.keys():
        print(k + " | ", end="")
    print("")
    print("0", end="")
    for v in gnattChart.keys():
        print("   " + str(gnattChart.get(v)), end="")

    print("\n-------------------------------------------")
    print("Process | CT | TAT | WT")
    for p in processList:
        print("     " + p.PID + " | " + str(p.endTime) + " | " + str(p.turnAroundTime) + " | " + str(p.waitingTime))
        totalTurnArTime = totalTurnArTime + p.turnAroundTime
        totalWaitingTime = totalWaitingTime + p.waitingTime

    print("Average Turnaround Time (ATAT): " + "%.2f" % (totalTurnArTime / noOfProcesses))
    print("Average Waiting Time (AWT): " + "%.2f" % (totalWaitingTime / noOfProcesses))
    print(
        "Throughput: " + "%.3f" % (
                    noOfProcesses / (int(sortedList[len(sortedList) - 1].endTime) - int(sortedList[0].startTime))))


else:
    raise Exception("Invalid input: total number of processes")
