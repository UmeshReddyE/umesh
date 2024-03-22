#include <stdio.h>
#include<string.h>
enum {q0, q1, q2, q3, q4}; // Define the states of the NFA

int is_accepting_state(int state) {
    return (state == q4); // Accept if in final state q4
}

int transition(int state, char c) {
    switch (state) {
        case q0:
            if (c == '1') return q1;
            else return q0;
        case q1:
            if (c == '0') return q2;
            else if (c == '1') return q1;
            else return q0;
        case q2:
            if (c == '1') return q3;
            else return q0;
        case q3:
            if (c == '1') return q4;
            else if (c == '0') return q2;
            else return q0;
        case q4:
            return q4;
    }
}

int run_nfa(char *input_string) {
    int current_state = q0;
    printf("Transition sequence:\nq0");
    while (*input_string != '\0') {
        printf(" --%c--> q%d", *input_string, transition(current_state, *input_string));
        current_state = transition(current_state, *input_string);
        input_string++;
    }
    printf("\n");
    return is_accepting_state(current_state);
}
void check11(char string[])
{
    int i=0,c=0;
    while(string[i]!='\0')
    {
    if(string[i]!='1' || string[i]!= '0')
    c++;
    i++;
    }
    if(c>0)
    printf("Enter valid alphabets.\n");
    else{
    int l=strlen(string);
    char a=string[l-1],b=string[l-2];
    if(a == '1' && b == '1') {
    printf("Rejected\n");
    }
    else{
    printf("Reached final state.\n Accepted.\n");
    }
    }
}

int main() {
    char input_string[100];
    int choice;
    printf("1. CHECK STRING CONTAINS SUBSTRING 1011.\n ");
    printf("2. CHECK STRING DOESN'T END WITH 11.\n ");
    printf("3. FOR EXIT.\n\n");
    printf("Enter your choice :");
    scanf("%d",&choice);
    if(choice==1){
        printf("Enter string :");
    scanf("%s", input_string);
    if (run_nfa(input_string)) {
        printf("Accepted\n");
    } else {
        printf("Rejected\n");
    }
    }
    else
    if(choice==2){
        printf("Enter the string\n");
        scanf("%s",input_string);
        check11(input_string);
    }
    return 0;
}
