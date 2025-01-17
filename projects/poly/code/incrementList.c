#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  int len;
  int *data;
} list;

// returns new list, incrementing each
// item, e.g.:
//   [1,1,3,2,1]
// returns:
//   [2,2,4,3,2]
list increment(list x) {
  list r = {0, malloc(x.len * 4)};
  for (int i = 0; i < x.len; i++) {
    int v = x.data[i] + 1;
    r.data[r.len++] = v;
  }

  return r;
}

int main(void) {
  list x = {
      .len = 10,
      .data = malloc(x.len * 4),
  };

  int n = 0;
  x.data[n++] = 1;
  x.data[n++] = 1;
  x.data[n++] = 2;
  x.data[n++] = 3;
  x.data[n++] = 3;
  x.data[n++] = 4;
  x.data[n++] = 1;
  x.data[n++] = 2;
  x.data[n++] = 7;
  x.data[n++] = 1;

  list r = increment(x);
  printf("[");
  for (int i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
