// Student Name – Aakash Milind Jain.
// Roll Number – 222010019.
// Class – FY MCA 2022.
// Subject – Operating Systems Lab.
// Implement mutual exclusion between processes - Using binary semaphore.

#include <stdio.h>
#include <pthread.h>

int semaphore = 1;
int pid = 1;
int i;

void *critical_section() {
    // Block other processes while a process is in critical section.
    while (semaphore <= 0);
    semaphore--; // wait(s) - Locks semaphore.
    printf("Simulating job %d\n", pid);
    pid += 1;
    for (i = 1; i <= 10; i++)
        printf("%d\n", i);
    printf("Job done.\n");
    semaphore++; // signal(s) - Releases semaphore.
}

int main() {
    pthread_t thread1_id, thread2_id, thread3_id;

    printf("Creating threads\n");
    pthread_create(&thread1_id, NULL, critical_section, (void *)1);
    pthread_create(&thread2_id, NULL, critical_section, (void *)2);
    // pthread_create(&thread3_id, NULL, critical_section, (void *)2);
    pthread_join(thread1_id, NULL);
    pthread_join(thread2_id, NULL);
    // pthread_join(thread3_id, NULL);
    printf("Semaphore value unchanged after execution: %d\n", semaphore);
    pthread_exit(NULL);
}
