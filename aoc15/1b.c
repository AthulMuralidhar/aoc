#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
  FILE *fp;
  fp = fopen("r_input.txt","r");
  int i = 0;
  int counter = 0;
  int index = 0;

  while ((i = fgetc(fp))!= EOF) {
    index +=1;
    if (i==40) {
      counter +=1;
    } else if (i==41) {
      counter -=1;
    }
    if (counter < 0) {
      break;
    }
  }

  printf("P1:%d\n",counter);
  printf("P2:%d\n",index);
  fclose(fp);
  return 0;
}
