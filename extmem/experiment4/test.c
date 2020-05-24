#include <stdlib.h>
#include <stdio.h>
#include "extmem.h"

int main(int argc, char **argv)
{
    Buffer buf; /* A buffer */
    unsigned char *readBlk, *writeBlk; /* A pointer to a block */
    int i, j, k;
    int X = 0;
    int Y = 0;
    int numOfPi = 0;
    int readAddr = 201;
    int writeAddr = 301;
    char str[5];

    /* Initialize the buffer */
    if (!initBuffer(520, 64, &buf))
    {
        perror("Buffer Initialization Failed!\n");
        return -1;
    }

    writeBlk = getNewBlockInBuffer(&buf);
    for(i = 0; i < 16; i++)
    {
        readBlk = readBlockFromDisk(readAddr, &buf);
        printf("�������ݿ�%d\n", readAddr);
        readAddr++;

        for(j =  0; j < 7; j++)
        {
            for(k = 0; k < 4; k++)
            {
                str[k] = *(readBlk + j * 8 + k);
            }
            Y = atoi(str);

            if(Y != X)
            {
                printf("(x = %d)\n", Y);
                X = Y;

                for(k = 0; k < 4; k++)
                {
                    *(writeBlk + (numOfPi % 14) * 4 + k) = *(readBlk + j * 8 + k);
                }
                numOfPi++;
                if(numOfPi % 14 == 0)
                {
                    itoa(writeAddr + 1, str, 10);
                    for (k = 0; k < 4; k++)
                    {
                        *(writeBlk + 7 * 8 + k) = str[k];
                    }
                    if(writeBlockToDisk(writeBlk, writeAddr, &buf) == 0);
                    {
                        printf("�����д�����%d��\n", writeAddr);
                        writeAddr++;
                        writeBlk = getNewBlockInBuffer(&buf);
                    }
                }
            }
        }
        freeBlockInBuffer(readBlk, &buf);
    }
    itoa(writeAddr + 1, str, 10);
    for (k = 0; k < 4; k++)
    {
        *(writeBlk + 7 * 8 + k) = str[k];
    }
    if(writeBlockToDisk(writeBlk, writeAddr, &buf) == 0);
    {
        printf("�����д�����%d��\n", writeAddr);
        writeAddr++;
        writeBlk = getNewBlockInBuffer(&buf);
    }


    printf("\n");
    printf("R�ϵ�A���Ծ�ͶӰ�������ֵһ����%d��\n", numOfPi);
    printf("\n");
    printf("IO��дһ��%d��\n", buf.numIO);
    printf("\n");

    freeBuffer(&buf);
    return 0;
}

