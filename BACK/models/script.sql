create database arsalud;
use arsalud;
create table categoria(
       idcategoria integer primary key auto_increment,
       nombre varchar(50) not null unique,
       descripcion varchar(256) null,
       
);


create table articulo(
       idarticulo integer primary key auto_increment,
       idcategoria integer not null,
       codigo varchar(50) null,
       nombre varchar(100) not null unique,
       precio_venta decimal(11,2) not null,
       stock integer not null,
       descripcion varchar(256) null,
       FOREIGN KEY (idcategoria) REFERENCES categoria(idcategoria)
);


create table persona(
       idpersona integer primary key auto_increment,
       tipo_persona varchar(20) not null,
       nombre varchar(100) not null,
       tipo_documento varchar(20) null,
       num_documento varchar(20) null,
       direccion varchar(70) null,
       telefono varchar(20) null,
       email varchar(50) null
);

create table rol(
       idrol integer primary key auto_increment,
       nombre varchar(30) not null,
       descripcion varchar(100) null,

);


create table usuario(
       idusuario integer primary key auto_increment,
       idrol integer not null,
       nombre varchar(100) not null,
       tipo_documento varchar(20) null,
       num_documento varchar(20) null,
       direccion varchar(70) null,
       telefono varchar(20) null,
       email varchar(50) not null,
       clave int not null,
       FOREIGN KEY (idrol) REFERENCES rol (idrol)
);

create table ingreso(
       idingreso integer primary key auto_increment,
       idproveedor integer not null,
       idusuario integer not null,
       tipo_comprobante varchar(20) not null,
       serie_comprobante varchar(7) null,
       num_comprobante varchar (10) not null,
       fecha datetime not null,
       impuesto decimal (4,2) not null,
       total decimal (11,2) not null,
       estado varchar(20) not null,
       FOREIGN KEY (idproveedor) REFERENCES persona (idpersona),
       FOREIGN KEY (idusuario) REFERENCES usuario (idusuario)
);


create table detalle_ingreso(
       iddetalle_ingreso integer primary key auto_increment,
       idingreso integer not null,
       idarticulo integer not null,
       cantidad integer not null,
       precio decimal(11,2) not null,
       FOREIGN KEY (idingreso) REFERENCES ingreso (idingreso) ON DELETE CASCADE,
       FOREIGN KEY (idarticulo) REFERENCES articulo (idarticulo)
);

create table venta(
       idventa integer primary key auto_increment,
       idcliente integer not null,
       idusuario integer not null,
       tipo_comprobante varchar(20) not null,
       serie_comprobante varchar(7) null,
       num_comprobante varchar (10) not null,
       fecha_hora datetime not null,
       impuesto decimal (4,2) not null,
       total decimal (11,2) not null,
       estado varchar(20) not null,
       FOREIGN KEY (idcliente) REFERENCES persona (idpersona),
       FOREIGN KEY (idusuario) REFERENCES usuario (idusuario)
);

create table detalle_venta(
       iddetalle_venta integer primary key auto_increment,
       idventa integer not null,
       idarticulo integer not null,
       cantidad integer not null,
       precio decimal(11,2) not null,
       descuento decimal(11,2) not null,
       FOREIGN KEY (idventa) REFERENCES venta (idventa) ON DELETE CASCADE,
       FOREIGN KEY (idarticulo) REFERENCES articulo (idarticulo)
);

insert into categoria (nombre, descripcion) value ('BELLEZA', 'Pelo, Maquillaje, Electro Belleza, Perfumes y Fragancias');
insert into categoria (nombre, descripcion) value ('DERMOCOSMETICA', 'Rostro, Corporal, Solar, Solar');
insert into categoria (nombre, descripcion) value ('CUIDADO PERSONAL', 'Cuidado Oral, Higiene Personal, Adultos');
insert into categoria (nombre, descripcion) value ('SALUD Y FARMACIAS', 'Medicamentos, Servicios de Salud, Farmacia, Nutricion y Deportes');
select * from categoria;
insert into articulo (idcategoria,codigo, nombre, precio_venta, stock, descripcion) value (1,'cod001', 'Maybelline the colossal', 2900, 100, 'Mascara de Pestañas');
insert into articulo (idcategoria,codigo, nombre, precio_venta, stock, descripcion) value (2, 'cod002', 'L`oreal', 1800, 100, 'Agua misceral');
insert into articulo (idcategoria,codigo, nombre, precio_venta, stock, descripcion) value (3, 'cod003', 'Plushbell', 500, 100, 'shampoo manzana');
insert into articulo (idcategoria,codigo, nombre, precio_venta, stock, descripcion) value (4, 'cod004', 'Centrum adulto', 2700, 100, 'Suplemento dietario');
select * from articulo;
insert into persona (tipo_persona, nombre, tipo_documento, num_documento, direccion, telefono, email) value ('Empresa','Pampita&Co','CUIT', 0001234, 'Avenida de Mayo 30', 115132412, 'pampita@gmail.com');
insert into persona (tipo_persona, nombre, tipo_documento, num_documento, direccion, telefono, email) value ('Consumidor final','Romina Haag','DNI', 34541123, 'Avenida Colon 5050', 3515491001, 'RShaag@gmail.com');
insert into persona (tipo_persona, nombre, tipo_documento, num_documento, direccion, telefono, email) value ('Monotributista','Ivan Sarjanovich','RUT', 123412-3, 'Santiago de Chile', 423123512, 'sarja97@gmail.com.cl');
select * from persona;