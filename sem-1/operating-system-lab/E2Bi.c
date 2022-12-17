// 2. Implement the following CPU scheduling.
// B) Priority (Non Pre-emptive).

#include <stdio.h>

struct process {
    int pid;
    int arrival_time;
    int priority;
    int burst_time;
    int completion_time;
    int turn_around_time;
    int waiting_time;
    int exec;
};

int main() {
    int process_count;

    printf("CPU SCHEDULING USING PRIORITY SCHEDULING (Non Pre-emptive)\n\nEnter the number of processes: ");
    scanf("%d", &process_count);
    printf("");

    struct process p[process_count];

    int i = 0, j = 0;
    for (i = 0; i < process_count; i++) {
        p[i].pid = i+1;
        printf("Enter process %d arrival time: ", i+1);
        scanf("%d", &p[i].arrival_time);
        printf("Enter process %d priority: ", i+1);
        scanf("%d", &p[i].priority);
        printf("Enter process %d burst time: ", i+1);
        scanf("%d", &p[i].burst_time);
        p[i].exec = 0;
    }

    int total_completion_time = 0;
    int total_turn_around_time = 0;
    int total_waiting_time = 0;
    int hpi = -1; // Highest priority index.

    for (i = 0; i < process_count; i++) {

        int delay = 0;
        for (j = 0; j < process_count; j++) {
            if (hpi == j || p[j].exec == 1 || (delay == 0 && hpi != -1 && p[hpi].priority < p[j].priority)) {
                continue;
            }

            if ((hpi == -1 || p[j].priority < p[hpi].priority) && p[j].arrival_time <= total_completion_time) {
                hpi = j;
                delay = 0;
            } else if ((hpi == -1 || p[j].arrival_time <= p[hpi].arrival_time) && p[j].arrival_time > total_completion_time) {
                hpi = (p[j].priority < p[hpi].priority || hpi == -1) ? j : hpi;
                delay = p[hpi].arrival_time - total_completion_time;
            } else if (p[j].arrival_time < total_completion_time && p[hpi].arrival_time < total_completion_time && p[hpi].priority == p[j].priority) {
                hpi = (p[hpi].arrival_time < p[j].arrival_time) ? hpi : j;
                delay = 0;
            }
        }

        p[hpi].completion_time = total_completion_time + delay + p[hpi].burst_time;
        p[hpi].turn_around_time = p[hpi].completion_time - p[hpi].arrival_time;
        p[hpi].waiting_time = p[hpi].turn_around_time - p[hpi].burst_time;
        p[hpi].exec = 1;

        total_completion_time += delay + p[hpi].burst_time;
        total_turn_around_time += p[hpi].turn_around_time;
        total_waiting_time += p[hpi].waiting_time;

        hpi = -1;
    }

    printf("\n------------------------------------------------------------------------------------------------------\n");
    printf("| Process | Arrival Time | Priority | Burst Time | Completion Time | Turn Around Time | Waiting Time |\n");
    printf("------------------------------------------------------------------------------------------------------\n");
    for (i = 0; i < process_count; i++) {
        printf("|%9d|%14d|%10d|%12d|%17d|%18d|%14d|\n", p[i].pid, p[i].arrival_time, p[i].priority, p[i].burst_time, p[i].completion_time, p[i].turn_around_time, p[i].waiting_time);
    }
    printf("------------------------------------------------------------------------------------------------------\n");

    double mean_turn_around_time = (double) total_turn_around_time / process_count;
    double mean_waiting_time = (double) total_waiting_time / process_count;
    printf("\nMean Turn Around Time:    \t%g.\n", mean_turn_around_time);
    printf("Mean Waiting Time: \t%g.\n", mean_waiting_time);

    return 0;
}
