var $ = jQuery;

 $(document).ready(function(){

 var exa = new FormData()

 $('#id_id_especialidad').on('change', function (){


        var id1 = $(this).val();

        var select_especialidad = $['select[id="id_id_especialidad"]'];
        var options = '<option value="=================="></option>';


        var id =  document.getElementById("id_id_especialidad").value;
	    var comboEspecialidad = document.getElementById("id_id_especialidad");
	    var nombre = comboEspecialidad.options[comboEspecialidad.selectedIndex].text;


		var datos={'action' : 'BuscaEspecialidad' , 'id':id1 };
        exa.append('action','BuscaEspecialidad');
        exa.append('id',id1);



        $.ajax({
            	   type: 'POST',
 	                url: window.location.pathname,
  	               data: exa ,
 	      		success: function (respuesta2) {

 	      		          var dato = JSON.parse(respuesta2);
                          const $id2 = document.querySelector("#id_id_medico");

 	      		           $("#id_id_medico").empty();

	                      $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		                });

 	      			      		},
 	      		error: function (request, status, error) {
 	      			alert(request.responseText);
 	      			alert (error);
 	      			$("#mensajes").html("Error Venta AJAX O RESPUESTA");
 	      		},
 	      		cache : false,
 	      		contentType : false,
 	      		processData: false,

 	        });


  });




   $('#id_id_TipoExamen').on('change', function (){


        var id1 = $(this).val();

        var select_examenes = $['select[id="id_id_examen"]'];
        var options = '<option value="=================="></option>';


        var id =  document.getElementById("id_id_TipoExamen").value;
	    var comboTipoExamen = document.getElementById("id_id_TipoExamen");
	    var nombre = comboTipoExamen.options[comboTipoExamen.selectedIndex].text;


		var datos={'action' : 'BuscaExamenes' , 'id':id1 };
        exa.append('action','BuscaExamenes');
        exa.append('id',id1);



        $.ajax({
            	   type: 'POST',
 	                url: window.location.pathname,
  	               data: exa ,
 	      		success: function (respuesta2) {

 	      		          var dato = JSON.parse(respuesta2);
                          const $id2 = document.querySelector("#id_id_examen");

 	      		           $("#id_id_examen").empty();

	                      $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		                });



 	      			      		},
 	      		error: function (request, status, error) {
 	      			alert(request.responseText);
 	      			alert (error);
 	      			$("#mensajes").html("Error Venta AJAX O RESPUESTA");
 	      		},
 	      		cache : false,
 	      		contentType : false,
 	      		processData: false,

 	        });


  });

 //$(function () {
// var dateNow = new Date();

//$('#fecha').datetimepicker({
// format: 'YYYY-MM-DD hh:mm:ss',
// defaultDate:dateNow
//});
//$("#fecha").data('DateTimePicker').setLocalDate(new Date(year, month, day, 00, 01));
//  });




 $("#btnTomaFoto").click(function(){
        alert("Entre a Rutina Foto");

		var nombre = document.getElementById("nombre").value

  		 $.ajax({
	           url: '/camara',
	           type: 'GET',

	           data : {nombre:nombre},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);

	                      $("#mensajes").html(data.nombre + data.mensaje);
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Fotografia con error !");
	   	    	}

	     });
    });


    $("#btnmotivoSeñas").click(function(){
        alert("Entre a Motivo Señas");
        nombre="nada";



		 $.ajax({
	           url: '/motivoSeñas',
	           type: 'GET',

	           data : {nombre:nombre},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);
                             alert("llegue"),
                             alert(data.mensaje);

	                       document.formHistoria["motivo"].value =data.mensaje;
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Señas  con error !");
	   	    	}

	     });
    });

  $("#btnsubjetivoSeñas").click(function(){
        alert("Entre a Subjetivo Señas");
        nombre="nada";



		 $.ajax({
	           url: '/subjetivoSeñas',
	           type: 'GET',

	           data : {nombre:nombre},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);
                             alert("llegue"),
                             alert(data.mensaje);

	                       document.formHistoria["subjetivo"].value =data.mensaje;
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Señas  con error !");
	   	    	}

	     });
    });


