#include <stdlib.h>
#include <stdio.h>
#include "extmem.h"

void sort(unsigned char *blk[8], int numOfMember);
void intersect();

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

    printf("�Թ�ϵR���ӱ�R.A�Ӵ�С˳���������\n");
    printf("��������������������д�뵽");
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
    printf("���̿���\n");
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

    printf("\n�Թ�ϵS���ӱ�S.C�Ӵ�С˳���������\n");
    printf("��������������������д�뵽");
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
    printf("���̿���\n");
    freeBuffer(&buf);
    printf("\n��������Ľ�������\n");
    intersect();
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
/*  �鿴������
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

void intersect()
{
    Buffer buf; /* A buffer */
    unsigned char *blk[8] = {NULL}; /*pointers to a block */
    int readRAddr = 101;
    int readSAddr[4] = {117, 125, 133, 141};
    int writeAddr = 201;
    int i, j, k;
    int A, B, C, D;
    char str[5];
    int blkCount[6] = {0};
    int notFinish = 1;
    int intersectCount = 0;

    /* Initialize the buffer */
    if(!initBuffer(520, 64, &buf))
    {
        perror("Buffer Initialization Failed!\n");
        return;
    }

    blk[5] = getNewBlockInBuffer(&buf);
    while(readRAddr < 117)
    {
        blk[4] = readBlockFromDisk(readRAddr, &buf);
        readRAddr++;
        blkCount[4] = 0;

        while(blkCount[4] < 7)
        {
            for(k = 0; k < 4; k++)
            {
                str[k] = *(blk[4] + blkCount[4] * 8 + k);
                blkCount[k] = 0;
            }
            A = atoi(str);

            for(i = 0; i < 4; i++)
            {
                readSAddr[i] = 117 + i * 8;
                blk[i] = readBlockFromDisk(readSAddr[i], &buf);
                readSAddr[i]++;
            }

            while(1)
            {
                // S�Ƿ��Ѿ���ȫ����
                notFinish = 0;
                for(i = 0; i < 4; i++)
                {
                    if(blkCount[i] < 7)
                    {
                        notFinish = 1;
                    }
                }
                if(!notFinish)
                {
                    break;
                }

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
                        C = atoi(str);
                        // printf("%d %d %d\n", C, readSAddr[i], blkCount[i]);
                        if(A == C)
                        {
                            for(k = 0; k < 4; k++)
                            {
                                str[k] = *(blk[i] + blkCount[i] * 8 + k + 4);
                            }
                            B = atoi(str);
                            for(k = 0; k < 4; k++)
                            {
                                str[k] = *(blk[4] + blkCount[4] * 8 + k + 4);
                            }
                            D = atoi(str);

                            if(B == D)
                            {
                                intersectCount++;
                                printf("(X = %d, Y = %d)\n", A, B);
                                for(k = 0; k < 8; k++)
                                {
                                    *(blk[5] + blkCount[5]*8 + k) = *(blk[4] + blkCount[4] * 8 + k);
                                }
                                blkCount[5]++;

                                if(blkCount[5] == 7)
                                {
                                    // ���뻺����
                                    itoa(writeAddr + 1, str, 10);
                                    for(k = 0; k < 4; k++)
                                    {
                                        *(blk[5] + 8 * 7 + k) = str[k];
                                    }
                                    if(writeBlockToDisk(blk[5], writeAddr, &buf) == 0)
                                    {
                                        printf("���д�����%d\n", writeAddr);
                                        writeAddr++;
                                        blk[5] = getNewBlockInBuffer(&buf);
                                    }
                                    blkCount[5] = 0;
                                }
                            }
                        }
                        else if(A > C)
                        {
                            blkCount[i] = 7;
                        }

                        // ����һλ
                        if((blkCount[i] == 6) && (readSAddr[i] % 8 != 5))
                        {
                            freeBlockInBuffer(blk[i], &buf);
                            blk[i] = readBlockFromDisk(readSAddr[i], &buf);
                            readSAddr[i]++;
                            blkCount[i] = 0;
                        }
                        else if(blkCount[i] != 7)
                        {
                            blkCount[i]++;
                        }
                    }
                }
            }
            for(k = 0; k < 4; k++)
            {
                freeBlockInBuffer(blk[k], &buf);
            }
            blkCount[4]++;
        }
        freeBlockInBuffer(blk[4], &buf);
    }

    itoa(writeAddr + 1, str, 10);
    for(k = 0; k < 4; k++)
    {
        *(blk[5] + 8 * 7 + k) = str[k];
    }
    if(writeBlockToDisk(blk[5], writeAddr, &buf) == 0)
    {
        printf("���д�����%d\n", writeAddr);
        writeAddr++;
        blk[5] = getNewBlockInBuffer(&buf);
    }
    blkCount[5] = 0;
    freeBuffer(&buf);
    printf("\nR��S�Ľ����ܹ���%d��Ԫ��", intersectCount);
    return;
}
