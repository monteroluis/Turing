<script>
var nodes = new vis.DataSet([
    { id: 1, label: "Q0",borderWidth:3,color:{border:'#000', background: 'lightblue'},fixed:{x:true,y:true}},
    { id: 2, label: "Q1",borderWidth:3,color:{border:'#000', background: 'lightblue'},fixed:{x:true,y:true}},
    { id: 3, label: "Q2", borderWidth:3,color:{border:'#000',background: 'lightblue'},fixed:{x:true,y:true}},
]);


var edges = new vis.DataSet([
    { id:0,from: 1, to: 1,color:{color:'#000'},selfReferenceSize:1,arrows:{to:{enabled:true,scaleFactor: 1.5}}},
    { id:1,from: 1, to: 1,font: {color: '#ffffff',strokeWidth: 1,strokeColor: '#171a6b'},color:{color:'lightgrey'},arrows:{to:{enabled:true}},selfReferenceSize:70,label:'# | a | R'},
    { id:2,from: 1, to: 1,font: {color: '#ffffff',strokeWidth: 1,strokeColor: '#171a6b'},color:{color:'lightgrey'}, arrows:{to:{enabled:true}},selfReferenceSize:20, label:'b | a | R'},
    { id:3,from: 1, to: 1,font: {color: '#ffffff',strokeWidth: 1,strokeColor: '#171a6b'},color:{color:'lightgrey'}, arrows:{to:{enabled:true}},selfReferenceSize:45, label:'a | a | R'},
    { id:4,from: 1, to: 2,font: {color: '#ffffff',strokeWidth: 1,strokeColor: '#171a6b'},color:{color:'lightgrey'}, length:200, label:'λ | λ | L',arrows:{to:{enabled:true}}},
    { id:5,from: 2, to: 2,font: {color: '#ffffff',strokeWidth: 1,strokeColor: '#171a6b'},color:{color:'lightgrey'}, label:'a | a | L',selfReferenceSize:40,arrows:{to:{enabled:true}}},
    { id:6,from: 2, to: 3,font: {color: '#ffffff',strokeWidth: 1,strokeColor: '#171a6b'},color:{color:'lightgrey'}, length:200, label:'λ | λ | R',arrows:{to:{enabled:true}} }
]);

var container = document.getElementById("mynetwork");
var data = {
    nodes: nodes,
    edges: edges
};
var options = {

    edges:{

    }

}

var network = new vis.Network(container, data,options);
    network.moveTo({
    position: {x:0,y:0},
    scale: 1.0,
    offset: {x:0,y:0}
  })

  network.on('afterDrawing', function(){
    var dataN = [{id: 1, x: -300, y:40}, {id:2, x:-100, y:40}, {id:3, x:100, y:40}];
    nodes.update(dataN);
  })

function actualizarGrafo(index){
    resetNodes();
    nodes.update({id:3,color:{border:'#000',background: 'lightblue'}})
    if(index <=3 && index >0){
        nodes.update ({id: 1, color: {background: 'red'}});

    }
    if(index == 4 || index ==5){
        nodes.update ({id: 2, color: {background: 'red'}});
    }
    if(index == 6)
        nodes.update ({id: 3, color: {background: 'red'}});

    edges.update({id: index, color: {color:'red'},shadow: {
        enabled: true,
        color: "rgba(0,0,0,0.5)"
    }})

}
function resetNodes(){
    for(var i=1;i<3;i++){
        nodes.update({id:i,color:{background: 'lightblue'}})
    }
}
function resetEdges(){
    for(var i=1;i<7;i++){
        edges.update({id:i,color:{color: 'lightgrey'},shadow:{enabled:false}})
    }
}
</script>