$("#btnAdicionarExamen").click(function(){

     var id_tipo_doc    =  document.formHistoria["id_id_tipo_doc"].value
     var documento      =  document.formHistoria["id_documento"].value
     var folio          =  document.formHistoria["id_folio"].value
     var fecha          =  document.formHistoria["fecha"].value
     var estado_folio   =  document.formHistoria['id_estado_folio'].value

    var id_cantidad=document.getElementById("id_cantidad").value;
	var id_TipoExamen =  document.getElementById("id_id_TipoExamen").value;
	var comboTipoExamen = document.getElementById("id_id_TipoExamen");
	var tipoExamenNombre = comboTipoExamen.options[comboTipoExamen.selectedIndex].text;

	var id_examen =  document.getElementById("id_id_examen").value;
	var comboExamen = document.getElementById("id_id_examen");
	var ExamenNombre = comboExamen.options[comboExamen.selectedIndex].text;



		  var tds = '<tr>';

		  tds += '<td class="col-xs-2">' + tipoExamenNombre + '</td>';
		  tds += '<td class="col-xs-6">' + ExamenNombre + '</td>';
		  tds += '<td class="col-xs-6">' + id_cantidad + '</td>';
          tds += '<td class="col-xs-1"><a href="#">Delete</a></td>';


          tds += '<td  style="visibility: hidden">' + id_tipo_doc + '</td>';
		  tds += '<td  style="visibility: hidden">' + documento + '</td>';
		  tds += '<td  style="visibility: hidden" >' + folio + '</td>';
		  tds += '<td  style="visibility: hidden" >' + fecha + '</td>';
		  tds += '<td  style="visibility: hidden" >' + id_TipoExamen + '</td>';
		  tds += '<td  style="visibility: hidden" >' + id_examen + '</td>';
		  tds += '<td  style="visibility: hidden" >' + estado_folio + '</td>';



		tds += '</tr>';

		$("#Examenes").append(tds);


        datavta = $("#formClinicos").serialize();
     	datavta1 =  JSON.stringify(datavta);

	<!--	seriali.push(datavta1); -->


	//	envio.delete('id_tipo_doc');
	//	envio.delete('documento');
	//    envio.delete('folio');
	//	envio.delete('fecha');
	//	envio.delete('id_TipoExamen');
	//	envio.delete('id_examen');
	//	envio.delete('cantidad');
	//	envio.delete('estado_folio');

        envio.append('id_tipo_doc', id_tipo_doc );
        envio.append( 'documento', documento);
        envio.append('folio', document.getElementById("folio_oculto").value);
        envio.append('fecha', fecha);
        envio.append('id_TipoExamen' , id_TipoExamen);
        envio.append('id_examen' , id_examen);
        envio.append('cantidad' , id_cantidad);
        envio.append('estado_folio' , estado_folio);


             for (var valores in envio.values) {
                     console.log(valores);
             }


     //   var object = {};
       //     envio.forEach(function(value, key){
     //                 object[key] = value;
      //                  });

     //       var jsonEnvio = JSON.stringify(object);


        seriali1.push(envio);

        addAEvent();


   });

function addAEvent(){



			    $('#Examenes').unbind();


				  $('#Examenes').on('click','tr td', function(evt){



				        var target,valorSeleccionado;

				        var column_num = parseInt( $(this).index() + 1 ) ;

				        var row_num = parseInt( $(this).parent().index() + 1 );

				  	   target = $(evt.target);
						   valorSeleccionado = target.text();



					        if(column_num == 4)
					        	{

                                seriali.splice(row_num-3, 1);
					        	    $(this).closest('tr').remove();



  	                            event.preventDefault();

					        	}

				    });
		  			}



$("#btnResmotivoInvidente").click(function(){
        alert("Entre a Rutina Respuesta Motivo Paciente");


  		 $.ajax({
	           url: '/resMotivoInvidente',
	           type: 'GET',

	           data : {},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);


	                    document.getElementById("id_motivo").value = data.Respuesta;
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
    });



$("#btnmotivoInvidente").click(function(){
        alert("Entre a Rutina Reproducir Audio Motivo");

		var nombre = " Cual es el motivo de consulta "

  		 $.ajax({
	           url: '/motivoInvidente',
	           type: 'GET',

	           data : {nombre:nombre},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);

	                   //   $("#mensajes").html(data.nombre + data.mensaje);
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
    });



    $("#btnReproducir").click(function(){
        alert("Entre a Rutina Reproducir Audio");

		var nombre = document.getElementById("nombre").value

  		 $.ajax({
	           url: '/reproduceAudio',
	           type: 'GET',

	           data : {nombre:nombre},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);

	                      $("#mensajes").html(data.nombre + data.mensaje);
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
    });

 });



    $("#btnBuscar").click(function(){
        alert("Entre a buscar");

        var busHabitacion = document.getElementById("busHabitacion").value;
        var busTipoDoc = document.getElementById("busTipoDoc").value;
        var busDocumento = document.getElementById("busDocumento").value;
        var busPaciente = document.getElementById("busPaciente").value;
        var busDesde = document.getElementById("busDesde").value;
        var busHasta = document.getElementById("busHasta").value;

        var sede = 1;
        var servicio = 1;





  		 $.ajax({
	           url: '/buscarAdmision/',
	           type: 'POST',

	           data : {BusHabitacion:busHabitacion, BusTipoDoc: busTipoDoc ,BusDocumento: busDocumento,BusPaciente: busPaciente,BusDesde: busDesde,BusHasta:busHasta ,Sede:sede, Servicio:servicio},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);


	                    document.getElementById("id_motivo").value = data.Respuesta;
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
    });



$(document).on('change', '#id_extraServicio', function(event) {

        alert("Entre Servicio Extra");
        var Serv =   $("#busServicio option:selected").text();

        var Sede =  document.getElementById("Sede").value;

        $.ajax({
	           url: '/buscarHabitaciones',
	            data : {Serv:Serv, Sede:Sede},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#busHabitacion");


 	      		     $("#busHabitacion").empty();


	                 $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });



                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
});



function valida(forma)
{
};



