#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_EXPRESSION_LENGTH 256

char current_expression[MAX_EXPRESSION_LENGTH] = {0};
char current_display[MAX_EXPRESSION_LENGTH] = "0";
double last_result = 0.0;
int new_input = 1;  // 新しい計算を開始するフラグ

// 関数プロトタイプ宣言
double evaluate_expression(const char *expression);
int is_operator(char c);
int precedence(char op);
double apply_operator(double a, double b, char op);
void update_display(const char *expression);

// ボタンが押されたときの処理
__declspec(dllexport) const char* button_pressed(const char *input) {
    if (strcmp(input, "C") == 0) {
        // クリア
        current_expression[0] = '\0';
        strcpy(current_display, "0");
        last_result = 0.0;
        new_input = 1;  // 新しい計算を開始
    } else if (strcmp(input, "=") == 0) {
        // 計算実行
        if (strlen(current_expression) > 0) {
            double result = evaluate_expression(current_expression);
            snprintf(current_display, sizeof(current_display), "%g", result);
            last_result = result;  // 結果を保持
        }
        // 計算式をリセット
        current_expression[0] = '\0';
        new_input = 1;  // 新しい計算を開始
    } else {
        if (new_input) {
            // 新しい計算が開始された場合、前の結果を式の先頭に置く
            // もし "0" のままなら、それを消して新しい入力で置き換える
            if (strcmp(current_display, "0") == 0) {
                current_expression[0] = '\0';
            } else {
                snprintf(current_expression, sizeof(current_expression), "%g", last_result);
            }
            new_input = 0;  // フラグをリセット
        }
        
        // 数字または演算子
        if (strlen(current_expression) < MAX_EXPRESSION_LENGTH - 1) {
            strcat(current_expression, input);
            update_display(current_expression);
        }
    }
    return current_display;
}

// 表示を更新する関数
void update_display(const char *expression) {
    strcpy(current_display, expression);
}

// 数式を評価する関数
double evaluate_expression(const char *expression) {
    double values[MAX_EXPRESSION_LENGTH];
    char operators[MAX_EXPRESSION_LENGTH];
    int val_index = 0, op_index = 0;
    int i = 0;

    while (expression[i] != '\0') {
        if (isspace(expression[i])) {
            i++;
            continue;
        }

        if (isdigit(expression[i]) || expression[i] == '.') {
            char number[MAX_EXPRESSION_LENGTH];
            int num_index = 0;

            while (isdigit(expression[i]) || expression[i] == '.') {
                number[num_index++] = expression[i++];
            }
            number[num_index] = '\0';

            values[val_index++] = atof(number);
        } else if (is_operator(expression[i])) {
            while (op_index > 0 && precedence(operators[op_index - 1]) >= precedence(expression[i])) {
                double b = values[--val_index];
                double a = values[--val_index];
                char op = operators[--op_index];

                values[val_index++] = apply_operator(a, b, op);
            }
            operators[op_index++] = expression[i++];
        } else {
            fprintf(stderr, "Invalid character in expression: %c\n", expression[i]);
            exit(1);
        }
    }

    while (op_index > 0) {
        double b = values[--val_index];
        double a = values[--val_index];
        char op = operators[--op_index];

        values[val_index++] = apply_operator(a, b, op);
    }

    return values[0];
}

// オペレータかどうかを判定
int is_operator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

// オペレータの優先度を返す
int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

// オペレータを適用して結果を返す
double apply_operator(double a, double b, char op) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return a / b;
        default: return 0;
    }
}

int main() {
    // テスト用のメイン関数
    char input[256];
    while (1) {
        printf("Input button press: ");
        scanf("%s", input);
        printf("Display: %s\n", button_pressed(input));
    }
    return 0;
}
