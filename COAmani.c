#include <stdio.h>
#include <stdint.h>

// Logical Right Shift of 4 bits
uint16_t logical_right_shift(uint16_t operand) {
    return operand >> 4;
}

// Arithmetic Right Shift of 4 bits
int16_t arithmetic_right_shift(int16_t operand) {
    return operand >> 4;
}

// Left Shift of 4 bits
uint16_t left_shift(uint16_t operand) {
    return operand << 4;
}

// Left Rotate of 4 bits
uint16_t left_rotate(uint16_t operand) {
    return (operand << 4) | (operand >> 12);
}

// Arithmetic Right Rotate of 4 bits
int16_t arithmetic_right_rotate(int16_t operand) {
    return (operand >> 4) | (operand << 12);
}

int main() {
    uint16_t operand;

    printf("Enter a 16-bit operand in hexadecimal format (e.g. 0xABCD): ");
    scanf("%hx", &operand);

    printf("Operand: 0x%04X\n", operand);
    printf("Logical Right Shift: 0x%04X\n", logical_right_shift(operand));
    printf("Arithmetic Right Shift: 0x%04X\n", arithmetic_right_shift((int16_t)operand));
    printf("Left Shift: 0x%04X\n", left_shift(operand));
    printf("Left Rotate: 0x%04X\n", left_rotate(operand));
    printf("Arithmetic Right Rotate: 0x%04X\n", arithmetic_right_rotate((int16_t)operand));

    return 0;
}
