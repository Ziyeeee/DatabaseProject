/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/5/2 18:38:21                            */
/*==============================================================*/


drop  
table  if   exists   storeView;

drop  
table  if   exists   commodityView;

drop  
table  if   exists   buyerView;

/*==============================================================*/
/* Table: Logistics                                             */
/*==============================================================*/
create table Logistics
(
   Lid                  char(8) not null,
   Oid                  char(8) not null,
   Daddress             varchar(32) not null,
   Dname                varchar(16) not null,
   DTel                 char(11) not null,
   Raddress             varchar(32) not null,
   Rname                varchar(16) not null,
   RTel                 char(11) not null,
   company              varchar(16) not null,
   Lstatus              char(4) not null,
   primary key (Lid)
);

/*==============================================================*/
/* Table: addressBook                                           */
/*==============================================================*/
create table addressBook
(
   Aid                  char(8) not null,
   Bid                  char(8) not null,
   address              varchar(32) not null,
   Rname                varchar(16) not null,
   Tel                  char(11) not null,
   postcode             char(6) not null,
   primary key (Aid)
);

/*==============================================================*/
/* Table: buyer                                                 */
/*==============================================================*/
create table buyer
(
   Bid                  char(8) not null,
   Bname                varchar(16) not null,
   Scredit              int,
   Bkey                 varchar(16) not null,
   BkeyProtect1         varchar(32),
   BkeyAns1             varchar(32),
   BkeyProtect2         varchar(32),
   BkeyAns2             varchar(32),
   primary key (Bid)
);

/*==============================================================*/
/* Table: cart                                                  */
/*==============================================================*/
create table cart
(
   Cid                  char(8) not null,
   Bid                  char(8) not null,
   size                 varchar(8),
   num                  smallint not null,
   primary key (Cid)
);

/*==============================================================*/
/* Table: Ccomment                                               */
/*==============================================================*/
create table Ccomment
(
   Commid               char(8) not null,
   Cid                  char(8) not null,
   star                 smallint not null,
   content              text not null,
   Odate                date not null,
   Otime                time not null,
   primary key (Commid)
);

/*==============================================================*/
/* Table: commodity                                             */
/*==============================================================*/
create table commodity
(
   Cid                  char(8) not null,
   Sid                  char(8) not null,
   Wid                  char(8) not null,
   stockSize            varchar(8) not null,
   Cname                varchar(16) not null,
   price                float(8,2) not null,
   discount             real,
   Cdescribe           	text,
   primary key (Cid)
);

/*==============================================================*/
/* Table: commodity_order                                       */
/*==============================================================*/
create table commodity_order
(
   Oid                  char(8) not null,
   Cid                  char(8) not null,
   primary key (Oid, Cid)
);

/*==============================================================*/
/* Table: orderForm                                               */
/*==============================================================*/
create table orderForm
(
   Oid                  char(8) not null,
   Bid                  char(8) not null,
   Sid                  char(8) not null,
   size                 varchar(8) not null,
   num                  smallint not null,
   price                float(8,2) not null,
   Odate                date not null,
   Otime                time not null,
   Lstatus              char(4) not null,
   primary key (Oid)
);

/*==============================================================*/
/* Table: store                                                */
/*==============================================================*/
create table store
(
   Sid                  char(8) not null,
   Sname                varchar(16) not null,
   Tel                  char(11) not null,
   Scredit              int,
   principal            char(16) not null,
   ID_card              char(18) not null,
   Bkey                 varchar(16) not null,
   BkeyProtect1         varchar(32),
   BkeyAns1             varchar(32),
   BkeyProtect2         varchar(32),
   BkeyAns2             varchar(32),
   primary key (Sid)
);

/*==============================================================*/
/* Table: warehouse                                             */
/*==============================================================*/
create table warehouse
(
   Wid                  char(8) not null,
   stockCid             char(8) not null,
   stockSize            varchar(8) not null,
   stock                smallint not null,
   address              varchar(32) not null,
   primary key (Wid, stockSize, stockCid)
);

/*==============================================================*/
/* View: buyerView                                              */
/*==============================================================*/
create  VIEW      buyerView
  as
select
    buyer.Bname,
    buyer.Scredit,
    commodity.Cname,
    commodity.price,
    commodity.discount,
    cart.size,
    cart.num
from
    buyer,
    commodity,
    cart
where
    buyer.Bid = cart.Bid and
    cart.Cid = commodity.Cid;

/*==============================================================*/
/* View: commodityView                                          */
/*==============================================================*/
create  VIEW      commodityView
  as
select
   store.Sname,
   store.Scredit,
   commodity.Cname,
   commodity.price,
   commodity.discount,
   commodity.Cdescribe,
   warehouse.stockSize,
   warehouse.stock
from
   store,
   commodity,
   warehouse
where
    store.Sid = commodity.Sid and
    commodity.Cid = warehouse.stockCid;

/*==============================================================*/
/* View: storeView                                              */
/*==============================================================*/
create  VIEW      storeView
  as
select
   store.Sname,
   store.Tel,
   store.Scredit,
   commodity.Cid,
   commodity.Cname,
   commodity.price,
   commodity.discount,
   warehouse.stockSize,
   warehouse.stock
from
   store,
   commodity,
   warehouse
where
   store.Sid = commodity.Sid and commodity.Cid = warehouse.stockCid;

alter table Logistics add constraint FK_order_logistics foreign key (Oid)
      references orderForm (Oid) on delete restrict on update restrict;

alter table addressBook add constraint FK_buyer_address foreign key (Bid)
      references buyer (Bid) on delete restrict on update restrict;

alter table cart add constraint FK_buyer_cart foreign key (Bid)
      references buyer (Bid) on delete restrict on update restrict;

alter table Ccomment add constraint FK_commodity_Ccomment foreign key (Cid)
      references commodity (Cid) on delete restrict on update restrict;

alter table commodity add constraint FK_store_commodity foreign key (Sid)
      references store (Sid) on delete restrict on update restrict;

alter table commodity add constraint FK_warehouse_commodity foreign key (Wid, stockSize, Cid)
      references warehouse (Wid, stockSize, stockCid) on delete restrict on update restrict;

alter table commodity_order add constraint FK_commodity_order foreign key (Oid)
      references orderForm (Oid) on delete restrict on update restrict;

alter table commodity_order add constraint FK_commodity_order2 foreign key (Cid)
      references commodity (Cid) on delete restrict on update restrict;

alter table orderForm add constraint FK_buyer_order foreign key (Bid)
      references buyer (Bid) on delete restrict on update restrict;

alter table orderForm add constraint FK_store_order foreign key (Sid)
      references store (Sid) on delete restrict on update restrict;

