#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

const uint32_t example[] = { 3,8,9,1,2,5,4,6,7 };
const uint32_t input[] = { 6,1,4,7,5,2,8,3,9 };

void print_array(const uint32_t* arr, uint32_t n) {
    printf("[");
    for (uint32_t i = 0; i < n; i++) {
        printf("%d:%d ", i, arr[i]);
    }
    printf("]\n");
}

void part1(const uint32_t* cups, uint32_t num_cups, uint32_t nmoves) {
    // Indexed by cup label.
    // Points to the label of the next cup in the circle
    uint32_t cup_next[num_cups + 1];

    cup_next[0] = 255; // index 0 is unused

    const uint32_t min_cup = 1;
    const uint32_t max_cup = 9;

    for (uint32_t i = 0; i < num_cups-1; i++) {
        cup_next[cups[i]] = cups[i+1];
    }
    cup_next[cups[num_cups-1]] = cups[0]; // loop back to first

    uint32_t current = cups[0];

    for (uint32_t i = 0; i < nmoves; i++) {
        //       ...(c)[p0,p1,p2]n...{d}...
        // next: ...(c)n...{d}[p0,p1,p2]....
        //
        // next current (n) is three positions after current
        uint32_t p0 = cup_next[current];
        uint32_t p1 = cup_next[p0];
        uint32_t p2 = cup_next[p1];
        uint32_t next_current = cup_next[p2];
        int32_t dest = (int32_t)current;
        while (1) {
            dest--;
            if (dest < min_cup) {
                dest = max_cup;
            }
            bool dest_in_picked = ((dest == p0) || (dest == p1) || (dest == p2));
            if (!dest_in_picked) {
                break;
            }
        }
        // printf("[%d] current: %d, next: %d, dest: %d, picked: [%d,%d,%d]\n",
        //         i+1, current, next_current, dest, p0,p1,p2);
        // print_array(cup_next, num_cups + 1);

        cup_next[current] = next_current;

        // [p0,p1,p2] move after dest
        uint32_t dest_next = cup_next[dest];
        cup_next[p2] = dest_next;
        cup_next[dest] = p0;

        current = next_current;
    }

    current = cup_next[1];
    for (uint32_t i = 1; i < num_cups; i++) {
        printf("%d", current);
        current = cup_next[current];
    }
    printf("\n");
}

void part2(const uint32_t* cups, uint32_t num_cups, uint32_t nmoves) {
    uint32_t* cup_next = (void*)calloc(1000001, sizeof(uint32_t));

    cup_next[0] = 0xFFFFFFFF; // index 0 is unused

    const uint32_t min_cup = 1;
    const uint32_t max_cup = 1000000;

    for (uint32_t i = 0; i < num_cups-1; i++) {
        cup_next[cups[i]] = cups[i+1];
    }
    cup_next[cups[num_cups-1]] = 10;
    for (uint32_t i = 10; i < 1000000; i++) {
        cup_next[i] = i+1;
    }
    cup_next[1000000] = cups[0]; // loop back to first

    uint32_t current = cups[0];
    for (uint32_t i = 0; i < nmoves; i++) {
        uint32_t p0 = cup_next[current];
        uint32_t p1 = cup_next[p0];
        uint32_t p2 = cup_next[p1];
        uint32_t next_current = cup_next[p2];
        int32_t dest = (int32_t)current;
        while (1) {
            dest--;
            if (dest < min_cup) {
                dest = max_cup;
            }
            bool dest_in_picked = ((dest == p0) || (dest == p1) || (dest == p2));
            if (!dest_in_picked) {
                break;
            }
        }
        cup_next[current] = next_current;
        uint32_t dest_next = cup_next[dest];
        cup_next[p2] = dest_next;
        cup_next[dest] = p0;
        current = next_current;
    }

    uint32_t a = cup_next[1];
    uint32_t b = cup_next[a];
    uint64_t prod = (uint64_t)a * (uint64_t)b;
    // printf("%d %d\n", a, b);
    printf("%llu\n", prod);

    free(cup_next);
}

#define PUZZLE_INPUT input
int main(int argc, char* argv[]) {
    part1(PUZZLE_INPUT, sizeof(PUZZLE_INPUT) / sizeof(PUZZLE_INPUT[0]), 100);
    part2(PUZZLE_INPUT, sizeof(PUZZLE_INPUT) / sizeof(PUZZLE_INPUT[0]), 10000000);
    return 0;
}
