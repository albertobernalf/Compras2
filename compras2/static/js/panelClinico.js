
 $(document).ready(function(){

var table = document.getElementById("tablaClinico")

table.addEventListener("click", getTablaFila);


function getTablaFila(){
var tds = event.path[1].children
 var datos = []
 for (var i = 0; i < tds.length; i++) {
  datos.push(tds[i].innerText)

 }
 console.log("LA INFO QUE NECESITO");
 console.log(datos[0]);
 console.log(datos[2]);
 console.log(datos[3]);


   document.getElementById("TipoDocPaciente").value = datos[0];
   document.getElementById("DocumentoPaciente").value = datos[2];
   document.getElementById("IngresoPaciente").value = datos[3];


$("#formCargaHc").submit();
};
});