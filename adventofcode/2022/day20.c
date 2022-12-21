#include <stdio.h>
#include <stdlib.h>
#include <stdlib.h>
#include <inttypes.h>

struct node {
    int64_t value;
    struct node* prev;
    struct node* next;
};

void print_list(const struct node* head) {
    const struct node* start = head;
    if (!head) {
        return;
    }

    printf("%"PRId64" ", head->value);
    const struct node* ptr = start->next;

    while (ptr != start) {
        printf("%"PRId64" ", ptr->value);
        ptr = ptr->next;
    }
    printf("\n");
}

void move_right(struct node* node) {
    // move one space right
    struct node* prev_temp = node->prev;
    struct node* next_temp = node->next;

    node->next->next->prev = node;
    node->next = node->next->next;

    node->prev = next_temp;
    next_temp->next = node;

    prev_temp->next = next_temp;
    next_temp->prev = prev_temp;
}

int64_t part1(const int64_t* numbers, size_t n, int num_mixes) {
    // Create a double-linked circular list
    // and an array of pointers to nodes (in original order)
    struct node* ptrs[n];
    for (int i = 0; i < n; i++) {
        struct node* node = (struct node*)malloc(sizeof(struct node));
        node->value = numbers[i];
        if (i > 0) {
            node->prev = ptrs[i-1];
            node->prev->next = node;
        }
        ptrs[i] = node;
    }
    ptrs[0]->prev = ptrs[n-1];
    ptrs[0]->prev->next = ptrs[0];
    // print_list(ptrs[0]);

    struct node* head = ptrs[0];
    int64_t len = n;

    for (int mixnum = 0; mixnum < num_mixes; mixnum++) {
        for (int i = 0; i < n; i++) {
            struct node* node = ptrs[i];
            struct node* ptr = node;

            int64_t mod_value = node->value % (len - 1);
            int64_t moves_right = mod_value;
            if (node->value < 0) {
                moves_right = len + mod_value - 1;
            }

            for (int64_t j = 0; j < moves_right; j++) {
                move_right(ptr);
            }
        }
        // print_list(head);
    }

    // Find 0
    struct node* ptr = head;
    while (ptr->value != 0) {
        ptr = ptr->next;
    }

    int64_t total = 0;
    for (int64_t i = 0; i <= 3000; i++) {
        if ((i != 0) && (i % 1000) == 0) {
            // printf("%d -> %d\n", i, ptr->value);
            total += ptr->value;
        }
        ptr = ptr->next;
    }

    return total;
}

int main() {
    int64_t numbers[5000];
    int numbers_index = 0;
    while (scanf("%"PRId64, &numbers[numbers_index++]) > 0);
    numbers_index--;
    // for (int i = 0; i < numbers_index; i++) {
    //     printf("%d\n", numbers[i]);
    // }
    printf("%"PRId64"\n", part1(numbers, numbers_index, 1));

    for (int i = 0; i < numbers_index; i++) {
        numbers[i] *= 811589153;
    }
    printf("%"PRId64"\n", part1(numbers, numbers_index, 10));
    return 0;
}
