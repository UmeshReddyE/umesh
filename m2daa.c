#include <stdio.h>
#include <stdlib.h>

int min_time_to_process_jobs(int a[], int b[], int n) {
    int T[n+1][2];
    T[1][0] = a[0];
    T[1][1] = b[0];
    
    for (int i = 2; i <= n; i++) {
        T[i][0] = T[i-1][0] + a[i-1] < T[i-1][1] + b[i-1] ? T[i-1][0] + a[i-1] : T[i-1][1] + b[i-1];
        T[i][1] = T[i-1][1] + b[i-1] < T[i-1][0] + a[i-1] ? T[i-1][1] + b[i-1] : T[i-1][0] + a[i-1];
    }
        
    return T[n][0] < T[n][1] ? T[n][0] : T[n][1];
}

int main() {
    int n;
    printf("Enter the number of jobs: ");
    scanf("%d", &n);
    
    int a[n], b[n];
    printf("Enter the processing time for each job on machine A: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    printf("Enter the processing time for each job on machine B: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &b[i]);
    }
    
    int min_time = min_time_to_process_jobs(a, b, n);
    printf("Minimum time to process all jobs: %d\n", min_time);
    
    return 0;
}
