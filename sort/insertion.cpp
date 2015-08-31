#include <iostream>

#define swap(array, x1, x2) { \
    int temp = array[x1]; \
    array[x1] = array[x2]; \
    array[x2] = temp; \
}

void insertion(int* array, int size)
{
    for (int i = 1; i < size; i++) {
        for (int j = i; j > 0; j--) {
            if (array[j] < array[j-1]) {
                swap(array, j, j-1);
            }
        }
    }
}

int main()
{
    int array[] = {8, 7, 5, 10, 5, 1, 3};
    int size = sizeof(array) / sizeof(int);
    insertion(array, size);

    for (int i = 0; i < size; i++) {
        std::cout << array[i] << std::endl;
    }
}
