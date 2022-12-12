// 1. Implement the following CPU scheduling.
// A) FCFS - First Come First Serve.

#include <stdio.h>

struct process {
    int pid;
    int arrival_time;
    int burst_time;
    int completion_time;
    int turn_around_time;
    int waiting_time;
    int exec;
};

int main() {
    int process_count;

    printf("CPU SCHEDULING USING FCFS \n\nEnter the number of processes: ");
    scanf("%d", &process_count);
    printf("");

    struct process p[process_count];

    int i = 0, j = 0;
    for (i = 0; i < process_count; i++) {
        p[i].pid = i+1;
        printf("Enter process %d arrival time: ", i+1);
        scanf("%d", &p[i].arrival_time);
        printf("Enter process %d burst time: ", i+1);
        scanf("%d", &p[i].burst_time);
        p[i].exec = 0;
    }

    int total_completion_time = 0;
    int total_turn_around_time = 0;
    int total_waiting_time = 0;
    int fci = -1; // First come index.
    for (i = 0; i < process_count; i++) {

        for (j = 0; j < process_count; j++) {
            if ((fci == -1 || p[j].arrival_time < p[fci].arrival_time) && p[j].exec != 1) {
                fci = j;
            }
        }

        int delay = 0;
        if (total_completion_time < p[fci].arrival_time) {
            delay = p[fci].arrival_time - total_completion_time;
        }

        p[fci].completion_time = total_completion_time + delay + p[fci].burst_time;
        p[fci].turn_around_time = p[fci].completion_time - p[fci].arrival_time;
        p[fci].waiting_time = p[fci].turn_around_time - p[fci].burst_time;
        p[fci].exec = 1;

        total_completion_time += delay + p[fci].burst_time;
        total_turn_around_time += p[fci].turn_around_time;
        total_waiting_time += p[fci].waiting_time;

        fci = -1;
    }

    printf("\n-------------------------------------------------------------------------------------------\n");
    printf("| Process | Arrival Time | Burst Time | Completion Time | Turn Around Time | Waiting Time |\n");
    printf("-------------------------------------------------------------------------------------------\n");
    for (i = 0; i < process_count; i++) {
        printf("|%9d|%14d|%12d|%17d|%18d|%14d|\n", p[i].pid, p[i].arrival_time, p[i].burst_time, p[i].completion_time, p[i].turn_around_time, p[i].waiting_time);
    }
    printf("-------------------------------------------------------------------------------------------\n");

    double mean_turn_around_time = (double) total_turn_around_time / process_count;
    double mean_waiting_time = (double) total_waiting_time / process_count;
    printf("\nMean Turn Around Time:    \t%g.\n", mean_turn_around_time);
    printf("Mean Waiting Time: \t%g.\n", mean_waiting_time);

    return 0;
}
