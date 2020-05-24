#include <stdlib.h>
#include <stdio.h>
#include "extmem.h"

void createIndex(int startAddr, int numOfDataBlk, int startWriteAddr, int selectNum);
void select(int indexStartAddr, int writeAddr, int numOfDataBlk, int selectNum);

int main(int argc, char **argv)
{
    printf("利用索引文件选出R.A=30的元组：\n");
    createIndex(201, 16, 301, 30);
    select(301, 401, 16, 30);

    printf("利用索引文件选出S.C=23的元组：\n");
    createIndex(217, 32, 317, 23);
    select(317, 417, 32, 23);
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
        return;
    }

    printf("将索引块写入到");
    for(i = 0; i < numOfDataBlk / 8 ; i++)
    {
        indexBlk = getNewBlockInBuffer(&buf);
        for(j = 0; j < 8; j++)
        {
            dataBlk = readBlockFromDisk(readAddr, &buf);
            // printf("%d ", readAddr);

            *(indexBlk + j * 8 + 0) = *(dataBlk + 0);
            *(indexBlk + j * 8 + 1) = *(dataBlk + 1);
            *(indexBlk + j * 8 + 2) = *(dataBlk + 6 * 8 + 0);
            *(indexBlk + j * 8 + 3) = *(dataBlk + 6 * 8 + 1);
            itoa(readAddr, strAddr, 10);
            for (k = 0; k < 4; k++)
            {
                *(indexBlk + j * 8 + k + 4) = strAddr[k];
            }

            readAddr++;
            freeBlockInBuffer(dataBlk, &buf);
        }
        if(writeBlockToDisk(indexBlk, writeAddr, &buf) == 0)
        {
            printf("%d ", writeAddr);
            writeAddr++;
        }
    }
    printf("磁盘块中\n");
    freeBuffer(&buf);

    return;
}

void select(int indexStartAddr, int writeAddr, int numOfDataBlk, int selectNum)
{
    Buffer buf; /* A buffer */
    unsigned char *blk, *writeBlk; /* A pointer to a block */
    int dataAddr[32] = {0};
    int i, j, k;
    int max, min, finish = 0;
    int selectBlkCount = 0;
    int selectNumCount = 0;
    int X, Y;
    int indexAddr = indexStartAddr;
    char str[5];
    char num[3];

    /* Initialize the buffer */
    if (!initBuffer(520, 64, &buf))
    {
        perror("Buffer Initialization Failed!\n");
        return;
    }

    for(i = 0; i < numOfDataBlk / 8 && finish == 0; i++)
    {
        blk = readBlockFromDisk(indexAddr, &buf);
        printf("读入索引块%d\n", indexAddr);
        indexAddr++;
        for(j = 0; j < 8; j++)
        {
            for(k = 0; k < 2; k++)
            {
                num[k] = *(blk + j * 8 + k);
            }
            max = atoi(num);
            for(k = 0; k < 2; k++)
            {
                num[k] = *(blk + j * 8 + k + 2);
            }
            min = atoi(num);
            if(min > selectNum)
            {
                continue;
            }
            else if(max >= selectNum && min <= selectNum)
            {
                for(k = 0; k < 4; k++)
                {
                    str[k] = *(blk + j * 8 + k + 4);
                }
                dataAddr[selectBlkCount] = atoi(str);
                selectBlkCount++;
            }
            else
            {
                finish = 1;
            }
        }
        freeBlockInBuffer(blk, &buf);
    }

    writeBlk = getNewBlockInBuffer(&buf);
    for(i = 0; i < selectBlkCount; i++)
    {
        blk = readBlockFromDisk(dataAddr[i], &buf);
        printf("读入数据块%d\n", dataAddr[i]);
        for(j = 0; j < 7; j++)
        {
            for(k = 0; k < 4; k++)
            {
                str[k] = *(blk + j*8 + k);
            }
            X = atoi(str);
            if(X == selectNum)
            {
                for(k = 0; k < 4; k++)
                {
                    str[k] = *(blk + j*8 + 4 + k);
                }
                Y = atoi(str);
                printf("(X = %d, Y = %d)\n", X, Y);

                for(k = 0; k < 8; k++)
                {
                     *(writeBlk + selectNumCount * 8 + k) = *(blk + j * 8 + k);
                }
                selectNumCount++;
                if(selectBlkCount % 7 == 0)
                {
                    itoa(writeAddr + 1, str, 10);
                    for (k = 0; k < 4; k++)
                    {
                        *(writeBlk + 7 * 8 + k) = str[k];
                    }
                    if(writeBlockToDisk(writeBlk, writeAddr, &buf) == 0);
                    {
                        printf("将结果写入磁盘%d中\n", writeAddr);
                        writeAddr++;
                        writeBlk = getNewBlockInBuffer(&buf);
                    }
                }
            }
        }
        freeBlockInBuffer(blk, &buf);
    }
    itoa(writeAddr + 1, str, 10);
    for (k = 0; k < 4; k++)
    {
        *(writeBlk + 7 * 8 + k) = str[k];
    }
    if(writeBlockToDisk(writeBlk, writeAddr, &buf) == 0);
    {
        printf("将结果写入磁盘%d中\n", writeAddr);
        writeAddr++;
        writeBlk = getNewBlockInBuffer(&buf);
    }

    
    printf("\n");
    printf("满足选择条件的元组一共%d个\n", selectNumCount);
    printf("\n");
    printf("IO读写一共%d次\n", buf.numIO);
    printf("\n");

    freeBuffer(&buf);
    return;
}
