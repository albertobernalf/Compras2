-- Script de cargue de datos inicial :

-- tengo que subir bien solicitud_sedescompra para que me siba bien areas,


-- translate(btrim(direccionl::text),'óÓáÁéÉíÍúÚñÑ'::text,'oOaAeEiIuUnN'::text)

select * from imhotep_usuarios;

select * from imhotep_sedes;
select * from solicitud_sedesCompra;

delete from solicitud_sedesCompra;

--Sedes: Problema

insert into solicitud_sedesCompra(codreg_sede ,  nom_sede ,  codreg_ips,  direccion ,  telefono ,  departamento ,  municipio ,  zona ,  sede ,  estadoreg)

select codreg_sede ,  translate(btrim(nom_sede::text),'óÓáÁéÉíÍúÚñÑ'::text,'oOaAeEiIuUnN'::text)  ,  codreg_ips,  translate(btrim(direccion::text),'óÓáÁéÉíÍúÚñÑ'::text,'oOaAeEiIuUnN'::text) ,  translate(btrim(telefono::text),'óÓáÁéÉíÍúÚñÑ'::text,'oOaAeEiIuUnN'::text) ,  translate(btrim(departamento::text),'óÓáÁéÉíÍúÚñÑ'::text,'oOaAeEiIuUnN'::text) ,  translate(btrim(municipio::text),'óÓáÁéÉíÍúÚñÑ'::text,'oOaAeEiIuUnN'::text) ,translate(btrim(zona::text),'óÓáÁéÉíÍúÚñÑ'::text,'oOaAeEiIuUnN'::text) ,  sede ,  'A'
from imhotep_sedes;


update solicitud_sedesCompra set direccion = 'Calle 36 Sur No. 77-33 Barrio Kennedy'  where codreg_sede = 'MK' ;
update solicitud_sedesCompra set direccion = 'Avenida Carrera 45 # 94 - 31/39 (Autopista Norte)' where codreg_sede = 'MN' ;
update solicitud_sedesCompra set direccion = 'Cra 66A #4G-86' where codreg_sede = 'AM' ;
update solicitud_sedesCompra set direccion = 'Cl. 1d # 17A - 35' where codreg_sede = 'SJ' ;
update solicitud_sedesCompra set direccion = 'Cra 102 # 17-49/57' where codreg_sede = 'SF' ;
update solicitud_sedesCompra set direccion = 'Cr 21 No 169 15/25 Bodega 2' where codreg_sede = 'MT' ;


   
-- Usuarios : Problema

delete from solicitud_usuarios;
  
insert into solicitud_usuarios (num_identificacion ,  nom_usuario ,  clave_usuario ,  carg_usuario , estadoreg , sede_id )
select num_identificacion, translate(btrim(nom_usuario::text),'óÓáÁéÉíÍúÚñÑ*'::text,'oOaAeEiIuUnN '::text),  translate(btrim(clave_usuario::text),'óÓáÁéÉíÍúÚñÑ*'::text,'oOaAeEiIuUnN '::text),  translate(btrim(carg_usuario::text),'óÓáÁéÉíÍúÚñÑ*'::text,'oOaAeEiIuUnN '::text), 'A' , 7 
from imhotep_usuarios 
where activo = 'S' and  num_identificacion in ('7548543','35195339','52046796','52956447','80760858','65761741','79307851','65822566','79646248','1032381487','64868812','49754113','55238662','52148511','52888300','52869056','1072657156','52908843','1016069653','51892844','1014281484','1013611750','52735753','1102388730','52161946','52233695',
'19456950','79717519','1014245115','53139189','1024567274','1019057514','1014250241','79690980','52973594','1010202398','1022981421','52027259','53079814','1032367193','1026281960',
'1010182068','52982328','53093836','1013605270','79830038','1110446284','1012329750','1012369594','1020805372','16788445','80738164','53026159','1013614781');

-- OJO ESTE USUARIO ES COMODIN PARA LOS DEFAULTS

