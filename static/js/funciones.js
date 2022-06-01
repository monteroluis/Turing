$(function() {

  $('#cargar').click(function(){
      id = ID;
      if($('#cadena').val() == ""){
          $(this).popover('show');
          return false;
      }else{
         actualizarGrafo(7);
          $(this).popover('hide');
          Stop();
          Clear();
          borrarTabla(4);
          cargarCadena(id);    
          return true;
      }
  });
  $('#evaluar').click(

      function(){
          Stop();
          id = ID;
          tiempo = 1000 - $("#rango").val();
          Tick = setInterval(function(){Evaluate(id)}, tiempo);
      }

  );
});

function AddVacio(table){
  for(i = 0; i < 40; i++){
      AddRow(Vacio, "", "", table);
  }
  return true;
}

function cargarCadena(table){
  var cadena = $('#cadena').val();
      borrarTabla(table);
      AddRow('λ', "active-row", "bg-danger text-light", table);
      for(i = 0; i < cadena.length; i++){
          AddRow(cadena.charAt(i), "", "", table);
      }
      AddVacio(table);
      return true;
}

function EvaluarNodo(symbol, id){
  MaquinaTuring[id].Count++;
  symbols = MaquinaTuring[id][MaquinaTuring[id].State]
  NextValues = symbols[symbol];
    actualizarGrafo(NextValues[3]);
  setTimeout(function(){resetEdges()}, tiempo+(tiempo/4));
  if(symbols[symbol] == undefined) return { Error : true, Acceptable : MaquinaTuring[id].Functions.Acceptable(MaquinaTuring[id].State), Message : `El símbolo <strong>'${symbol}'</strong> no tiene transición definida en el estado <strong>${MaquinaTuring[id].State}</strong> de esta máquina. ${symbols.ERROR ? symbols.ERROR : ''}`};
  MaquinaTuring[id].State = NextValues[1];
  return { Error : false, Acceptable: MaquinaTuring[id].Functions.Acceptable(MaquinaTuring[id].State), Output : NextValues[0], Movement : NextValues[2] };
}

function Evaluate(id){
      chain = $("#tabla" + id + " td");
      i = MaquinaTuring[id].i;
      if(!MaquinaTuring[id].Functions.Acceptable(MaquinaTuring[id].State) && chain.length > i && MaquinaTuring[id].Count < 10000){
          tiempo = 1000 - $("#rango").val();
          result = EvaluarNodo(chain[i].textContent.trim(), id);
          if(result.Error){
              Update();
              Stop();
              $('#modalTitle').html('¡Error!');
              $('#modalText').html(result.Message);
              $('#myModal').modal('show');
             
          }else{
              if (i >= chain.length - 2) AddVacio(id);
              chain[i].textContent = (result.Output);
              i += result.Movement;
              MaquinaTuring[id].i += result.Movement;
              chain[i].setAttribute('id', 'new-row');
              ChangeActiveRow(id, tiempo);
              Update();
          }

          
      }else{
          if(MaquinaTuring[id].Functions.Acceptable(MaquinaTuring[id].State)){
              Update();            
              Stop();   
          }
          if(MaquinaTuring[id].Count >= 10000){
              Update();
              Stop();
              $('#modalTitle').html('¡Error!');
              $('#modalText').html('La cadena ingresada ha generado muchas transiciones sin definir un resultado.');
              $('#myModal').modal('show');
          }
      }

      
}
function Stop(){
  clearInterval(Tick);
}
// SYNTAXIS Machine[CURRENT_STATE] = { INCOMING_SYMBOL: [OUTPUT_SYMBOL, NEXT_STATE, HEAD_MOVEMENT]}
function Turing(){

  MaquinaTuring[4][0] = {
      'λ' : ['λ', 1 , 1, 9]
  }
  MaquinaTuring[4][1] = {
      'a' : ['a', 1, 1, 3],
      'b' : ['a', 1, 1, 2],
      '' : ['a', 1, 1, 1],
      'λ' : ['λ', 2, -1, 4] 
  }
  MaquinaTuring[4][2] = {
      'a' : ['a', 2, -1, 5],
      'λ' : ['λ', 3, 1, 6]
  }
  MaquinaTuring[4][3] = {
      'a' : ['a', 10, 0]
  }
  MaquinaTuring[4]['i'] = 0;
  MaquinaTuring[4]['Count'] = 0;
  MaquinaTuring[4]['State'] = 0;
  MaquinaTuring[4]['Functions'] = {
      Acceptable(state) { return state == 3 }
  };
}
