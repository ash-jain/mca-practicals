// Implement the following CPU scheduling.
// B) Priority (Pre-emptive).

#include <stdio.h>

struct process {
    int pid;
    int arrival_time;
    int burst_time;
    int priority;
    int remaining_time;
    int completion_time;
    int turn_around_time;
    int waiting_time;
    int response_time;
    int exec;
};

int main() {
    int process_count;

    printf("CPU SCHEDULING USING PRIORITY SCHEDULING (Pre-emptive)\n\nEnter the number of processes: ");
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
        p[i].remaining_time = p[i].burst_time;
        p[i].exec = 0;
    }

    int total_completion_time = 0;
    int total_turn_around_time = 0;
    int total_waiting_time = 0;
    int total_response_time = 0;
    int count = 0;
    int hpi = -1; // Highest priority index.

    while (count < process_count) {

        for (j = 0; j < process_count; j++) {
            if (hpi == j || p[j].exec == 1)
                continue;

            if ((hpi == -1 || p[j].priority < p[hpi].priority) && p[j].arrival_time <= total_completion_time) {
                hpi = j;
            } else if (hpi != -1 && p[hpi].priority == p[j].priority) {
                hpi = (p[hpi].arrival_time < p[j].arrival_time) ? hpi : j;
            }
        }

        if (hpi == -1) {
            total_completion_time++;
            continue;
        } else if (p[hpi].burst_time == p[hpi].remaining_time) {
            p[hpi].response_time = total_completion_time - p[hpi].arrival_time;
        }

        p[hpi].remaining_time--;
        total_completion_time++;

        if (p[hpi].remaining_time == 0) {
            p[hpi].completion_time = total_completion_time;
            p[hpi].turn_around_time = p[hpi].completion_time - p[hpi].arrival_time;
            p[hpi].waiting_time = p[hpi].turn_around_time - p[hpi].burst_time;
            p[hpi].exec = 1;
            count += 1;
            total_turn_around_time += p[hpi].turn_around_time;
            total_waiting_time += p[hpi].waiting_time;
            total_response_time += p[hpi].response_time;
        }

        hpi = -1;
    }

    printf("\n----------------------------------------------------------------------------------------------------------------------\n");
    printf("| Process | Arrival Time | Priority | Burst Time | Completion Time | Turn Around Time | Waiting Time | Response Time |\n");
    printf("----------------------------------------------------------------------------------------------------------------------\n");
    for (i = 0; i < process_count; i++) {
        printf("|%9d|%14d|%10d|%12d|%17d|%18d|%14d|%15d|\n", p[i].pid, p[i].arrival_time, p[i].priority, p[i].burst_time, p[i].completion_time, p[i].turn_around_time, p[i].waiting_time, p[i].response_time);
    }
    printf("----------------------------------------------------------------------------------------------------------------------\n");

    double mean_turn_around_time = (double) total_turn_around_time / process_count;
    double mean_waiting_time = (double) total_waiting_time / process_count;
    double mean_response_time = (double) total_response_time / process_count;
    printf("\nMean Turn Around Time:    \t%g.\n", mean_turn_around_time);
    printf("Mean Waiting Time: \t%g.\n", mean_waiting_time);
    printf("Mean Response Time: \t %g.\n", mean_response_time);

    return 0;
}
