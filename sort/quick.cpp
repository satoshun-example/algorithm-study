#include <iostream>

#define swap(array, x1, x2) { \
    int temp = array[x1]; \
    array[x1] = array[x2]; \
    array[x2] = temp; \
}

void quick(int* array, int left, int right)
{
    int pivot = array[(left + right) / 2];
    int i = left, j = right;
    while (i <= j) {
        while (array[i] > pivot) i++;
        while (array[j] < pivot) j--;

        if (i <= j) {
            swap(array, i, j);
            i++; j--;
        }
    }
    if (left < j) {
        quick(array, left, j);
    }

    if (i < right) {
        quick(array, i, right);
    }
}

int main()
{
    int array[] = {8, 7, 5, 10, 5, 1, 3};
    int size = sizeof(array) / sizeof(int);
    quick(array, 0, size);

    for (int i = 0; i < size; i++) {
        std::cout << array[i] << std::endl;
    }
}