insert into solicitud_usuarios values (1,'11111','NO APLICA','1', 'NO APLICA','A',7);

insert into solicitud_usuarios (num_identificacion,nom_usuario, clave_usuario,carg_usuario,estadoReg,sede_id) values ('1110446284','CRISTHIAN ELIAS AGUDELO QUINTERO','Elias 01', 'Facturador(a)','A',7);

select * from solicitud_usuarios;


-- delete from solicitud_usuarios;
select * from solicitud_usuarios;
select * from solicitud_usuarios where num_identificacion = '52956447';
delete from solicitud_usuarios where clave_usuario like ('%*%');

-- Problema no inserta todo por caracteres especiales, tildes caracteres extraños etc.

insert into solicitud_usuarios (num_identificacion ,  nom_usuario ,  clave_usuario ,  carg_usuario , estadoreg , sede_id )
select num_identificacion,nom_usuario, clave_usuario, carg_usuario, 'A' , 7
from imhotep_usuarios 
--where activo = 'S' and  num_identificacion in ('7548543','35195339','52046796','52956447','80760858','65822566','79646248','64868812');
where activo = 'S' and  num_identificacion in ('7548543','35195339','52046796','52956447','80760858','65822566','64868812');
 B4s32023*

-- Areas. OK

select * from mae_areas;
select * from solicitud_sedesCompra;
select * from solicitud_areas;
delete  from solicitud_areas;


insert into solicitud_areas (area,estadoreg,sede_id)
select  translate(btrim(areas.area::text),'óÓáÁéÉíÍúÚñÑ'::text,'oOaAeEiIuUnN'::text),'A', sedes.id
from mae_areas areas, solicitud_sedesCompra sedes
where areas.sede = sedes.sede;


-- Proveedores -- Problemas  UTF8

select * from mae_proovedores;


insert into solicitud_proveedores (codreg_proveedor, proveedor,correo,estadoReg)
select codreg_proovedor, translate(btrim(proovedor::text),'óÓáÁéÉíÍúÚñÑ'::text,'oOaAeEiIuUnN'::text),'adminbd@clinicamedical.com.co','A' 
from mae_proovedores
where activo = 'S';

update solicitud_proveedores set correo='';



delete from public.solicitud_solicitudes;;
delete from public.solicitud_solicitudesdetalle;;

select * from public.solicitud_solicitudes;
select * from public.solicitud_solicitudesdetalle;

INSERT INTO solicitud_solicitudesdetalle ( item ,  cantidad ,  justificacion ,  "especificacionesTecnicas" ,  "especificacionesAlmacen" ,  "especificacionesCompras" ,  estadoreg ,             descripcion_id, "estadosAlmacen_id", "estadosCompras_id", "estadosSolicitud_id", "estadosValidacion_id", solicitud_id, "tiposCompra_id", "usuarioResponsableValidacion_id", "entregadoAlmacen", presentacion_id, "solicitadoAlmacen", producto )  VALUES(1, 10,'parayap','','','','A',1, 1, 1, 1, 1, 11, 6,17,0,6, 0,'COMPU001'  )

select * from public.solicitud_presentacion;
select * from public.solicitud_tiposcompra;


INSERT INTO solicitud_solicitudesdetalle ( item ,  cantidad ,  justificacion ,  "especificacionesTecnicas" ,  "especificacionesAlmacen" ,  "especificacionesCompras" ,  estadoreg ,             descripcion_id, "estadosAlmacen_id", "estadosCompras_id", "estadosSolicitud_id", "estadosValidacion_id", solicitud_id, "tiposCompra_id", "usuarioResponsableValidacion_id", "entregadoAlmacen", presentacion_id, "solicitadoAlmacen", producto, , "usuarioResponsableCompra", , "usuarioResponsableAlmacen_id" )  VALUES(1, 10,'para yap','','','','A',1, 1, 1, 1, 1, 17, 6,17,0,1, 0,'COMPU001'  )