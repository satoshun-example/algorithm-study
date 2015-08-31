#include <iostream>
#include <math.h>

#define swap(array, x1, x2) { \
    int temp = array[x1]; \
    array[x1] = array[x2]; \
    array[x2] = temp; \
}

int* digitRadix(int* array, int size, int digit)
{
    int* newArray = new int[size];

    int count[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; // 0-9
    for (int i = 0; i < size; i++) {
        int d = int(array[i] / pow(10, digit-1)) % 10;
        count[d]++;
    }

    for (int i = 1; i < 10; i++) {
        count[i] += count[i-1];
    }

    for (int i = size-1; i >= 0; i--) {
        int d = int(array[i] / pow(10, digit-1)) % 10;
        newArray[--count[d]] = array[i];
    }

    return newArray;
}

void radix(int* array, int size)
{
    int* newArray = array;
    int maxDigit = 3; // TODO
    for (int digit = 1; digit <= maxDigit; digit++) {
        newArray = digitRadix(newArray, size, digit);
    }

    memcpy(array, newArray, size * sizeof(int));
}

int main()
{
    int array[] = {8, 7, 5, 10, 5, 1, 3, 212, 12, 321, 35, 1, 890};
    int size = sizeof(array) / sizeof(int);
    radix(array, size);

    for (int i = 0; i < size; i++) {
        std::cout << array[i] << std::endl;
    }
}
