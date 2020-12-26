#include <stdio.h>
#define UPPER_BOUND 1000001

int remove_next(int *next_arr, int n) {
  int i = next_arr[n];
  next_arr[n] = next_arr[next_arr[n]];
  return i;
}

int insert_next(int *next_arr, int node, int n) {
  next_arr[n] = next_arr[node];
  next_arr[node] = n;
}

int main() {
  int next_arr[UPPER_BOUND];
  int min_cup = 1;
  int max_cup = 1000000;
  const int input_list[] = {9, 4, 2, 3, 8, 7, 6, 1, 5};

  for(int i = 0; i < sizeof(input_list) / sizeof(int) - 1; i++) {
    next_arr[input_list[i]] = input_list[i+1];
  }
  next_arr[input_list[(sizeof(input_list) / sizeof(int)) - 1]] = 10;
  for(int i = 10; i < 1000000; i++) {
    next_arr[i] = i+1;
  }
  next_arr[UPPER_BOUND-1] = 9;

  int current_cup = 9;
  const int moves = 10000000;

  int picked_up[3];
  for(int m = 0; m < moves; m++) {
    for(int i = 0; i < 3; i++) {
      picked_up[i] = remove_next(next_arr, current_cup);
    }

    int dest_cup = current_cup - 1;
    while(1) {
      char in_picked_up = 0;
      for(int i = 0; i < 3; i++) {
        if(dest_cup == picked_up[i]) {
          in_picked_up = 1;
          break;
        }
      }
      if(!in_picked_up && dest_cup >= min_cup)
        break;

      dest_cup--;

      if(dest_cup < min_cup) {
        dest_cup = max_cup;
      }
    }

    for(int i = 2; i >= 0; i--) {
      insert_next(next_arr, dest_cup, picked_up[i]);
    }

    current_cup = next_arr[current_cup];
  }

  printf("%lu\n", ((unsigned long) next_arr[1]) * ((unsigned long) next_arr[next_arr[1]]));
  return 0;
}
