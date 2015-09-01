#include <iostream>

#define swap(array, x1, x2) { \
    int temp = array[x1]; \
    array[x1] = array[x2]; \
    array[x2] = temp; \
}

void comb(int* array, int size)
{
    int c;
    do {
        c = 0;
        for (int i = 1; i < size; i++) {
            if (array[i] < array[i-1]) {
                swap(array, i, i-1);
                c++;
            }
        }
    } while (c != 0);
}

int main()
{
    int array[] = {8, 7, 5, 10, 5, 1, 3, 6};
    int size = sizeof(array) / sizeof(int);
    comb(array, size);

    for (int i = 0; i < size; i++) {
        std::cout << array[i] << std::endl;
    }
}
