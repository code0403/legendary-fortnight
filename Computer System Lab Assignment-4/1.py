def fcfs_scheduling(processes):
   
    processes.sort(key=lambda x: (x[1], x[0]))  # Sort by arrival time and then process ID
    
    gantt_chart = []
    completion_times = {}
    turnaround_times = {}
    waiting_times = {}
    
    current_time = 0
    
    for process_id, arrival_time, burst_time in processes:
        # Updating current time to handle idle CPU time
        if current_time < arrival_time:
            current_time = arrival_time
        
        # Updating the Gantt chart
        gantt_chart.append(process_id)
        
        # Calculate completion time
        completion_time = current_time + burst_time
        completion_times[process_id] = completion_time
        
        # Calculating turnaround time
        turnaround_time = completion_time - arrival_time
        turnaround_times[process_id] = turnaround_time
        
        # Calculating waiting time
        waiting_time = max(0, current_time - arrival_time)
        waiting_times[process_id] = waiting_time
        
        # Update current time
        current_time = completion_time
    
    return gantt_chart, completion_times, turnaround_times, waiting_times

def print_output(gantt_chart, completion_times, turnaround_times, waiting_times):
    # Printing the Gantt chart
    print("Gantt Chart:")
    print("|", end=" ")
    for process_id in gantt_chart:
        print(process_id, "|", end=" ")
    print()

    # Calculating the total time taken to complete all processes
    total_completion_time = max(completion_times.values())

    # Printing the timeline
    print("0", end=" ")
    for process_id in gantt_chart:
        print(completion_times[process_id], end=" ")
    print()

    # Printing CT, TAT, WT for each process
    print("Process | CT | TAT | WT")
    for process_id in completion_times:
        ct = completion_times[process_id]
        tat = turnaround_times[process_id]
        wt = waiting_times[process_id]
        print(f"{process_id} | {ct} | {tat} | {wt}")
    
    # Calculating and printing AWT and ATAT
    num_processes = len(completion_times)
    total_waiting_time = sum(waiting_times.values())
    total_turnaround_time = sum(turnaround_times.values())
    avg_waiting_time = total_waiting_time / num_processes
    avg_turnaround_time = total_turnaround_time / num_processes

    # Calculate throughput
    throughput = num_processes / total_completion_time

    print(f"Average Turnaround Time (ATAT): {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time (AWT): {avg_waiting_time:.2f}")
    print(f"Throughput: {throughput:.3f}")

if __name__ == "__main__":
    # Reading input from the user
    num_processes = int(input("Number of processes: "))
    processes = []
    for i in range(num_processes):
        process_id, arrival_time, burst_time = input(f"Enter process {i + 1} details (ID ArrivalTime BurstTime): ").split()
        processes.append((process_id, int(arrival_time), int(burst_time)))
    
    # Perform FCFS scheduling
    gantt_chart, completion_times, turnaround_times, waiting_times = fcfs_scheduling(processes)
    
    print_output(gantt_chart, completion_times, turnaround_times, waiting_times)
