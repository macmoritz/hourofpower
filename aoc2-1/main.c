#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  FILE *file;
  char line[100];
  char *rule, *passwd, letter, *occ_range;
  int valid = 0, max_occ, min_occ, occ = 0;

  file = fopen("input.txt", "r");
  
  while(fgets(line, 100, file)) {
    // printf("%s", line);
    rule = strtok(line, ":");
    passwd = strtok(NULL, ":");
    letter = rule[strlen(rule) - 1];
    occ_range = strtok(rule, " ");
    // printf("%c %s\n", letter, occ_range);
    
    min_occ = atoi(strtok(occ_range, "-"));
    max_occ = atoi(strtok(NULL, "-"));
    // printf("min_occ %d, max_occ %d\n", min_occ, max_occ);
    for(int i = 0; i < strlen(passwd); i++) {
      if(passwd[i] == letter) {
        occ += 1;
        if(occ > max_occ) break;
      } 
    }
    // printf("%d\n", occ);
    if (occ >= min_occ && occ <= max_occ) {
      valid += 1;
    }
    occ = 0;
  }
  fclose(file);
  printf("%d passwords are valid!", valid);
  return 0;
}

