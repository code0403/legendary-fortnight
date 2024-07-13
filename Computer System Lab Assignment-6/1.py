import heapq

class Process:
    def __init__(self, pid, priority, arrival_time, burst_time):
        self.pid = pid
        self.priority = priority
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.arrival_time < other.arrival_time
        return self.priority < other.priority

def non_preemptive_priority_scheduling(processes):
    total_processes = len(processes)
    if not processes:
        print("No processes provided.")
        return []

    processes.sort(key=lambda p: (p.arrival_time, p.priority))
    ready_queue = []
    current_time = 0
    gantt_chart = []
    total_waiting_time = 0

    while processes or ready_queue:
        while processes and processes[0].arrival_time <= current_time:
            heapq.heappush(ready_queue, processes.pop(0))

        if ready_queue:
            current_process = heapq.heappop(ready_queue)
            start_time = max(current_time, current_process.arrival_time)
            burst_time = current_process.burst_time
            current_time += burst_time
            current_process.completion_time = current_time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            total_waiting_time += current_process.waiting_time
            gantt_chart.append((start_time, current_process.pid))
        else:
            current_time = processes[0].arrival_time if processes else float('inf')

    print("Gantt Chart:")
    for start_time, pid in gantt_chart:
        print(f"| {pid} ", end="")
    print("|")
    print(end="")
    prev_time = 0
    for start_time, _ in gantt_chart:
        print(f" {start_time}  ", end="")
        prev_time = start_time
    print(f"  {prev_time + burst_time}  ")
    
    # print(f"\nTotal wait time (WT): {total_waiting_time:.2f}")
    average_waiting_time = total_waiting_time / total_processes
    print(f"\nAverage Waiting Time (AWT): {average_waiting_time:.2f}")
    
    # Calculate average waiting time only if there are completed processes
    if processes:
        average_waiting_time = total_waiting_time / len(processes)
        print(f"\nAverage Waiting Time (AWT): {average_waiting_time:.2f}")

    return processes

if __name__ == "__main__":
    n = int(input("Number of processes: "))
    processes = []

    if n <= 0:
        print("Invalid number of processes.")
    else:
        for i in range(n):
            try:
                priority, arrival_time, burst_time = map(int, input(f"Enter Priority, arrival time and Burst time for Process P{i+1}: ").split())
                processes.append(Process(f"P{i+1}", priority, arrival_time, burst_time))
            except ValueError:
                print("Invalid input format. Please provide integers for priority, arrival time, and burst time.")

        # Perform scheduling
        remaining_processes = non_preemptive_priority_scheduling(processes)
