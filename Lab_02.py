import random


class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid  # ID процесу
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time


def generate_processes(n):
    processes = []
    for i in range(1, n + 1):
        arrival_time = random.randint(0, 10)
        burst_time = random.randint(1, 10)
        priority = random.randint(1, 5)
        processes.append(Process(i, arrival_time, burst_time, priority))
    return processes


# Round Robin
def round_robin(processes, time_quantum):
    queue = sorted(processes, key=lambda p: p.arrival_time)
    time = 0
    completed = []

    print("\nRound Robin Execution:")
    while queue:
        process = queue.pop(0)
        if process.remaining_time > time_quantum:
            print(f"Process {process.pid} executed from {time} to {time + time_quantum}")
            process.remaining_time -= time_quantum
            time += time_quantum
            queue.append(process)
        else:
            print(f"Process {process.pid} executed from {time} to {time + process.remaining_time}")
            time += process.remaining_time
            process.remaining_time = 0
            completed.append(process)


def fcfs(processes):
    queue = sorted(processes, key=lambda p: p.arrival_time)
    time = 0
    total_waiting_time = 0

    print("\nFCFS Execution:")
    for process in queue:
        start_time = max(time, process.arrival_time)
        finish_time = start_time + process.burst_time
        waiting_time = start_time - process.arrival_time
        total_waiting_time += waiting_time
        print(f"Process {process.pid} executed from {start_time} to {finish_time}")
        time = finish_time


def priority_scheduling(processes):
    queue = sorted(processes, key=lambda p: (p.priority, p.arrival_time))
    time = 0

    print("\nPriority Scheduling Execution:")
    for process in queue:
        start_time = max(time, process.arrival_time)
        finish_time = start_time + process.burst_time
        print(f"Process {process.pid} with priority {process.priority} executed from {start_time} to {finish_time}")
        time = finish_time


def calculate_average_times(processes, execution_order):
    total_waiting_time = 0
    total_turnaround_time = 0

    for process in processes:
        start_time = execution_order[process.pid]['start_time']
        finish_time = execution_order[process.pid]['finish_time']
        waiting_time = start_time - process.arrival_time
        turnaround_time = finish_time - process.arrival_time
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    return avg_waiting_time, avg_turnaround_time


if __name__ == "__main__":
    random.seed(1)
    num_processes = 5
    time_quantum = 3

    processes = generate_processes(num_processes)

    print("Generated Processes:")
    for p in processes:
        print(f"ID: {p.pid}, Arrival Time: {p.arrival_time}, Burst Time: {p.burst_time}, Priority: {p.priority}")

    round_robin(processes, time_quantum)
    fcfs(processes)
    priority_scheduling(processes)
