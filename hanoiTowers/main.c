#include <stdbool.h>
#include <stdio.h>

#define slice_count 15


void moveDisk(int disk, int from[], int to[]) {
    bool set = false;
    for(int i = slice_count - 1; i >= 0; i--) {
        if(from[i] == disk) {
            from[i] = 0;
        }
        if(to[i] == 0 && !set) {
            to[i] = disk;
            set = true;
        }
    }
}

void printTowers(int a[], int b[], int c[]) {
    for(int i = 0; i < slice_count; i++) {
        printf("\t%d\t%d\t%d\n", a[i], b[i], c[i]);
    }
    printf("\t-----------------\n\ta\tb\tc\n\n");
}

void moveTower(int n, int a[], int b[], int c[]) {
    if (n == 1) {
        moveDisk(1, a, b);
    } else {
        moveTower(n-1, a, c, b);
        moveDisk(n, a, b);
        moveTower(n-1, c, b, a);
    }
}

int main(int argc, char **argv) {
    int a[slice_count] = {};
    int b[slice_count] = {};
    int c[slice_count] = {};

    for (int i = 0; i < slice_count; i++) {
        a[i] = i + 1;
    }

    printTowers(a, b, c);
    moveTower(slice_count, a, c, b);
    printf("\n");
    printTowers(a, b, c);
    return 0;
}
