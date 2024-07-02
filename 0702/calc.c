// calc.c

#include <stdio.h>
#include <stdlib.h>

// 四則演算を行う関数
double calculate(char *expression) {
    double num1, num2;
    char op;
    int result = sscanf(expression, "%lf %c %lf", &num1, &op, &num2);
    if (result != 3) {
        printf("Error: Invalid expression\n");
        return 0.0;
    }
    
    switch (op) {
        case '+':
            return num1 + num2;
        case '-':
            return num1 - num2;
        case '*':
            return num1 * num2;
        case '/':
            if (num2 == 0) {
                printf("Error: Division by zero\n");
                return 0.0;
            }
            return num1 / num2;
        default:
            printf("Error: Unsupported operator\n");
            return 0.0;
    }
}
