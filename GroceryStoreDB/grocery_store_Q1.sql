USE grocery_store;

create table Products (
product_id INT NOT NULL PRIMARY KEY,
name varchar(100) NOT NULL,
units_id INT NOT NULL,
price_per_unit DOUBLE NOT NULL);

create table Units (
units_id INT NOT NULL PRIMARY KEY,
units_name varchar(45) NOT NULL);

select * from Products;

alter table grocery_store.Products
add index fk_units_id_ix (units_id ASC) VISIBLE;
;
alter table grocery_store.Products
add constraint fk_units_id foreign key (units_id) references grocery_store.Units(units_id)
ON DELETE NO ACTION
ON UPDATE RESTRICT;

create table grocery_store.Orders (
order_id INT NOT NULL PRIMARY KEY,
customer_name varchar(100) NOT NULL,
total_price DOUBLE NOT NULL,
datetime DATETIME NOT NULL);

create table grocery_store.Order_Details (
order_id INT NOT NULL PRIMARY KEY,
product_id INT NOT NULL,
quantity DOUBLE NOT NULL,
total_price DOUBLE NOT NULL);

alter table grocery_store.Order_Details
add index fk_order_id_ix (order_id ASC) VISIBLE;
;
alter table grocery_store.Order_Details
add constraint fk_order_id foreign key (order_id) references grocery_store.Orders (order_id)
ON DELETE NO ACTION
ON UPDATE RESTRICT;

alter table grocery_store.Order_Details
add index fk_product_id_ix (product_id ASC) VISIBLE;
;
alter table grocery_store.Order_Details
add constraint fk_product_id foreign key (product_id) references grocery_store.Products(product_id)
ON DELETE NO ACTION
ON UPDATE RESTRICT;