#include <iostream>

void bubble(int* array, int size)
{
    for (int i = 0; i < size; i++) {
        for (int j = 1; j < size; j++) {
            if (array[j-1] > array[j]) {
                int temp = array[j];
                array[j] = array[j-1];
                array[j-1] = temp;
            }
        }
    }
}

int main()
{
    int array[] = {8, 7, 5, 10, 5, 1, 3};
    int size = sizeof(array) / sizeof(int);
    bubble(array, size);

    for (int i = 0; i < size; i++) {
        std::cout << array[i] << std::endl;
    }
}
