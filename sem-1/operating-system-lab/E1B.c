// 1. Implement the following CPU scheduling.
// B) SJFS - Shortest Job First Serve (Non Pre-emptive).

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

    printf("CPU SCHEDULING USING SJFS (Non Pre-emptive)\n\nEnter the number of processes: ");
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
    int lbi = -1; // Least burst index.
    for (i = 0; i < process_count; i++) {

        int delay = 0;
        for (j = 0; j < process_count; j++) {
            if (lbi == j || p[j].exec == 1 || (lbi != -1 && p[lbi].burst_time < p[j].burst_time)) {
                continue;
            }

            if ((lbi == -1 || p[j].burst_time < p[lbi].burst_time) && p[j].arrival_time <= total_completion_time) {
                lbi = j;
                delay = 0;
            } else if (lbi == -1 && p[j].arrival_time > total_completion_time) {
                lbi = j;
                delay = p[j].arrival_time - total_completion_time;
            } else if (p[j].arrival_time < total_completion_time && p[lbi].arrival_time < total_completion_time && p[lbi].burst_time == p[j].burst_time) {
                lbi = (p[lbi].arrival_time < p[j].arrival_time) ? lbi : j;
                delay = 0;
            }
        }

        p[lbi].completion_time = total_completion_time + delay + p[lbi].burst_time;
        p[lbi].turn_around_time = p[lbi].completion_time - p[lbi].arrival_time;
        p[lbi].waiting_time = p[lbi].turn_around_time - p[lbi].burst_time;
        p[lbi].exec = 1;

        total_completion_time += delay + p[lbi].burst_time;
        total_turn_around_time += p[lbi].turn_around_time;
        total_waiting_time += p[lbi].waiting_time;

        lbi = -1;
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
    printf("Mean Waiting Time: \t%g.\n", (float) mean_waiting_time);

    return 0;
}
