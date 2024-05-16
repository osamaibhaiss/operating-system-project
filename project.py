class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.finish_time = None
        self.waiting_time = 0
        self.turnaround_time = 0


def read_processes_from_file(file_path):
    processes = []
    with open(file_path, 'r') as file:
        for line in file:
            pid, arrival_time, burst_time = map(int, line.strip().split(','))
            processes.append(Process(pid, arrival_time, burst_time))
    return processes


def first_come_first_serve(processes):
    current_time = 0
    for process in processes:
        current_time = max(current_time, process.arrival_time)
        process.start_time = current_time
        process.finish_time = current_time + process.burst_time
        process.turnaround_time = process.finish_time - process.arrival_time
        process.waiting_time = process.start_time - process.arrival_time
        current_time = process.finish_time
    return processes


def shortest_remaining_time(processes):
    current_time = 0
    ready_queue = []
    completed_processes = []
    while processes or ready_queue:
        for process in processes[:]:
            if process.arrival_time <= current_time:
                ready_queue.append(process)
                processes.remove(process)
        if ready_queue:
            ready_queue.sort(key=lambda x: x.remaining_time)
            current_process = ready_queue.pop(0)
            current_process.start_time = current_time
            current_process.remaining_time -= 1
            current_time += 1
            if current_process.remaining_time == 0:
                current_process.finish_time = current_time
                current_process.turnaround_time = current_process.finish_time - current_process.arrival_time
                current_process.waiting_time = current_process.start_time - current_process.arrival_time
                completed_processes.append(current_process)
        else:
            current_time += 1
    return completed_processes


def round_robin(processes, quantum):
    current_time = 0
    ready_queue = []
    completed_processes = []
    while processes or ready_queue:
        for process in processes[:]:
            if process.arrival_time <= current_time:
                ready_queue.append(process)
                processes.remove(process)
        if ready_queue:
            current_process = ready_queue.pop(0)
            current_process.start_time = current_time
            if current_process.remaining_time > quantum:
                current_time += quantum
                current_process.remaining_time -= quantum
                ready_queue.append(current_process)
            else:
                current_time += current_process.remaining_time
                current_process.remaining_time = 0
                current_process.finish_time = current_time
                current_process.turnaround_time = current_process.finish_time - current_process.arrival_time
                current_process.waiting_time = current_process.start_time - current_process.arrival_time
                completed_processes.append(current_process)
        else:
            current_time += 1
    return completed_processes


def calculate_metrics(processes):
    if not processes:
        return 0, 0, 0  # If no data in file you must return
    total_turnaround_time = sum(process.turnaround_time for process in processes)
    total_waiting_time = sum(process.waiting_time for process in processes)
    total_cpu_time = sum(process.burst_time for process in processes)
    cpu_utilization = total_cpu_time / processes[-1].finish_time
    return total_turnaround_time, total_waiting_time, cpu_utilization


def generate_gantt_chart(processes):
    return ''.join(f"| {process.pid} " for process in processes) + '|'


def display_results(processes, total_turnaround_time, total_waiting_time, cpu_utilization):
    print("Process    Start Time    Finish Time    Turnaround Time    Waiting Time")
    for process in processes:
        print(f"{process.pid}         {process.start_time}              {process.finish_time}                {process.turnaround_time}                    {process.waiting_time}")
    print("\nGantt Chart:")
    print(generate_gantt_chart(processes))
    print("\nTotal Turnaround Time:", total_turnaround_time)
    print("Total Waiting Time:", total_waiting_time)
    print("CPU Utilization:", cpu_utilization)


if __name__ == "__main__":
    # reading the data from a file
    file_path = "C:\\Users\\Palestine\\Desktop\\osfinalpr\\input.txt"
    processes = read_processes_from_file(file_path)

    # fcfs scheduling simulation
    fcfs_processes = first_come_first_serve(processes.copy())
    fcfs_turnaround_time, fcfs_waiting_time, fcfs_cpu_utilization = calculate_metrics(fcfs_processes)

    # SRT  scheduling simulation
    srt_processes = shortest_remaining_time(processes.copy())
    srt_turnaround_time, srt_waiting_time, srt_cpu_utilization = calculate_metrics(srt_processes)

    #
    quantum = 3
    rr_processes = round_robin(processes.copy(), quantum)
    rr_turnaround_time, rr_waiting_time, rr_cpu_utilization = calculate_metrics(rr_processes)

    # display results of all processes
    print("FCFS Results:")
    display_results(fcfs_processes, fcfs_turnaround_time, fcfs_waiting_time, fcfs_cpu_utilization)

    print("\nSRT Results:")
    display_results(srt_processes, srt_turnaround_time, srt_waiting_time, srt_cpu_utilization)

    print("\nRR Results (Quantum =", quantum, "):")
    display_results(rr_processes, rr_turnaround_time, rr_waiting_time, rr_cpu_utilization)
