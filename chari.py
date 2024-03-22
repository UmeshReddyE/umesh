class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0


def main():
    # Get input from user
    num_processes = int(input("Enter the number of processes: "))
    time_quantum = float(input("Enter the time quantum: "))

    processes = []
    for i in range(num_processes):
        arrival_time, burst_time = map(float, input(f"Enter arrival time and burst time for process {i + 1}: ").split())
        processes.append(Process(i + 1, arrival_time, burst_time))

    # Run the round-robin algorithm
    current_time = 0
    num_completed = 0
    while num_completed < num_processes:
        for process in processes:
            if process.remaining_time <= 0:
                continue
            print(f"Executing process {process.pid} for time quantum {time_quantum}")
            current_time += time_quantum
            process.remaining_time -= time_quantum

            if process.remaining_time <= 0:
                num_completed += 1
                process.completion_time = current_time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time

    # Print the results
    print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")


if __name__ == "__main__":
    main()
