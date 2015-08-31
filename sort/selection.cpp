#include <iostream>

#define swap(array, x1, x2) { \
    int temp = array[x1]; \
    array[x1] = array[x2]; \
    array[x2] = temp; \
}

void selection(int* array, int size)
{
    for (int i = 0; i < size; i++) {
        int minIndex = i;
        for (int j = i+1; j < size; j++) {
            if (array[minIndex] > array[j]) {
                minIndex = j;
            }
        }

        swap(array, minIndex, i);
    }
}

int main()
{
    int array[] = {8, 7, 5, 10, 5, 1, 3};
    int size = sizeof(array) / sizeof(int);
    selection(array, size);

    for (int i = 0; i < size; i++) {
        std::cout << array[i] << std::endl;
    }
}
