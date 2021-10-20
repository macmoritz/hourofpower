#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>


int fromBinary(const char *s) {
  return (int) strtol(s, NULL, 2);
}

int main() {
    FILE *file;
    char line[11], row_text[8], col_text[4];
    int max_seat_ID = 0, max_row = 127, max_column = 7;
    int row, col, local_seat_ID, seat_index = 0;
    bool seat_status[850];

    file = fopen("input.txt", "r");

    while (fgets(line, 11, file)) {
        col = 0, row = 0;
        memset(&row_text[0], 0, sizeof(row_text));
        memset(&col_text[0], 0, sizeof(col_text));
        local_seat_ID = 0;
        for(int i = 0; i < 10; i++) {
            switch(line[i]) {
                case 'F':
                    row_text[i] = '0';
                    break;
                case 'B':
                    row_text[i] = '1';
                    break;
                case 'R':
                    col_text[i % 7] = '1';
                    break;
                case 'L':
                    col_text[i % 7] = '0';
                    break;
            }
        }
        row = fromBinary(row_text), col = fromBinary(col_text);
        local_seat_ID = row * 8 + col;

        if (local_seat_ID > max_seat_ID) {
            max_seat_ID = local_seat_ID;
        }

        seat_status[seat_index] = true;
        seat_index += 1;
    }

    fclose(file);
    printf("part1: %d is the highest seat ID!\n", max_seat_ID);

    for(int i = 0; i < sizeof(seat_status)/sizeof(seat_status[0]) - 2; i++) {
        if(seat_status[i - 1] && !seat_status[i] && seat_status[i + 1]) {
            printf("part2: seat ID %d is missing\n", i);
            break;
        }
    }
    return 0;
}
