Process Scheduling Simulation
📜 Description
This Python program simulates three different process scheduling algorithms:

First Come First Serve (FCFS)
Shortest Remaining Time (SRT)
Round Robin (RR)
The program simulates the execution of processes based on the above algorithms and calculates the following for each process:

Start Time
Finish Time
Turnaround Time
Waiting Time
It also computes the CPU Utilization and generates a Gantt Chart for visualizing the scheduling sequence.

🛠 Features
Simulates Process Scheduling Algorithms:
First Come First Serve (FCFS)
Shortest Remaining Time (SRT)
Round Robin (RR)
Displays:
Process details: Start Time, Finish Time, Turnaround Time, Waiting Time
Gantt Chart for process execution visualization
CPU Utilization as a percentage
Metrics:
Total Turnaround Time
Total Waiting Time
📥 Installation
Prerequisites:
Python 3.x or higher
Steps:
Clone this repository or download the script files:

bash
Copy
git clone <repository-url>
Ensure you have the correct permissions to read the input file.

📂 Input Format
The program reads process data from a file. Each line in the file should contain:

Process ID (integer)
Arrival Time (integer)
Burst Time (integer)
The values should be comma-separated. Here's an example:

txt
Copy
1,0,5
2,1,3
3,2,8
4,3,6
🚀 How to Use
Set the file_path variable in the script to the location of your input file (e.g., input.txt).

Run the script:

bash
Copy
python process_scheduling.py
The program will run the simulation for each scheduling algorithm and output:

FCFS: First Come First Serve
SRT: Shortest Remaining Time
RR: Round Robin (with quantum = 3)
💻 Example Output
FCFS Results:
sql
Copy
Process    Start Time    Finish Time    Turnaround Time    Waiting Time
1          0             5              5                  0
2          5             8              6                  3
3          8             16             14                 6
4          16            22             19                 13
Gantt Chart:

Copy
| 1 | 2 | 3 | 4 |
Metrics:

Total Turnaround Time: 44
Total Waiting Time: 22
CPU Utilization: 100%
🔄 Scheduling Algorithms
1. First Come First Serve (FCFS):
Processes are executed in the order they arrive, i.e., first process to arrive is executed first.
2. Shortest Remaining Time (SRT):
The process with the shortest remaining burst time is selected next.
3. Round Robin (RR):
Each process gets a fixed time slice (quantum). If it does not finish within that time slice, it goes back to the ready queue to wait for the next turn.
📊 Metrics Calculated
Turnaround Time:
Time from when the process arrives to when it finishes.
Waiting Time:
Time the process spends waiting in the queue before being executed.
CPU Utilization:
Percentage of time the CPU is actively processing.
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
