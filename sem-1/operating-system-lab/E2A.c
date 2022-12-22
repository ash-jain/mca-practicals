// Implement the following CPU scheduling.
// A) Round Robin.

#include <stdio.h>

struct process {
    int pid;
    int arrival_time;
    int burst_time;
    int remaining_time;
    int completion_time;
    int turn_around_time;
    int waiting_time;
};

int main() {
    int process_count;
    int TQ;

    printf("CPU SCHEDULING USING ROUND ROBIN SCHEDULING \n\nEnter the number of processes: ");
    scanf("%d", &process_count);
    printf("");

    struct process p[process_count];

    int i = 0, j = 0, k = 0;
    for (i = 0; i < process_count; i++) {
        p[i].pid = i+1;
        printf("Enter process %d arrival time: ", i+1);
        scanf("%d", &p[i].arrival_time);
        printf("Enter process %d burst time: ", i+1);
        scanf("%d", &p[i].burst_time);
        p[i].remaining_time = p[i].burst_time;
    }

    printf("Enter time quantum: ");
    scanf("%d", &TQ);
    printf("");

    int ready_queue[process_count];
    int q_size = 0;
    int total_completion_time = 0;
    int total_turn_around_time = 0;
    int total_waiting_time = 0;
    int count = 0;
    int tmp;
    int delay;
    int inq;

    while (count < process_count) {

        for (i = 0; i < process_count; i++) {
            if (p[i].remaining_time <= 0 || p[i].arrival_time > total_completion_time + TQ)
                continue;

            inq = 0;
            for (j = 0; j < q_size; j++) {
                if (ready_queue[j] == i) {
                    inq = 1;
                    break;
                }
            }
            if (inq == 1)
                continue;

            if (q_size == 0) {
                ready_queue[0] = i;
                q_size++;
                continue;
            }

            for (j = 0; j < q_size; j++) {
                if (p[ready_queue[j]].arrival_time > p[i].arrival_time) {
                    for (k = j; k < q_size; k++) {
                        tmp = ready_queue[k];
                        ready_queue[k] = i;
                        i = tmp;
                    }
                    ready_queue[q_size] = i;
                    q_size++;
                    break;
                } else if (j == q_size - 1) {
                    ready_queue[q_size] = i;
                    q_size++;
                    break;
                }
            }
        }

        if (q_size == 0) {
            total_completion_time++;
            continue;
        }

        tmp = ready_queue[0];
        delay = (p[tmp].arrival_time > total_completion_time) ? p[tmp].arrival_time - total_completion_time : 0;
        p[tmp].remaining_time -= TQ;
        total_completion_time += delay + (p[tmp].remaining_time >= 0) ? TQ : TQ + p[tmp].remaining_time;
        if (p[tmp].remaining_time <= 0) {
            p[tmp].completion_time = total_completion_time + delay;
            p[tmp].turn_around_time = p[tmp].completion_time - p[tmp].arrival_time;
            p[tmp].waiting_time = p[tmp].turn_around_time - p[tmp].burst_time;
            count += 1;
            total_turn_around_time += p[tmp].turn_around_time;
            total_waiting_time += p[tmp].waiting_time;
        }
        for (k = 0; k < q_size-1; k++) {
            ready_queue[k] = ready_queue[k+1];
        }
        if (p[tmp].remaining_time <= 0) { q_size--; }
        else { ready_queue[q_size-1] = tmp; }

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
