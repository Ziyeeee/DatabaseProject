#include <stdlib.h>
#include <stdio.h>
#include "extmem.h"

void createIndex(int startAddr, int numOfDataBlk, int selectNum);
void select(int indexStartAddr, int writeAddr, int numOfDataBlk, int selectNum);

int main(int argc, char **argv)
{
    Buffer buf; /* A buffer */
    unsigned char *blk; /* A pointer to a block */
    int i = 0;

    /* Initialize the buffer */
    if (!initBuffer(520, 64, &buf))
    {
        perror("Buffer Initialization Failed!\n");
        return -1;
    }
    return 0;
}


void createIndex(int startReadAddr, int numOfDataBlk, int startWriteAddr, int selectNum)
{
    Buffer buf; /* A buffer */
    unsigned char *dataBlk, *indexBlk; /* A pointer to a block */
    int i, j, k;
    int readAddr = startReadAddr;
    int writeAddr = startWriteAddr;
    char strAddr[5];

    /* Initialize the buffer */
    if (!initBuffer(520, 64, &buf))
    {
        perror("Buffer Initialization Failed!\n");
        return -1;
    }

    printf("将索引块写入到");
    for(i = 0; i < numOfDataBlk / 8 < i++)
    {
        indexBlk = getNewBlockInBuffer(&buf);
        for(j = 0; j < 8; i++)
        {
            dataBlk = readBlockFromDisk(readAddr, &buf);

            *(indexBlk + i * 8 + 0) = *(dataBlk + 0);
            *(indexBlk + i * 8 + 1) = *(dataBlk + 1);
            *(indexBlk + i * 8 + 2) = *(dataBlk + 6 * 8 + 0);
            *(indexBlk + i * 8 + 3) = *(dataBlk + 6 * 8 + 1);
            itoa(readAddr, strAddr, 10);
            for (k = 0; k < 4; k++)
            {
                *(indexBlk + i * 8 + k + 4) = strAddr[k];
            }

            readAddr++;
            freeBlockInBuffer(dataBlk, &buf);
        }
        writeBlockToDisk(indexBlk, writeAddr, &buf);
        printf("%d ");
        writeAddr++;
    }
    printf("磁盘块中\n");

    select(startWriteAddr, 100 + startWriteAddr, numOfDataBlk, selectNum);
    return;
}

void select(int indexStartAddr, int writeAddr, int numOfDataBlk, int selectNum)
{

}
