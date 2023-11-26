#include <stdio.h>
#include <stdlib.h>

long long merge(int arr[], int temp[], int left, int mid, int right) {
    int i = left;
    int j = mid + 1;
    int k = left;
    long long inversionCount = 0;

    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
            // Count inversions
            inversionCount += (mid - i + 1);
        }
    }

    while (i <= mid) {
        temp[k++] = arr[i++];
    }

    while (j <= right) {
        temp[k++] = arr[j++];
    }

    for (i = left; i <= right; i++) {
        arr[i] = temp[i];
    }

    return inversionCount;
}

long long mergeSort(int arr[], int temp[], int left, int right) {
    long long inversionCount = 0;

    if (left < right) {
        int mid = (left + right) / 2;

        inversionCount += mergeSort(arr, temp, left, mid);
        inversionCount += mergeSort(arr, temp, mid + 1, right);

        inversionCount += merge(arr, temp, left, mid, right);
    }

    return inversionCount;
}

int main() {
    int n = 100000;
    int arr[n];
    int temp[n];
    long long inversionCount = 0;

    FILE *file = fopen("merge_text.txt", "r");
    if (file == NULL) {
        fprintf(stderr, "Unable to open file.\n");
        return 1;
    }
    for (int i = 0; i < n; i++) {
        fscanf(file, "%d", &arr[i]);
    }

    fclose(file);

    //Count inversions
    inversionCount = mergeSort(arr, temp, 0, n - 1);

    printf("Number of inversions: %lld\n", inversionCount);

    return 0;
}
