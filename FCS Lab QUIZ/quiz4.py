"""
In this lab, you will be given a set of processes with their arrival times and burst times. Your task is to
implement the Non Preemtive SJF scheduling algorithm to schedule these processes and calculate the Gantt
chart, completion time (CT), turnaround time (TAT), waiting time (WT), average waiting time (AWT), and
average turnaround time (ATAT). [10 points]

-:Sample Input [2]:-
Number of processes: 5
Process Arrival Time Burst Time
1 1 7
2 2 5
3 3 1
4 4 2
5 5 8
-:Sample Output [2]:-
Gantt Chart:
| - | 1 | 3 | 4 | 2 | 5 |
0 1 8 9 11 16 24
Process | CT | TAT | WT
1 | 8 | 7 | 0
2 | 16 | 14 | 9
3 | 9 | 6 | 5
4 | 11 | 7 | 5
5 | 24 | 19 | 11
Average Turnaround Time (ATAT): 10.6
Average Waiting Time (AWT): 6


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
    print(gnattChart)
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
