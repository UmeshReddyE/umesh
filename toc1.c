#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int len, zeros = 0, ones = 0;
    printf("Enter a string: ");
    scanf("%s", str);
    len = strlen(str);
    for (int i = 0; i < len; i++) {
        if (str[i] == '0') {
            zeros++;
        } else if (str[i] == '1') {
            ones++;
        }
    }
    if (zeros >= 2 && ones <= 2) {
        printf("The string is valid.\n");
    } else {
        printf("The string is invalid.\n");
    }
    return 0;
}
