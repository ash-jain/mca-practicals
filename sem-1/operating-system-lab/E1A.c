// Implement the following CPU scheduling.
// A) FCFS - First-Come-First-Serve.

#include <stdio.h>

struct process {
    int pid;
    int arrival_time;
    int burst_time;
    int completion_time;
    int turn_time;
    int waiting_time;
} p[5];

int main() {
    int process_count;

    printf("Enter the number of processes: ");
    scanf("%d", &process_count);

    int i = 0;
    for (i = 0; i < process_count; i++) {
        p[i].pid = i;
        printf("Enter process %d arrival time: ", i);
        scanf("%d", &p[i].arrival_time);
        printf("Enter process %d burst time: ", i);
        scanf("%d", &p[i].burst_time);

        if (i == 0) {
            p[i].completion_time = p[i].burst_time;
        } else {
            p[i].completion_time = p[i-1].completion_time + p[i].burst_time;
        }

        p[i].turn_time = p[i].completion_time - p[i].arrival_time;
        p[i].waiting_time = p[i].turn_time - p[i].burst_time;
    }

    printf("\n------------------------------------------------------------------------------------\n");
    printf("| Process | Arrival Time | Burst Time | Completion Time | Turn Time | Waiting Time |\n");
    printf("------------------------------------------------------------------------------------\n");
    for (i = 0; i < process_count; i++) {
        printf("|%9d|%14d|%12d|%17d|%11d|%14d|\n", p[i].pid, p[i].arrival_time, p[i].burst_time, p[i].completion_time, p[i].turn_time, p[i].waiting_time);
    }
    printf("------------------------------------------------------------------------------------\n");

    int total_waiting_time = 0;
    int total_turn_time = 0; 
    for (i = 0; i < process_count; i++) {
        total_turn_time += p[i].turn_time;
        total_waiting_time += p[i].waiting_time;
    }

    printf("\nAverage Turn Time:    \t%d.\n", total_turn_time / process_count);
    printf("Average Waiting Time: \t%d.\n", total_waiting_time / process_count);

    return 0;
}
