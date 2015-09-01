#include <iostream>

#define swap(array, x1, x2) { \
    int temp = array[x1]; \
    array[x1] = array[x2]; \
    array[x2] = temp; \
}

void counting(int* array, int size)
{
    int max = array[0];
    for (int i = 0; i < size; i++) {
        if (max < array[i]) {
            max = array[i];
        }
    }
    int* count = new int[max+1];
    memset(count, 0, (max+1) * sizeof(int));

    for (int i = 0; i < size; i++) {
        count[array[i]]++;
    }

    for (int i = 1; i <= max; i++) {
        count[i] += count[i-1];
    }

    int* newArray = new int[size];
    for (int i = 0; i < size; i++) {
        int index = --count[array[i]];
        newArray[index] = array[i];
    }

    memcpy(array, newArray, size * sizeof(int));
}

int main()
{
    int array[] = {8, 7, 5, 10, 5, 1, 3, 6};
    int size = sizeof(array) / sizeof(int);
    counting(array, size);

    for (int i = 0; i < size; i++) {
        std::cout << array[i] << std::endl;
    }
}
