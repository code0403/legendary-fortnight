class Process:
    def __init__(self, pid, arrivalTime, burstTime):
        self.pid = pid
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.burstTimeRemaining = burstTime
        self.completionTime = 0
        self.turnaroundTime = 0
        self.waitingTime = 0
        self.inQueue = False

def check_for_new_arrivals(processes, n, current_time, ready_queue):
    for i in range(n):
        p = processes[i]
        if p.arrivalTime <= current_time and not p.inQueue and p.burstTimeRemaining > 0:
            processes[i].inQueue = True
            ready_queue.append(i)

def update_queue(processes, n, quantum, ready_queue, current_time):
    if len(ready_queue) == 0:
        return None
    
    pid = ready_queue.pop(0)
    p = processes[pid]

    if p.burstTimeRemaining <= quantum:
        current_time += p.burstTimeRemaining
        p.burstTimeRemaining = 0
        p.completionTime = current_time
    else:
        current_time += quantum
        p.burstTimeRemaining -= quantum
        ready_queue.append(pid)

    return pid, current_time

def round_robin(processes, n, quantum):
    ready_queue = []
    current_time = 0
    gantt_chart = []

    while True:
        check_for_new_arrivals(processes, n, current_time, ready_queue)
        if len(ready_queue) == 0:
            break
        
        pid, current_time = update_queue(processes, n, quantum, ready_queue, current_time)
        if pid is not None:
            gantt_chart.append(pid)

    return gantt_chart

def main():
    n = int(input("Enter the number of processes: "))
    quantum = int(input("Enter the time quantum: "))

    processes = []
    for i in range(n):
        arrivalTime, burstTime = map(int, input(f"Enter arrival time and burst time for Process P{i + 1}: ").split())
        processes.append(Process(i + 1, arrivalTime, burstTime))

    gantt_chart = round_robin(processes, n, quantum)
    print("\nGantt chart:")
    print("| ", end="")
    for process in gantt_chart:
        print(f"P{process} | ", end="")
    print()

    avg_turnaround_time = 0
    avg_waiting_time = 0
    for process in processes:
        process.turnaroundTime = process.completionTime - process.arrivalTime
        process.waitingTime = process.turnaroundTime - process.burstTime
        avg_turnaround_time += process.turnaroundTime
        avg_waiting_time += process.waitingTime

    avg_turnaround_time /= n
    avg_waiting_time /= n

    throughput = n / processes[-1].completionTime if processes[-1].completionTime != 0 else 0

    print("\nProcess | AT | BT | CT | TAT | WT |")
    for process in processes:
        print(f"P{process.pid}\t| {process.arrivalTime}\t| {process.burstTime}\t| {process.completionTime}\t| {process.turnaroundTime}\t| {process.waitingTime}\t|")

    print(f"\nAverage Turnaround Time (ATAT): {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time (AWT): {avg_waiting_time:.2f}")
    print(f"Throughput: {throughput:.3f}")

if __name__ == "__main__":
    main()
