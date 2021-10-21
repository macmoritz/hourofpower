#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>


int main() {
    FILE *file;
    char line[100], group_used[100], all_answers[2048];
    int all_answers_counter = 0;

    file = fopen("input.txt", "r");

    while (fgets(line, 100, file)) {
        if(line[0] == '\0') { 
            memset(&group_used[0], 0, sizeof(group_used));
        }

        for(int i = 0; i < sizeof(line)/sizeof(line[0]); i++) {
            if(memchr(group_used, line[i], sizeof(group_used))) {
                all_answers[all_answers_counter] = line[i];
                all_answers_counter += 1;
            }
        }
        
    }
    fclose(file);
    printf("part1: %lu is the sum of true answered questions!\n", sizeof(all_answers)/sizeof(all_answers[0]));

    return 0;
}
