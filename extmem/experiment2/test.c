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
    int notFinish = 1;
    int readAddr[4] = {101, 105, 109, 113};
    int blkCount[5] = {0};
    int max, X, maxPos, changed;

    /* Initialize the buffer */
    if(!initBuffer(520, 64, &buf))
    {
        perror("Buffer Initialization Failed!\n");
        return -1;
    }

    printf("对关系R按R.A从大到小顺序进行排序：\n");
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

    printf("排序后的数据写入到");
    writeAddr = 201;
    blk[4] = getNewBlockInBuffer(&buf);
    for(i = 0; i < 4; i++)
    {
        blk[i] = readBlockFromDisk(readAddr[i], &buf);
        readAddr[i]++;
    }
    while(1)
    {
        notFinish = 0;
        for(i = 0; i < 4; i++)
        {
            if(readAddr[i] % numOfMember != 1 || blkCount[i] < 7)
            {
                notFinish = 1;
            }
        }
        if(!notFinish)
        {
            break;
        }

        changed = 0;
        for(i = 0; i < 4; i++)
        {
            if(blkCount[i] > 6)
            {
                continue;
            }
            else
            {
                for(k = 0; k < 4; k++)
                {
                    str[k] = *(blk[i] + blkCount[i] * 8 + k);
                }
                X = atoi(str);
                // printf("%d, %d ", X, i);
                if(X > max || changed == 0)
                {
                    max = X;
                    maxPos = i;
                    changed = 1;
                }
            }
        }

        // printf("%d ", max);

        // 最大值存入缓冲区
        for(k = 0; k < 8; k++)
        {
            *(blk[4] + blkCount[4]*8 + k) = *(blk[maxPos] + blkCount[maxPos] * 8 + k);
        }

        blkCount[4]++;
        if(blkCount[4] == 7)
        {
            itoa(writeAddr + 1, str, 10);
            for(k = 0; k < 4; k++)
            {
                *(blk[4] + 8 * 7 + k) = str[k];
            }
            if(writeBlockToDisk(blk[4], writeAddr, &buf) == 0)
            {
                printf("%d ", writeAddr);
                writeAddr++;
                blk[4] = getNewBlockInBuffer(&buf);
            }
            blkCount[4] = 0;
        }
        // 取出最大值后移一位
        if((blkCount[maxPos] == 6) && (readAddr[maxPos] % numOfMember != 1))
        {
            freeBlockInBuffer(blk[maxPos], &buf);
            blk[maxPos] = readBlockFromDisk(readAddr[maxPos], &buf);
            //printf("\n%d, %d ", readAddr[maxPos], maxPos);
            /*
            for(i = 0; i < 7; i++)
            {
                for(k = 0; k < 4; k++)
                {
                    str[k] = *(blk[maxPos] + i * 8 + k);
                }
                printf("%d ", atoi(str));
            }
            */
            readAddr[maxPos]++;
            blkCount[maxPos] = 0;
        }
        else
        {
            blkCount[maxPos]++;
        }
    }
    printf("磁盘块中\n");
    printf("IO读写一共%d次\n", buf.numIO);
    freeBuffer(&buf);


    numOfMember = 8;
    addr = 17;
    writeAddr = 117;
    notFinish = 1;
    readAddr[0] = 117;
    readAddr[1] = 125;
    readAddr[2] = 133;
    readAddr[3] = 141;
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

    printf("\n对关系S按S.C从大到小顺序进行排序：\n");
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

    printf("排序后的数据写入到");
    writeAddr = 217;
    blk[4] = getNewBlockInBuffer(&buf);
    for(i = 0; i < 4; i++)
    {
        blk[i] = readBlockFromDisk(readAddr[i], &buf);
        readAddr[i]++;
    }
    while(1)
    {
        notFinish = 0;
        for(i = 0; i < 4; i++)
        {
            if(readAddr[i] % numOfMember != 5 || blkCount[i] < 7)
            {
                notFinish = 1;
            }
        }
        if(!notFinish)
        {
            break;
        }

        changed = 0;
        for(i = 0; i < 4; i++)
        {
            if(blkCount[i] > 6)
            {
                continue;
            }
            else
            {
                for(k = 0; k < 4; k++)
                {
                    str[k] = *(blk[i] + blkCount[i] * 8 + k);
                }
                X = atoi(str);
                // printf("%d, %d ", X, i);
                if(X > max || changed == 0)
                {
                    max = X;
                    maxPos = i;
                    changed = 1;
                }
            }
        }

        // printf("%d ", max);

        // 最大值存入缓冲区
        for(k = 0; k < 8; k++)
        {
            *(blk[4] + blkCount[4]*8 + k) = *(blk[maxPos] + blkCount[maxPos] * 8 + k);
        }

        blkCount[4]++;
        if(blkCount[4] == 7)
        {
            itoa(writeAddr + 1, str, 10);
            for(k = 0; k < 4; k++)
            {
                *(blk[4] + 8 * 7 + k) = str[k];
            }
            if(writeBlockToDisk(blk[4], writeAddr, &buf) == 0)
            {
                printf("%d ", writeAddr);
                writeAddr++;
                blk[4] = getNewBlockInBuffer(&buf);
            }
            blkCount[4] = 0;
        }
        // 取出最大值后移一位
        if((blkCount[maxPos] == 6) && (readAddr[maxPos] % numOfMember != 5))
        {
            freeBlockInBuffer(blk[maxPos], &buf);
            blk[maxPos] = readBlockFromDisk(readAddr[maxPos], &buf);
            // printf("\n%d, %d ", readAddr[maxPos], maxPos);
            /*
            for(i = 0; i < 7; i++)
            {
                for(k = 0; k < 4; k++)
                {
                    str[k] = *(blk[maxPos] + i * 8 + k);
                }
                printf("%d ", atoi(str));
            }
            */
            readAddr[maxPos]++;
            blkCount[maxPos] = 0;
        }
        else
        {
            blkCount[maxPos]++;
        }
    }
    printf("磁盘块中\n");
    printf("IO读写一共%d次\n", buf.numIO);
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
