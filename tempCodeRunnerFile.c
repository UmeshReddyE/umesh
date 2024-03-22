or (int k = 0; k < num_input_symbols; k++) {
                printf(" | %c%c%c'", states[i].rules[j].lhs, input_symbols[k], stack_symbols[j]);
            }