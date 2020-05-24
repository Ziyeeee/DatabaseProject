#include <stdlib.h>
#include <stdio.h>
#include "extmem.h"

void sort(unsigned char *blk[8], int numOfMember);

int main(int argc, char **argv)
{
    Buffer buf; /* A buffer */
    unsigned char *blk[8] = {NULL}; /*pointers to a block */
    int numOfMember = 4;
    int addr = 1;
    int writeAddr = 101;
    int i, j, k;
    char str[5];
    int blkCount[5] = {0};

    /* Initialize the buffer */
    if(!initBuffer(520, 64, &buf))
    {
        perror("Buffer Initialization Failed!\n");
        return -1;
    }

    printf("对关系R的子表按R.A从大到小顺序进行排序：\n");
    printf("将进行组内排序后的数据写入到");
    for(i = 0; i < 4; i++)
    {
        for(j = 0; j < numOfMember; j++)
        {
            blk[j] = readBlockFromDisk(addr, &buf);
            addr++;
        }
        sort(blk, numOfMember);
        for(j = 0; j < numOfMember; j++)
        {
            itoa(writeAddr + 1, str, 10);
            for(k = 0; k < 4; k++)
            {
                *(blk[j] + 8 * 7 + k) = str[k];
            }
            if(writeBlockToDisk(blk[j], writeAddr, &buf) == 0)
            {
                printf("%d ", writeAddr);
                writeAddr++;
            }
            freeBlockInBuffer(blk[j], &buf);
        }
    }
    printf("磁盘块中\n");
    freeBuffer(&buf);

    numOfMember = 8;
    addr = 17;
    writeAddr = 117;
    for(i = 0; i < 5; i++)
    {
        blkCount[i] = 0;
    }

    /* Initialize the buffer */
    if(!initBuffer(520, 64, &buf))
    {
        perror("Buffer Initialization Failed!\n");
        return -1;
    }

    printf("\n对关系S的子表按S.C从大到小顺序进行排序：\n");
    printf("将进行组内排序后的数据写入到");
    for(i = 0; i < 4; i++)
    {
        for(j = 0; j < numOfMember; j++)
        {
            blk[j] = readBlockFromDisk(addr, &buf);
            addr++;
        }
        sort(blk, numOfMember);
        for(j = 0; j < numOfMember; j++)
        {
            itoa(writeAddr + 1, str, 10);
            for(k = 0; k < 4; k++)
            {
                *(blk[j] + 8 * 7 + k) = str[k];
            }
            if(writeBlockToDisk(blk[j], writeAddr, &buf) == 0)
            {
                printf("%d ", writeAddr);
                writeAddr++;
            }
            freeBlockInBuffer(blk[j], &buf);
        }
    }
    printf("磁盘块中\n");
    freeBuffer(&buf);
    return 0;
}

void sort(unsigned char *blk[8], int numOfMember)
{
    int i, j, k, m, n;
    int X, Y;
    int maxPosi, maxPosj, unchanged;
    char str[5];
    char temp;

    for(i = 0; i < numOfMember; i++)
    {
        for(j = 0; j < 7; j++)
        {
            for(k = 0; k < 4; k++)
            {
                str[k] = *(blk[i] + j*8 + k);
            }
            X = atoi(str);
            unchanged = 1;

            n = j + 1;
            for(m = i; m < numOfMember; m++)
            {
                while(n < 7)
                {
                    for(k = 0; k < 4; k++)
                    {
                        str[k] = *(blk[m] + n*8 + k);
                    }
                    Y = atoi(str);
                    if(Y > X)
                    {
                        maxPosi = m;
                        maxPosj = n;
                        X = Y;
                        unchanged = 0;
                        // printf("%d, %d ", m, n);
                    }
                    n++;
                }
                n = 0;
            }
            // printf("\n%d, %d\n", maxPosi, maxPosj);
            if(unchanged == 0)
            {
                for(k = 0; k < 8; k++)
                {
                    temp = *(blk[i] + j*8 + k);
                    *(blk[i] + j*8 + k) = *(blk[maxPosi] + maxPosj*8 + k);
                    *(blk[maxPosi] + maxPosj*8 + k) = temp;
                }
            }
            // printf("%d ", X);
        }
        // printf("\n");
    }
/*  查看排序结果
    for(i = 0; i < numOfMember; i++)
    {
        for(j = 0; j < 7; j++)
        {
            for(k = 0; k < 4; k++)
            {
                str[k] = *(blk[i] + j*8 + k);
            }
            X = atoi(str);
            printf("%d ", X);
        }
    }
    printf("\n");
*/
    return;
}
