#include <stdio.h>

struct Process
{
    int pid;
    int allocation[3];
    int max_need[3];
    int available[3];
    int remaining[3];
    int exec;
};

int main()
{
    int pcount;

    printf("Enter the number of process: ");
    scanf("%d", &pcount);

    struct Process p[pcount];
    int resources [3] = {0, 0, 0};

    int i, j, k;

    for (i = 0; i < 3; i++) {
        printf("Enter the limit for resource %d: ", i+1);
        scanf("%d", &resources[i]);
    }

    for (i = 0; i < pcount; i++)
    {
        p[i].pid = i;
        for (j = 0; j < 3; j++) {
            printf("Enter resource %d allocation for process %d: ", j + 1, i + 1);
            scanf("%d", &p[i].allocation[j]);
            resources[j] -= p[i].allocation[j];
        }
        for (j = 0; j < 3; j++) {
            printf("Enter %d max need for process %d: ", j + 1, i + 1);
            scanf("%d", &p[i].max_need[j]);
        }
        for (j = 0; j < 3; j++) {
            p[i].remaining[j] = p[i].max_need[j] - p[i].allocation[j];
        }
        p[i].exec = 0;
    }


    printf("\n----------------------------------------------------------------\n");
    printf("| Process | Allocation | Max Need | Available | Remaining Need |\n");
    printf("----------------------------------------------------------------\n");
    printf("|         |            |          |%4d%3d%4d|                |\n", resources[0], resources[1], resources[2]);

    int exec_count = 0;
    while (exec_count < pcount) {
        for (i = 0; i < pcount; i++) {
            if (p[i].exec != 1 && 
            p[i].remaining[0] <= resources[0] &&
            p[i].remaining[1] <= resources[1] &&
            p[i].remaining[2] <= resources[2]) {
                resources[0] += p[i].allocation[0];
                resources[1] += p[i].allocation[1];
                resources[2] += p[i].allocation[2];
                p[i].available[0] = resources[0];
                p[i].available[1] = resources[1];
                p[i].available[2] = resources[2];
                p[i].exec = 1;
                exec_count++;
            }
        }
    }

    for (i = 0; i < pcount; i++)
    {
        printf("|%9d|%4d%4d%4d|%3d%4d%3d|%4d%3d%4d|%5d%6d%5d|\n", p[i].pid, p[i].allocation[0],
               p[i].allocation[1], p[i].allocation[2], p[i].max_need[0], p[i].max_need[1], p[i].max_need[2], p[i].available[0], p[i].available[1], p[i].available[2], p[i].remaining[0], p[i].remaining[1], p[i].remaining[2]);
    }
    printf("----------------------------------------------------------------\n");
}
