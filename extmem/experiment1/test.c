#include <stdlib.h>
#include <stdio.h>
#include "extmem.h"

int main(int argc, char **argv)
{
    Buffer buf; /* A buffer */
    unsigned char *blk, *selectBlk; /* A pointer to a block */
    int i, j, k;
    int byteCount = 0;
    int count = 0;
    int selectAddr = 49;
    char strAddr[5], str[5];
    int X = -1;
    int Y = -1;

    printf("�������������Ĺ�ϵѡ���㷨R.A=30\n");
    /* Initialize the buffer */
    if (!initBuffer(520, 64, &buf))
    {
        perror("Buffer Initialization Failed!\n");
        return -1;
    }
    if (!(selectBlk = getNewBlockInBuffer(&buf)))
    {
        printf("Get Blk Failed!\n");
    }

    for (i = 0; i < 16; i++)
    {
        if ((blk = readBlockFromDisk(i + 1, &buf)))
        {
            printf("�������ݿ�%d\n", i + 1);
            for (j = 0; j < 7; j++)
            {
                for (k = 0; k < 4; k++)
                {
                    str[k] = *(blk + j*8 + k);
                }
                X = atoi(str);

                if (X == 30)
                {
                    count++;
                    for (k = 0; k < 4; k++)
                    {
                        str[k] = *(blk + j*8 + 4 + k);
                    }
                    Y = atoi(str);
                    printf("(%d, %d) \n", X, Y);
                    if (byteCount < 8)
                    {
                        for (k = 0; k < 4; k++)
                        {
                            *(selectBlk + byteCount*8 + k) = *(blk + j*8 + k);
                            *(selectBlk + byteCount*8 + 4 + k) = *(blk + j*8 + 4 + k);
                        }
                        byteCount++;
                    }
                    else
                    {
                        itoa(selectAddr + 1, strAddr, 10);
                        for (k = 0; k < 4; k++)
                        {
                            *(selectBlk + byteCount*8 + k) = strAddr[k];
                        }
                        if (writeBlockToDisk(selectBlk, selectAddr, &buf) == 0);
                        {
                            printf("�������������д����̣�%d\n", selectAddr);
                            selectAddr++;
                        }
                        freeBlockInBuffer(selectBlk, &buf);
                        if ((selectBlk = getNewBlockInBuffer(&buf)))
                        {
                            printf("Get Blk Failed!\n");
                        }
                        byteCount = 0;
                    }
                }
            }
        }
        freeBlockInBuffer(blk, &buf);
    }

    if (writeBlockToDisk(selectBlk, selectAddr, &buf) == 0)
    {
        printf("�����д����̣�%d\n", selectAddr);
        selectAddr++;
    }
    printf("\n");
    printf("����ѡ��������Ԫ��һ����%d��\n", count);
    printf("\n");
    printf("IO��дһ��%d��\n", buf.numIO); /* Check the number of IO's */

    freeBlockInBuffer(selectBlk, &buf);
    freeBlockInBuffer(blk, &buf);
    freeBuffer(&buf);

    printf("\n�������������Ĺ�ϵѡ���㷨S.C=23\n");
    count = 0;
    byteCount = 0;
    if (!initBuffer(520, 64, &buf))
    {
        perror("Buffer Initialization Failed!\n");
        return -1;
    }

    if (!(selectBlk = getNewBlockInBuffer(&buf)))
    {
        printf("Get Blk Failed!\n");
    }

    for (i = 16; i < 48; i++)
    {
        if ((blk = readBlockFromDisk(i + 1, &buf)))
        {
            printf("�������ݿ�%d\n", i + 1);
            for (j = 0; j < 7; j++)
            {
                for (k = 0; k < 4; k++)
                {
                    str[k] = *(blk + j*8 + k);
                }
                X = atoi(str);

                if (X == 23)
                {
                    count++;
                    for (k = 0; k < 4; k++)
                    {
                        str[k] = *(blk + j*8 + 4 + k);
                    }
                    Y = atoi(str);
                    printf("(%d, %d) \n", X, Y);
                    if (byteCount < 8)
                    {
                        for (k = 0; k < 4; k++)
                        {
                            *(selectBlk + byteCount*8 + k) = *(blk + j*8 + k);
                            *(selectBlk + byteCount*8 + 4 + k) = *(blk + j*8 + 4 + k);
                        }
                        byteCount++;
                    }
                    else
                    {
                        itoa(selectAddr + 1, strAddr, 10);
                        for (k = 0; k < 4; k++)
                        {
                            *(selectBlk + byteCount*8 + k) = strAddr[k];
                        }
                        if (writeBlockToDisk(selectBlk, selectAddr, &buf) == 0);
                        {
                            printf("�������������д����̣�%d\n", selectAddr);
                            selectAddr++;
                        }
                        freeBlockInBuffer(selectBlk, &buf);
                        if ((selectBlk = getNewBlockInBuffer(&buf)))
                        {
                            printf("Get Blk Failed!\n");
                        }
                        byteCount = 0;
                    }
                }
            }
        }
        freeBlockInBuffer(blk, &buf);
    }

    if (writeBlockToDisk(selectBlk, selectAddr, &buf) == 0)
    {
        printf("�����д����̣�%d\n", selectAddr);
    }
    printf("\n");
    printf("����ѡ��������Ԫ��һ����%d��\n", count);
    printf("\n");
    printf("IO��дһ��%d��\n", buf.numIO); /* Check the number of IO's */

    freeBlockInBuffer(selectBlk, &buf);
    freeBlockInBuffer(blk, &buf);
    freeBuffer(&buf);
    return 0;
}

