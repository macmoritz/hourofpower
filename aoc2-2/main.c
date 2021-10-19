#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


int main() {
  FILE *file;
  char line[100];
  char *rule, *passwd, letter, *occ_range;
  int valid = 0, nd_occ, st_occ;

  file = fopen("input.txt", "r");
  
  while(fgets(line, 100, file)) {
    rule = strtok(line, ":");
    passwd = strtok(NULL, ":");
    letter = rule[strlen(rule) - 1];
    occ_range = strtok(rule, " ");
    printf("%c %s %s", letter, occ_range, passwd);

    st_occ = atoi(strtok(occ_range, "-"));
    nd_occ = atoi(strtok(NULL, "-"));
    printf("%d %d", st_occ, nd_occ);
    
    if((char)passwd[st_occ - 1] == (char)letter ^ (char)passwd[nd_occ - 1] == (char)letter) {
      valid += 1;
      printf("valid\n\n");
    } else {
      printf("\n");
    }
  }
  fclose(file);
  printf("%d passwords are valid!\n", valid);

  printf("%d %d %d\n", true, true, true ^ true);
  printf("%d %d %d\n", true, false, true ^ false);
  printf("%d %d %d\n", false, true, false ^ true);
  printf("%d %d %d\n", false, false, false ^ false);
  return 0;
}

