# In this lab, you will be given a set of processes with their arrival times and burst times. Your task is to
# implement the Non Preemtive SJF scheduling algorithm to schedule these processes and calculate the Gantt
# chart, completion time (CT), turnaround time (TAT), waiting time (WT), average waiting time (AWT), and
# average turnaround time (ATAT).


from collections import OrderedDict

# Process class with attributes
class Process:
    def __init__(self, ProcessID, arrivalTime, burstTime, isTerminated, startTime, endTime, turnAroundTime, waitingTime):
        self.ProcessID = ProcessID
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.isTerminated = isTerminated
        self.startTime = startTime
        self.endTime = endTime
        self.turnAroundTime = turnAroundTime
        self.waitingTime = waitingTime

    def __repr__(self):
        return str(self)


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
try:
    noOfProcesses = int(val)
    if noOfProcesses <= 0:
        raise ValueError
except ValueError:
    raise Exception("Invalid input: total number of processes")

processList = []

for i in range(noOfProcesses):
    process_id, arrival_time, burst_time = input(f"Enter process {i + 1} details (ID ArrivalTime BurstTime): ").split()
    processList.append(Process(process_id, int(arrival_time), int(burst_time), False, 0, 0, 0, 0))

# sort the list on arrival time
sortedList = sorted(processList, key=lambda l: l.arrivalTime, reverse=False)
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
        gnattChart[p.ProcessID] = p.startTime
        notInitialized = False

    gnattChart[p.ProcessID] = p.endTime
    lastEndTime = p.endTime

print("Gnatt Chart")
# print(gnattChart)
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
    print("     " + p.ProcessID + " | " + str(p.endTime) + " | " + str(p.turnAroundTime) + " | " + str(p.waitingTime))
    totalTurnArTime = totalTurnArTime + p.turnAroundTime
    totalWaitingTime = totalWaitingTime + p.waitingTime

print("Average Turnaround Time (ATAT): " + "%.2f" % (totalTurnArTime / noOfProcesses))
print("Average Waiting Time (AWT): " + "%.2f" % (totalWaitingTime / noOfProcesses))
print("Throughput: " + "%.3f" % (noOfProcesses / (int(sortedList[len(sortedList) - 1].endTime) - int(sortedList[0].startTime))))


