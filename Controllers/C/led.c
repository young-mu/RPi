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

#define DIR_PREFIX  "/srv/http/Controllers/C/led_attr/"

int nGPIO = 0;

const char *file_ebl = DIR_PREFIX"enable";

int main(int argc, const char *argv[])
{
    int fd_ebl;
    char *mem_ebl;
    int ebl;
    int i;
    pid_t child;

    int page_sz = getpagesize();

    fd_ebl = open(file_ebl, O_RDWR);
    if (fd_ebl == -1) {
        handle_error("open %s", file_ebl);
    }

    mem_ebl = mmap(NULL, page_sz, PROT_WRITE | PROT_READ, MAP_SHARED, fd_ebl, 0);

    ebl = atoi(mem_ebl);
    if (ebl == 0) {
        sprintf(mem_ebl, "%d\n", 1);
        msync(mem_ebl, sizeof(int), MS_ASYNC);
    }

    wiringPiSetup();
    pinMode(nGPIO, OUTPUT);

    child = fork();
    if (0 == child) {
        while (1) {
            ebl = atoi(mem_ebl);
            if (ebl == 1) {
                digitalWrite(nGPIO, HIGH);
            } else if (ebl == 0) {
                digitalWrite(nGPIO, LOW);
                munmap(mem_ebl, page_sz);
                close(fd_ebl);
                exit(0);
            }
        }
    } else {
        ebl = atoi(mem_ebl);
        printf("{\"enable\":%d\n", ebl);
    }

    munmap(mem_ebl, page_sz);
    close(fd_ebl);

    return 0;
}
