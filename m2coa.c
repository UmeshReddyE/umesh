#include <stdio.h>
#include <math.h>
int main() {
    int block_size = 16; // words
    int cache_size = 128; // blocks
    int words_per_cache_line = 1;
    int main_memory_size =  block_size * cache_size * 1024 * cache_size; // blocks
    int address_bits = log2(main_memory_size);
    int block_offset_bits = log2(block_size);
    int num_sets = cache_size / (block_size * words_per_cache_line);
    int set_index_bits = log2(num_sets);
    int tag_bits = address_bits - block_offset_bits - set_index_bits;
    printf("Word offset: %d bits\n", block_offset_bits);
    printf("Set index: %d bits\n", set_index_bits);
    printf("Tag: %d bits\n", tag_bits);
    return 0;
}
