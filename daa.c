#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Job {
    int id;
    int deadline;
    int profit;
} Job;

int compare_jobs(const void *a, const void *b) {
    Job *job1 = (Job *) a;
    Job *job2 = (Job *) b;
    return job2->profit - job1->profit;
}

void schedule_jobs(Job jobs[], int n) {
    qsort(jobs, n, sizeof(Job), compare_jobs);
    int max_deadline = 0;
    for (int i = 0; i < n; i++) {
        if (jobs[i].deadline > max_deadline) {
            max_deadline = jobs[i].deadline;
        }
    }
    int slot[max_deadline];
    for (int i = 0; i < max_deadline; i++) {
        slot[i] = -1;
    }
    int total_profit = 0;
    for (int i = 0; i < n; i++) {
        for (int j = jobs[i].deadline - 1; j >= 0; j--) {
            if (slot[j] == -1) {
                slot[j] = jobs[i].id;
                total_profit += jobs[i].profit;
                break;
            }
        }
    }
    printf("Job sequence with maximum profit: ");
    for (int i = 0; i < max_deadline; i++) {
        if (slot[i] != -1) {
            printf("%d ", slot[i]);
        }
    }
    printf("\nTotal profit: %d\n", total_profit);
}

int main() {
    Job jobs[] = {
        {1, 2, 40},
        {2, 4, 15},
        {3, 3, 60},
        {4, 2, 20},
        {5, 3, 10},
        {6, 1, 45},
        {7, 1, 55}
    };
    int n = sizeof(jobs) / sizeof(Job);
    schedule_jobs(jobs, n);
    return 0;
}
