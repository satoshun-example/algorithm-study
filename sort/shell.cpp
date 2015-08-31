#include <iostream>

#define swap(array, x1, x2) { \
    int temp = array[x1]; \
    array[x1] = array[x2]; \
    array[x2] = temp; \
}

void shell(int* array, int size)
{
    int interval = 4; // TODO
    while (interval > 0) {
        for (int i = interval; i < size; i+=interval) {
            for (int j = i; j > 0; j-=interval) {
                if (array[j] < array[j-interval]) {
                    swap(array, j, j-interval);
                }
            }
        }

        interval /= 2;
    }
}

int main()
{
    int array[] = {8, 7, 5, 10, 5, 1, 3};
    int size = sizeof(array) / sizeof(int);
    shell(array, size);

    for (int i = 0; i < size; i++) {
        std::cout << array[i] << std::endl;
    }
}
