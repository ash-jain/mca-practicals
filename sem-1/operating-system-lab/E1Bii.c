// 1. Implement the following CPU scheduling.
// B) SJFS - Shortest Job First Serve (Pre-emptive).

#include <stdio.h>

struct process {
    int pid;
    int arrival_time;
    int burst_time;
    int remaining_time;
    int completion_time;
    int turn_around_time;
    int waiting_time;
    int response_time;
    int exec;
};

int main() {
    int process_count;

    printf("CPU SCHEDULING USING SJFS (Pre-emptive)\n\nEnter the number of processes: ");
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
        p[i].remaining_time = p[i].burst_time;
        p[i].exec = 0;
    }

    int total_completion_time = 0;
    int total_turn_around_time = 0;
    int total_waiting_time = 0;
    int total_response_time = 0;
    int count = 0;
    int lri = -1; // Least remaining index.

    while (count < process_count) {

        for (j = 0; j < process_count; j++) {
            if (lri == j || p[j].exec == 1)
                continue;

            if ((lri == -1 || p[j].remaining_time < p[lri].remaining_time) && p[j].arrival_time <= total_completion_time) {
                lri = j;
            } else if (lri != -1 && p[lri].remaining_time == p[j].remaining_time) {
                lri = (p[lri].arrival_time < p[j].arrival_time) ? lri : j;
            }
        }

        if (lri == -1) {
            total_completion_time++;
            continue;
        } else if (p[lri].burst_time == p[lri].remaining_time) {
            p[lri].response_time = total_completion_time - p[lri].arrival_time;
        }

        p[lri].remaining_time--;
        total_completion_time++;

        if (p[lri].remaining_time == 0) {
            p[lri].completion_time = total_completion_time;
            p[lri].turn_around_time = p[lri].completion_time - p[lri].arrival_time;
            p[lri].waiting_time = p[lri].turn_around_time - p[lri].burst_time;
            p[lri].exec = 1;
            count += 1;
            total_turn_around_time += p[lri].turn_around_time;
            total_waiting_time += p[lri].waiting_time;
            total_response_time += p[lri].response_time;
        }

        lri = -1;
    }

    printf("\n-----------------------------------------------------------------------------------------------------------\n");
    printf("| Process | Arrival Time | Burst Time | Completion Time | Turn Around Time | Waiting Time | Response Time |\n");
    printf("-----------------------------------------------------------------------------------------------------------\n");
    for (i = 0; i < process_count; i++) {
        printf("|%9d|%14d|%12d|%17d|%18d|%14d|%15d|\n", p[i].pid, p[i].arrival_time, p[i].burst_time, p[i].completion_time, p[i].turn_around_time, p[i].waiting_time, p[i].response_time);
    }
    printf("-----------------------------------------------------------------------------------------------------------\n");

    double mean_turn_around_time = (double) total_turn_around_time / process_count;
    double mean_waiting_time = (double) total_waiting_time / process_count;
    double mean_response_time = (double) total_response_time / process_count;
    printf("\nMean Turn Around Time:    \t%g.\n", mean_turn_around_time);
    printf("Mean Waiting Time: \t%g.\n", mean_waiting_time);
    printf("Mean Response Time: \t %g.\n", mean_response_time);

    return 0;
}
