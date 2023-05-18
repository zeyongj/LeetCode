#include <stdlib.h>
#include <string.h>

char * multiply(char * num1, char * num2){
    int len1 = strlen(num1), len2 = strlen(num2);
    int *result = (int *)calloc((len1 + len2), sizeof(int));

    for(int i = len1 - 1; i >= 0; i--) {
        for(int j = len2 - 1; j >= 0; j--) {
            int mul = (num1[i] - '0') * (num2[j] - '0'); 
            int p1 = i + j, p2 = i + j + 1;
            int sum = mul + result[p2];

            result[p1] += sum / 10;
            result[p2] = sum % 10;
        }
    }  

    char *product = (char *)calloc((len1 + len2 + 1), sizeof(char));
    int index = 0;
    for(int i = 0; i < len1 + len2; i++){
        if(!(index == 0 && result[i] == 0)) product[index++] = result[i] + '0';
    }
    product[index] = '\0';

    free(result);

    return index == 0 ? "0" : product;
}
