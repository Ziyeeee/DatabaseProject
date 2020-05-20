# 数据库实验四 查询处理算法的模拟实现

## ExtMem程序库介绍

ExtMem程序库是一个专门为本课程编写的模拟外存磁盘块存储和存取的程序库，由C语言开发。ExtMem程序库的功能包括内存缓冲区管理、磁盘块读/写，它提供了1个数据结构和7个API函数。

ExtMem程序库定义了Buffer数据类型，包含如下6个域：

* numIO：外存I/O次数；  

* bufSize：缓冲区大小（单位：字节）；

* blkSize：块的大小（单位：字节）；

* numAllBlk：缓冲区内可存放的最多块数；

* numFreeBlk：缓冲区内可用的块数；

* data：缓冲区内存区域。

缓冲区中每个块内数据大小为blkSize个字节，其最后4个字节用来存放其后继磁盘块的地址（在ExtMem库中，我们4个字节来记录磁盘块地址，地址在程序中为unsigned int类型。若无后继磁盘块，则置为0），其余(blkSize – 4)个字节用于存放块内的记录。缓冲区每个块之前有1个字节的标志位表示是否被占用。

ExtMem库提供了如下API函数：

* ```c
  Buffer *initBuffer(size_t bufSize, size_t blkSize, Buffer *buf);
  ```

> 初始化缓冲区，其输入参数bufSize为缓冲区大小（单位：字节），blkSize为块的大小（单位：字节），buf为指向待初始化的缓冲区的指针。若缓冲区初始化成功，则该函数返回指向该缓冲区的地址；否则，返回NULL。

* ```c
  void freeBuffer(Buffer *buf);
  ```

> 释放缓冲区buf占用的内存空间。

* ```c
  unsigned char *getNewBlockInBuffer(Buffer *buf);
  ```

> 在缓冲区buf中申请一个新的块。若申请成功，则返回该块的起始地址；否则，返回NULL。

* ```c
  void freeBlockInBuffer(unsigned char *blk, Buffer *buf);
  ```

> 解除块blk对缓冲区内存的占用，即将blk占据的内存区域标记为可用。

* ```c
  int dropBlockOnDisk(unsigned int addr);
  ```

> 从磁盘上删除地址为addr的磁盘块内的数据。若删除成功，则返回0；否则，返回-1。

* ```c
  unsigned char *readBlockFromDisk(unsigned int addr, Buffer *buf);
  ```

> 将磁盘上地址为addr的磁盘块读入缓冲区buf。若读取成功，则返回缓冲区内该块的地址；否则，返回NULL。同时，缓冲区buf的I/O次数加1。

* ```c
  int writeBlockToDisk(unsigned char *blkPtr, unsigned int addr, Buffer *buf);
  ```

> 将缓冲区buf内的块blk写入磁盘上地址为addr的磁盘块。若写入成功，则返回0；否则，返回-1。同时，缓冲区buf的I/O次数加1。

文件experimentTest/test.c中给出了ExtMem库使用方法的具体示例。

## 数据准备

本实验使用ExtMem程序库已预先建立了关系R和S的物理存储。关系的物理存储形式为磁盘块序列B1, B2, …, Bn，其中Bi的最后4个字节存放Bi+1的地址。  
extmem-c\data下的每个文件模拟一个磁盘块。R和S的每个元组的大小均为8个字节。每个磁盘块大小为64个字节，可存放7个元组和1个后继磁盘块地址。  
初始化缓冲区块的大小为64个字节，缓冲区大小设置为64*8+8=520个字节。其中8个字节为标志位，表示每个块是否被占用。这样，每块可存放7个元组和1个后继磁盘块地址，缓冲区内可最多存放8个块。  
本实验已随机生成关系R和S，R中包含16 * 7 = 112个元组，S中包含32 * 7 = 224个元组。extmem-c\data目录下文件1.blk至16.blk 为关系R的元组数据，文件17.blk至48.blk 为关系S的元组数据。数据经过手工修改，关系R和S有9个相同元组，分别是：  
(22, 712)、(23, 758)、(25, 440)、(30, 703)、(30, 617)、(30, 624)、(34, 665)、(36, 895)、(40, 557)

## 基础题

### 1. 基于线性搜索的关系选择算法

选出R.A=30或S.C=23的元组，记录IO读写次数，并将选择结果存放在磁盘上。

1. 读取一块磁盘数据到缓冲区
2. 依次检查元组是否满足条件
3. 将满足条件的元组保留在缓冲区中
4. 转到步骤1，直至读完所有的磁盘数据
5. 将缓冲区的元组写入到磁盘
6. 显示磁盘存储地址及IO次数