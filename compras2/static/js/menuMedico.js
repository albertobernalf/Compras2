
var $ = jQuery;

 $(document).ready(function(){

 var exa = new FormData()




// $(function () {
// var dateNow = new Date();

// $('#fecha').datetimepicker({
// format: 'YYYY-MM-DD hh:mm:ss',
// defaultDate:dateNow
// });

// $("#fecha").data('DateTimePicker').setLocalDate(new Date(year, month, day, 00, 01));
//  });

$("#btnAdicInterconsultas").click(function(){


    let elementInt = document.getElementById("tablaInterconsultas");
    elementInt.removeAttribute("hide");



    elementInt.setAttribute("hide", "show");

    alert("Se muestra la TABLA otra vez ?");


  //  var cantidad=document.getElementById("cantidad").value;

	var DescripcionConsulta =  document.getElementById("descripcionConsulta").value;

	var InterconsultasDiagnosticos =  document.getElementById("interconsultasDiagnosticos").value;

	var comboDiagnostico = document.getElementById("interconsultasDiagnosticos");

	var DiagnosticoNombre = comboDiagnostico.options[comboDiagnostico.selectedIndex].text;

    var InterconsultasEspecialidad =  document.getElementById("interconsultasEspecialidad").value;

	var comboEspecialidades = document.getElementById("interconsultasEspecialidad");

	var EspecialidadesNombre = comboEspecialidades.options[comboEspecialidades.selectedIndex].text;



		  var tds = '<tr>';

		  tds += '<td class="col-xs-2">' + DiagnosticoNombre + '</td>';
		  tds += '<td class="col-xs-6">' + EspecialidadesNombre + '</td>';
		  tds += '<td class="col-xs-6">' + DescripcionConsulta + '</td>';
          tds += '<td class="col-xs-1"><a href="#">Delete</a></td>';



		tds += '</tr>';

		$("#tablaDiagnosticos").append(tds);


        envioDiag.append('DiagnosticoNombre' , DiagnosticoNombre);
        envioDiag.append('EspecialidadesNombre' , EspecialidadesNombre);
        envioDiag.append('DescripcionConsulta' , DescripcionConsulta);



             for (var valores in envio.values) {
                     console.log(valores);
             }


        serialiInt.push(envioDiag);




        addAEvent();


   });



$("#btnAdicDiagnosticos").click(function(){




   // var cantidad=document.getElementById("cantidad").value;

	var TiposDiagnostico =  document.getElementById("tiposDiagnostico").value;

	var comboTiposDiagnostico = document.getElementById("tiposDiagnostico");

	var TiposDiagnosticoNombre =  comboTiposDiagnostico.options[comboTiposDiagnostico.selectedIndex].text;

	var Diagnosticos =  document.getElementById("diagnosticos").value;

	var comboDiagnostico = document.getElementById("diagnosticos");

	var DiagnosticoNombre = comboDiagnostico.options[comboDiagnostico.selectedIndex].text;





		  var tds = '<tr>';

		  tds += '<td class="col-xs-2">' + TiposDiagnosticoNombre + '</td>';
		  tds += '<td class="col-xs-6">' + DiagnosticoNombre + '</td>';
		//  tds += '<td class="col-xs-6">' + cantidad + '</td>';
          tds += '<td class="col-xs-1"><a href="#">Delete</a></td>';





		tds += '</tr>';

		$("#tablaDiagnosticos").append(tds);





        envioDiag.append('TiposDiagnostico' , TiposDiagnostico);
        envioDiag.append('Diagnosticos' , Diagnosticos);
       // envioDiag.append('cantidad' , cantidad);



             for (var valores in envio.values) {
                     console.log(valores);
             }





        serialiDiag.push(envioDiag);




        addAEvent();


   });



$("#btnAdicAntecedentes").click(function(){

   alert("Se muestra la TABLA otra vez ?");

    var descripcion=document.getElementById("descripcion").value;

	var TiposAntecedente =  document.getElementById("tiposAntecedente").value;

	var antecedentes =  document.getElementById("antecedentes").value;

	var comboExamen = document.getElementById("antecedentes");

	var ExamenNombre = comboExamen.options[comboExamen.selectedIndex].text;


		  var tds = '<tr>';

		  tds += '<td class="col-xs-2">' + TiposAntecedente + '</td>';
		  tds += '<td class="col-xs-6">' + ExamenNombre + '</td>';
		  tds += '<td class="col-xs-6">' + descripcion + '</td>';
          tds += '<td class="col-xs-1"><a href="#">Delete</a></td>';



		tds += '</tr>';

		$("#tablaAntecedentes").append(tds);

          alert("Sa enviar");


        envio.append('TiposAntecedente' , TiposAntecedente);
        envio.append('ExamenNombre' , ExamenNombre);
        envio.append('descripcion' , descripcion);

  alert("antes del push");

             for (var valores in envio.values) {
                     console.log(valores);
             }

        serialiAnt.push(envio);




        addAEvent();


   });


$("#btnAdicExamenTerapias").click(function(){

    alert("Entre boton");



    var cantidad=document.getElementById("cantidad").value;

	var TipoExamen =  document.getElementById("tipoExamenLab").value;

	var examen =  document.getElementById("terapias").value;

	var comboExamen = document.getElementById("terapias");

	var ExamenNombre = comboExamen.options[comboExamen.selectedIndex].text;


		  var tds = '<tr>';

		  tds += '<td class="col-xs-2">' + TipoExamen + '</td>';
		  tds += '<td class="col-xs-6">' + ExamenNombre + '</td>';
		  tds += '<td class="col-xs-6">' + cantidad + '</td>';
          tds += '<td class="col-xs-1"><a href="#">Delete</a></td>';



		tds += '</tr>';

		$("#tablaTerapias").append(tds);


        envioTer.append('tipoExamen' , TipoExamen);
        envioTer.append('examen' , examen);
        envioTer.append('cantidad' , cantidad);



        serialiTer.push(envioTer);




        addAEvent();


   });




$("#btnAdicExamenLab").click(function(){




    var cantidad=document.getElementById("cantidad").value;

	var TipoExamen =  document.getElementById("tipoExamenLab").value;

	var examen =  document.getElementById("laboratorios1").value;

	var comboExamen = document.getElementById("laboratorios1");

	var ExamenNombre = comboExamen.options[comboExamen.selectedIndex].text;





		  var tds = '<tr>';

          tds += '<td  style="visibility: hidden">' + TipoExamen + '</td>';
		 // tds += '<td class="col-xs-2">' + TipoExamen + '</td>';
		  tds += '<td class="col-xs-6">' + ExamenNombre + '</td>';
		  tds += '<td class="col-xs-6">' + cantidad + '</td>';
          tds += '<td class="col-xs-1"><a href="#">Delete</a></td>';


         // tds += '<td  style="visibility: hidden">' + id_tipo_doc + '</td>';



		tds += '</tr>';

		$("#tablaExamenes").append(tds);




        envioLab.append('tipoExamen' , TipoExamen);
        envioLab.append('examen' , examen);
        envioLab.append('cantidad' , cantidad);




        serialiLab.push(envioLab);




        addAEvent();


   });


$("#btnAdicExamenRad").click(function(){

    alert("Entre boton");



    var cantidad=document.getElementById("cantidad").value;
	var TipoExamen =  document.getElementById("tipoExamenRad").value;

	var examen =  document.getElementById("radiologias1").value;

	var comboExamen = document.getElementById("radiologias1");

	var ExamenNombre = comboExamen.options[comboExamen.selectedIndex].text;


		  var tds = '<tr>';
          tds += '<td  style="visibility: hidden">' + TipoExamen + '</td>';
		 // tds += '<td class="col-xs-2">' + TipoExamen + '</td>';
		  tds += '<td class="col-xs-6">' + ExamenNombre + '</td>';
		  tds += '<td class="col-xs-6">' + cantidad + '</td>';
          tds += '<td class="col-xs-1"><a href="#">Delete</a></td>';


		tds += '</tr>';

		$("#tablaExamenesRad").append(tds);


        envioRad.append('tipoExamen' , TipoExamen);
        envioRad.append('examen' , examen);
        envioRad.append('cantidad' , cantidad);



        serialiRad.push(envioRad);

        addAEvent();


   });






function addAEvent(){



			    $('#tablaExamenes').unbind();
                $('#tablaExamenesRad').unbind();
                $('#tablaTerapias').unbind();
                $('#tablaAntecedentes').unbind();
                $('#tablaDiagnosticos').unbind();
                $('#tablaInterconsultas').unbind();


				  $('#tablaExamenes').on('click','tr td', function(evt){



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



				  $('#tablaExamenesRad').on('click','tr td', function(evt){



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


                    $('#tablaTerapias').on('click','tr td', function(evt){



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

				     $('#tablaDiagnosticos').on('click','tr td', function(evt){



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

				     $('#tablaAntecedentes').on('click','tr td', function(evt){



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

                     $('#tablaInterconsultas').on('click','tr td', function(evt){



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

