#include<stdio.h>
#include<string.h>

struct pda_rule {
    char state;
    char input_symbol;
    char stack_top;
    char *new_stack;
};
struct cfg_rule {
    char lhs;
    char *rhs;
};
void pda_to_cfg(struct pda_rule *pda_rules, int num_pda_rules) {
    int num_cfg_rules = num_pda_rules * 2;
    struct cfg_rule cfg_rules[num_cfg_rules];

    int i, j, k = 0;
    char new_lhs;
    for (i = 0; i < num_pda_rules; i++) {
        new_lhs = pda_rules[i].state;
        if (strcmp(pda_rules[i].new_stack, "") == 0) {
            cfg_rules[k].lhs = new_lhs;
            cfg_rules[k].rhs = malloc(3 * sizeof(char));
            cfg_rules[k].rhs[0] = pda_rules[i].input_symbol;
            cfg_rules[k].rhs[1] = new_lhs;
            cfg_rules[k].rhs[2] = '\0';
            k++;
        }
        cfg_rules[k].lhs = new_lhs;
        cfg_rules[k].rhs = malloc(4 * sizeof(char));
        cfg_rules[k].rhs[0] = pda_rules[i].input_symbol;
        cfg_rules[k].rhs[1] = pda_rules[i].new_stack[0];
        cfg_rules[k].rhs[2] = new_lhs;
        cfg_rules[k].rhs[3] = '\0';
        k++;
    }
    printf("\nCFG Productions:\n");
    for (i = 0; i < num_cfg_rules; i++) {
        printf("%c -> %s\n", cfg_rules[i].lhs, cfg_rules[i].rhs);
    }
}
int main() {
    struct pda_rule pda_rules[] = {
        {'q', '0', 'z', "xz"},
        {'q', '0', 'x', "xx"},
        {'q', '1', 'x', "x"},
        {'q', ' ', 'x', ""},
        {'p', '1', 'x', "xx"},
        {'p', ' ', 'x', ""},
        {'p', '1', 'z', ""}
    };
    pda_to_cfg(pda_rules, 7);

    return 0;
}
