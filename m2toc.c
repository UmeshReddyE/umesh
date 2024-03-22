#include <stdio.h>
#include <string.h>

#define MAX_STATES 10
#define MAX_SYMBOLS 10
#define MAX_STACK_SYMBOLS 10

int num_states, num_input_symbols, num_stack_symbols;
char input_symbols[MAX_SYMBOLS], stack_symbols[MAX_STACK_SYMBOLS];

struct rule {
    char lhs;
    char rhs[MAX_STACK_SYMBOLS + 1];
};

struct state {
    int num_rules;
    struct rule rules[MAX_SYMBOLS];
};

struct state states[MAX_STATES];

void read_input_symbols() {
    printf("Enter the input symbols: ");
    scanf("%s", input_symbols);
    num_input_symbols = strlen(input_symbols);
}

void read_stack_symbols() {
    printf("Enter the stack symbols: ");
    scanf("%s", stack_symbols);
    num_stack_symbols = strlen(stack_symbols);
}

void read_num_states() {
    printf("Enter the number of states: ");
    scanf("%d", &num_states);
}

void read_rules() {
    for (int i = 0; i < num_states; i++) {
        printf("Enter the number of rules for state %d: ", i);
        scanf("%d", &states[i].num_rules);

        for (int j = 0; j < states[i].num_rules; j++) {
            printf("Enter the rule %d for state %d: ", j, i);
            scanf("%s", states[i].rules[j].rhs);
            states[i].rules[j].lhs = stack_symbols[j];
        }
    }
}

void print_grammar() {
    printf("\nContext-Free Grammar:\n");

    for (int i = 0; i < num_states; i++) {
        for (int j = 0; j < states[i].num_rules; j++) {
            printf("%c -> %s", states[i].rules[j].lhs, states[i].rules[j].rhs);

            // for (int k = 0; k < num_input_symbols; k++) {
            //     printf(" | %c%c%c'", states[i].rules[j].lhs, input_symbols[k], stack_symbols[j]);
            // }

            printf("\n");
        }
    }

    printf("S -> %cZ\n", stack_symbols[0]);
}

int main() {
    read_input_symbols();
    read_stack_symbols();
    read_num_states();
    read_rules();
    print_grammar();
    return 0;
}
