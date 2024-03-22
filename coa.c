#include <stdio.h>

unsigned short int rightShiftZeroFill(unsigned short int operand) {
    return (operand >> 4);
}

short int rightShiftSignExtension(short int operand) {
    return (operand >> 4);
}

unsigned short int leftShift(unsigned short int operand) {
    return (operand << 4);
}

unsigned short int leftRotate(unsigned short int operand) {
    return ((operand << 4) | (operand >> 12));
}

unsigned short int rightRotate(unsigned short int operand) {
    return ((operand >> 4) | (operand << 12));
}

int main() {
    unsigned short int operand = 0b1010110010011101;
    
    printf("Operand: %04X\n", operand);
    
    unsigned short int result = rightShiftZeroFill(operand);
    printf("Right Shift (Zero Fill): %04X\n", result);
    
    short int result2 = rightShiftSignExtension((short int)operand);
    printf("Right Shift (Sign Extension): %04X\n", result2);
    
    result = leftShift(operand);
    printf("Left Shift: %04X\n", result);
    
    result = leftRotate(operand);
    printf("Left Rotate: %04X\n", result);
    
    result = rightRotate(operand);
    printf("Right Rotate: %04X\n", result);
    
    return 0;
}
