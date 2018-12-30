#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  FILE *fp;
  fp = fopen("r_input.txt","r");
  int i = 0;
  while ((i = fgetc(fp))!= EOF) {
    printf("%c\n",i);
  }
  fclose(fp);
  return 0;
}
