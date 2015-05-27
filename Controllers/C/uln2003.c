#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <wiringPi.h>

#define handle_error(fmt, args...)  \
    do {                            \
        char buf[20];               \
        sprintf(buf, fmt, ##args);  \
        perror(buf);                \
        exit(EXIT_FAILURE);         \
    } while (0)

int delay[5] = {20, 15, 10, 5, 2};
const char *file_dir = "./dir.conf";
const char *file_spd = "./spd.conf";

int main(int argc, const char *argv[])
{
    int fd_dir, fd_spd;
    char *mem_dir, *mem_spd;
    int dir, spd;

    int page_sz = getpagesize();

    fd_dir = open(file_dir, O_RDONLY);
    if (fd_dir == -1) {
        handle_error("open %s", file_dir);
    }

    fd_spd = open(file_spd, O_RDONLY);
    if (fd_spd == -1) {
        handle_error("open %s", file_spd);
    }

    mem_dir = mmap(NULL, page_sz, PROT_READ, MAP_PRIVATE, fd_dir, 0);
    mem_spd = mmap(NULL, page_sz, PROT_READ, MAP_PRIVATE, fd_spd, 0);

    while (1) {
        sleep(2);

        dir = atoi(mem_dir);
        if (dir !=0 && dir != 1) {
            fprintf(stderr, "invalid dir value: %d", dir);
            exit(1);
        }
        printf("mem_dir: %d\n", dir);

        spd = atoi(mem_spd);
        if (spd < 1 || spd > 5) {
            fprintf(stderr, "invalid spd value: %d", spd);
            exit(1);
        }
        printf("mem_spd: %d\n", spd);
        printf("delay : %d\n", delay[spd - 1]);
    }

    close(fd_dir);
    close(fd_spd);
    munmap(mem_dir, page_sz);
    munmap(mem_spd, page_sz);

    return 0;
}
