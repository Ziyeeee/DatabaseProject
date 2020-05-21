#include <stdlib.h>
#include <stdio.h>
#include "extmem.h"

void sort(unsigned char *blk[8], int numOfMember);

int main(int argc, char **argv)
{
    Buffer buf; /* A buffer */
    unsigned char *blk[8]; /*pointers to a block */
    int numOfMember = 4;
    int addr = 1;
    int i, j;

    /* Initialize the buffer */
    if(!initBuffer(520, 64, &buf))
    {
        perror("Buffer Initialization Failed!\n");
        return -1;
    }

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
            freeBlockInBuffer(blk[j], &buf);
        }
    }


    return 0;
}

void sort(unsigned char *blk[8], int numOfMember)
{
    int i, j, k, m, n;
    int X, Y;
    int maxPosi, maxPosj;
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
                    }
                    n++;
                }
                n = 0;
            }
            for(k = 0; k < 8; k++)
            {
                temp = *(blk[i] + j*8 + k);
                *(blk[i] + j*8 + k) = *(blk[maxPosi] + maxPosj*8 + k);
                *(blk[maxPosi] + maxPosj*8 + k) = temp;
            }
        }
    }

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

    return;
}
