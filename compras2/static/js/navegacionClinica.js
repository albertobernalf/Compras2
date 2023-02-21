formHistoriaClinica.addEventListener('submit', e=>{


         alert("Entre Form formHistoriaClinica");
         alert("serlialiLab = " +  serialiLab);

        e.preventDefault()

             var tipoDoc    =  document.getElementById("tipoDoc_id").value

             var documento      =  document.getElementById("documentoPaciente").value;

             var folio  = "0";
             var fecha          =  document.getElementById("fecha").value;

             var motivo =          document.getElementById("id_motivo").value;
             var subjetivo =      document.getElementById("id_subjetivo").value;
             var objetivo =       document.getElementById("id_objetivo").value;
             var analisis =        document.getElementById("id_analisis").value;
             var plan =           document.getElementById("id_plan").value;
             var causasExterna = document.getElementById("causasExterna").value;
             var dependenciasRealizado = document.getElementById("dependenciasRealizado").value;
             var usuarioRegistro = document.getElementById("usuarioRegistro").value;
             var consecAdmision=document.getElementById("IngresoPaciente").value;
             var perfil = document.getElementById("perfil").value;
             var tiposfolio = 0;
             // Medico Verificar
             if (perfil == 1)
                {
                document.getElementById("tiposFolio").value=1;
                }
                // Enfermeria Verificar
             if (perfil == 2)
                {
                document.getElementById("tiposFolio").value=2;
                }


             var tiposFolio = document.getElementById("tiposFolio").value;
             alert("tiposFolio =" + tiposFolio);
             var profesional = document.getElementById("profesional").value;
             alert("Profesional = ", profesional);
             var espMedico = document.getElementById("espMedico").value;
             var planta = document.getElementById("Username_id").value;
             var fechaRegistro = document.getElementById("fechaRegistro").value;
             var estadoReg = "A"
             var diagnosticos = document.getElementById("diagnosticos").value;


             envio1.append('tipoDoc', tipoDoc );
             envio1.append( 'documento', documento);
             envio1.append( 'consecAdmision', consecAdmision);
             envio1.append('folio', folio);
             envio1.append('fecha', fecha);
             envio1.append('tiposFolio', tiposFolio);
             envio1.append('profesional', profesional);
             envio1.append('causasExterna', causasExterna);
             envio1.append('dependenciasRealizado', dependenciasRealizado);
             envio1.append('espMedico', espMedico);
             envio1.append('planta', planta);
             envio1.append('motivo' , motivo);
             envio1.append('subjetivo' , subjetivo);
             envio1.append('objetivo' , objetivo);
             envio1.append('analisis' , analisis);
             envio1.append('plan' , plan);
             envio1.append('fechaRegistro' , fechaRegistro);
             envio1.append('usuarioRegistro' , usuarioRegistro);
             envio1.append('estadoReg' , estadoReg);
             envio1.append('diagnosticos' , diagnosticos);

             // InicioLaboratorio
             // Aqui serializar la forma  HistoriaExamenesCabezoteForm

             document.formCabezoteLab['historia'].value =0;
             document.formCabezoteLab['estadoReg'].value ='A';

             // convertir formdata a JSON

             const formDataCabezoteLab = new FormData(formCabezoteLab);
             var object = {};
             formDataCabezoteLab.forEach((value, key) => object[key] = value);

             //Convierto a JSON

             var jsonCabezoteLab = JSON.stringify(object);

             envio1.append('jsonCabezoteLab' , jsonCabezoteLab);


            // Rutina manejo serialiLab

// Display the key/value pairs


                    for (var clave in serialiLab){
                 		   // Controlando que json realmente tenga esa propiedad
            		    if (serialiLab.hasOwnProperty(clave)) {
             		    // Mostrando en pantalla la clave junto a su valor
               		    //   alert("La clave es " + clave + " y el valor es " + serialiLab[clave]);
               		    console.log ("clave PRIMER FOR");

			           	console.log (clave + ', ' + serialiLab[clave]);
                 	       envio_final = serialiLab[clave];


	                     }
        	           }
        	         //   var dato = JSON.parse(envio_final);
                        console.log("Envio final = ");
                        console.log(JSON.stringify (envio_final));



                      var jsonLab = {};
                    var jsonDefLab = [];
                    var inicio = 0;

           //     alert("Entries = " + JSON.stringify (envio_final.entries()));


     		    for(var pair of envio_final.entries()) {

                 	       if (inicio == 3)
                        {
                         // insjsonDeferto desde aqui
                      //   alert("Los datos jsonLab son : ");

                       //  alert( JSON.stringify (jsonLab ));

                         jsonDefLab.push(JSON.stringify (jsonLab ));
                          delete jsonLab['tipoExamen'];
                          delete jsonLab['examen'];
                          delete jsonLab['cantidad'];

                         //   alert( "Con El jSONlAB bORRADO QUEDA = " + JSON.stringify (jsonLab ));
                             alert( "y El jSONdeflAB queda = " + JSON.stringify (jsonDefLab ));
                         inicio = 0;

		            	}

		           inicio = inicio +1;

                   if (pair[0] == "tipoExamen" )
                    {

                   jsonLab[pair[0]] = pair[1];
                    }

                    if (pair[0] == "examen"  )
                    {

                       jsonLab[pair[0]] = pair[1];

                    }

                   if (pair[0] == "cantidad" )
                            {

                       jsonLab[pair[0]] = pair[1];

                            }

        	        }


        	        alert("jsondef = " + JSON.stringify (jsonDefLab));


        console.log(JSON.stringify (jsonDefLab));

                  var jsonDefLab1 = JSON.stringify(jsonDefLab);

                  envio1.append('serialiLab',jsonDefLab1);

                 // Fin Rutina manejo serialiLab

                 // Fin Laboratorio



                 // Inicio Radiologia

                 // Aqui serializar la forma  HistoriaExamenesCabezoteForm

                   document.formCabezoteRad['historia'].value =0;
                   document.formCabezoteRad['estadoReg'].value ='A';

             // convertir formdata a JSON

             const formDataCabezoteRad = new FormData(formCabezoteRad);
             var object = {};
             formDataCabezoteRad.forEach((value, key) => object[key] = value);

             //Convierto a JSON

             var jsonCabezoteRad = JSON.stringify(object);

             envio1.append('jsonCabezoteRad' , jsonCabezoteRad);

             // Rutina manejo serialiRad


     		    for (var clave in serialiRad){
                 		   // Controlando que json realmente tenga esa propiedad
            		    if (serialiRad.hasOwnProperty(clave)) {
             		    // Mostrando en pantalla la clave junto a su valor
               		    //   alert("La clave es " + clave + " y el valor es " + serialiLab[clave]);
			           	console.log (clave + ', ' + serialiRad[clave]);
                 	       envio_finalRad = serialiRad[clave];
	                     }
        	           }
                        console.log("Envio final = ");
                        console.log(envio_finalRad);


                   // Display the key/value pairs

                    var jsonRad = {};
                    var jsonDefRad = [];
                    var inicio = 0;

                    for(var pair of envio_finalRad.entries()) {
                        console.log(pair[0]+ ', '+ pair[1]);

                          if (inicio == 3)
                        {
                         // insjsonDeferto desde aqui
                         alert(" VOYA PUSH jsonLab = " + jsonRad);
                         jsonDefRad.push(jsonRad);
                         delete jsonRad.tipoExamen ;
                         delete jsonRad.examen ;
                         delete jsonRad.Cantidad ;
                         inicio = 0;
                         alert("entre esta vez");
                         alert("jsonDefRad = " + jsonDefRad);
		            	}
		           inicio = inicio +1;

                   if (pair[0] == "tipoExamen" )
                    {
                   jsonRad.tipoExamen = pair[1];
                    }
                    if (pair[0] == "examen"  )
                    {
                       jsonRad.examen = pair[1];

                    }
                   if (pair[0] == "cantidad" )
                    {
                        jsonRad.cantidad = pair[1];

                    }
                    }

                  console.log(jsonDefRad);
                  var jsonDefRad1 = JSON.stringify(jsonDefRad);

                  envio1.append('serialiRad',jsonDefRad1);

                 // Fin Rutina manejo serialiRad





                 // Fin Radiologia


               $.ajax({
            	   type: 'POST',
 	               url: '/crearHistoriaClinica/',
  	               data: envio1,
 	      		success: function (respuesta2) {
 	      		       // var data = JSON.parse(respuesta2);
 	      		        alert("con stringy = " + JSON.stringify(respuesta2))
 	      		        // alert(data['Tipo']);
 	      		        //alert(data['Mensaje']);

 	      		        alert(respuesta2.Tipo);
 	      		        alert(respuesta2.Mensaje);


 	      		        if (respuesta2.Tipo != '"Error')
 	      		         {
 	      		        document.getElementById("id_motivo").value = "";
                        document.getElementById("id_subjetivo").value = "";
                        document.getElementById("id_objetivo").value = "";
                        document.getElementById("id_analisis").value = "";
                        document.getElementById("id_plan").value = "";
                        document.getElementById("causasExterna").value = "";
                        document.getElementById("dependenciasRealizado").value = "";
                        document.getElementById("diagnosticos").value = "";

                         const $id2 = document.querySelector("#id_id_medico");

 	      		         //  $("#laboratorios1").empty();
 	      		         //  $("#radiologias1").empty();
 	      		        //   $("#terapias").empty();
 	      		          // $("#tiposAntecedente").empty();
                            //$("#antecedente").empty();
                        //$("#tiposDiagnostico").empty();
                            //$("#diagnostico").empty();
 	      		        }

 	      	 			$("#mensajes").html(respuesta2.Mensaje);


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

})
