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

int nGPIOs[4] = {0, 1, 2, 3};

const char *file_ebl = "/srv/http/Controllers/C/uln2003_attr/enable";
const char *file_dir = "/srv/http/Controllers/C/uln2003_attr/direction";
const char *file_spd = "/srv/http/Controllers/C/uln2003_attr/speed";

int dlyMS[5] = {20, 15, 10, 5, 2};

int CW_seq[4][4] = {{1, 0, 0, 0},
                    {0, 1, 0, 0},
                    {0, 0, 1, 0},
                    {0, 0, 0, 1}};
int CCW_seq[4][4] = {{0, 0, 0, 1},
                     {0, 0, 1, 0},
                     {0, 1, 0, 0},
                     {1, 0, 0, 0}};
int (*seq[2])[4] = {CW_seq, CCW_seq};

int main(int argc, const char *argv[])
{
    int fd_ebl, fd_dir, fd_spd;
    char *mem_ebl, *mem_dir, *mem_spd;
    int ebl, dir, spd;
    int i, j;

    int page_sz = getpagesize();

    fd_ebl = open(file_ebl, O_RDWR);
    if (fd_ebl == -1) {
        handle_error("open %s", file_ebl);
    }
    fd_dir = open(file_dir, O_RDONLY);
    if (fd_dir == -1) {
        handle_error("open %s", file_dir);
    }
    fd_spd = open(file_spd, O_RDONLY);
    if (fd_spd == -1) {
        handle_error("open %s", file_spd);
    }

    mem_ebl = mmap(NULL, page_sz, PROT_WRITE | PROT_READ, MAP_SHARED, fd_ebl, 0);
    mem_dir = mmap(NULL, page_sz, PROT_READ, MAP_PRIVATE, fd_dir, 0);
    mem_spd = mmap(NULL, page_sz, PROT_READ, MAP_PRIVATE, fd_spd, 0);

    ebl = atoi(mem_ebl);
    if (ebl == 0) {
        sprintf(mem_ebl, "%d\n", 1);
        msync(mem_ebl, sizeof(int), MS_ASYNC);
    }

    wiringPiSetup();
    for (i = 0; i < 4; i++) {
        pinMode(nGPIOs[i], OUTPUT);
    }

    ebl = atoi(mem_ebl);
    dir = atoi(mem_dir);
    spd = atoi(mem_spd);
    printf("{\"enable\":%d, \"direction\":%d, \"speed\":%d}\n", ebl, dir, spd);

    while (1) {
        ebl = atoi(mem_ebl);
        if (ebl == 1) {
            dir = atoi(mem_dir);
            spd = atoi(mem_spd);
            for (i = 0; i < 4; i++) {
                for (j = 0; j < 4; j++) {
                    digitalWrite(nGPIOs[j], seq[dir][i][j]);
                }
                delay(dlyMS[spd - 1]);
            }
        } else if (ebl == 0) {
            for (i = 0; i < 4; i++) {
                digitalWrite(nGPIOs[i], 0);
            }
            exit(0);
        }
    }

    munmap(mem_ebl, page_sz);
    munmap(mem_dir, page_sz);
    munmap(mem_spd, page_sz);

    close(fd_ebl);
    close(fd_dir);
    close(fd_spd);

    return 0;
}
