#include <stdio.h>

#define slice_count 3

int doMoves(n, start, mid, end) {
    if (n == slice_count) {
        return 0;
    }

    if (n == 1) {
        if (n % 2) {
            doMoves(n + 1, start, end, mid);
        } else {
            doMoves(n + 1, start, mid, end);
        }
    }

}

int main() {
    int a[slice_count] = {};
    int b[slice_count] = {};
    int c[slice_count] = {};

    for (int i = 0; i < slice_count; i++) {
        a[i] = i + 1;
    }

    doMoves(1, a, b, c);

    return 0;
}
