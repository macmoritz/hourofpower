#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char * trim(char * s) {
    int l = strlen(s);
    while(isspace(s[l - 1])) --l;
    while(* s && isspace(* s)) ++s, --l;
    return strndup(s, l);
}

int main() {
  FILE *file;
  char line[100];
  char *rule, *passwd, letter, *occ_range;
  int valid1 = 0, valid2 = 0, max_occ, min_occ, occ = 0;

  file = fopen("input.txt", "r");

  while(fgets(line, 100, file)) {
    rule = strtok(line, ":");
    passwd = trim(strtok(NULL, ":"));
    letter = rule[strlen(rule) - 1];
    occ_range = strtok(rule, " ");

    min_occ = atoi(strtok(occ_range, "-"));
    max_occ = atoi(strtok(NULL, "-"));
    for(int i = 0; i < strlen(passwd); i++) {
      if(passwd[i] == letter) {
        occ += 1;
        if(occ > max_occ) break;
      }
    }

    if (occ >= min_occ && occ <= max_occ) {
      valid1 += 1;
    }

    if (passwd[min_occ - 1] == letter ^ passwd[max_occ - 1] == letter) {
      valid2 += 1;
    }

    occ = 0;
  }
  fclose(file);
  printf("part1: %d passwords are valid!\n", valid1);
  printf("part2: %d passwords are valid!\n", valid2);
  return 0;
}

