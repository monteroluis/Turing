let titulo=document.getElementById('titulo1');
let ejemplo=document.getElementById('info');
let cinta=document.getElementById('cargar');
let velocidad=document.getElementById('velocidad');
let correr=document.querySelector('.correr');
let detener=document.querySelector('.detener');
let integrantes=document.getElementById('int');
let Ejemplo=document.querySelector('.ejemplo');
let Ejemplo1=document.querySelector('.ejemplo1');
let textto=document.querySelector('.texto');
let idiomas=document.getElementById('idiomas');

function Ingles(){
    titulo.innerHTML="TURING MACHINE";
    ejemplo.innerHTML="Example";
    cinta.innerHTML="Sart tape"
    velocidad.innerHTML="Speed:"
    correr.innerHTML="Run";
    detener.innerHTML="Stop";
    cerrar.innerHTML="Close";
    integrantes.innerHTML="Team mates"
    Ejemplo.innerHTML="Examples"
    Ejemplo1.innerHTML="Examples:"
    textto.innerHTML= `Change "b" to "a" <br/> 
    Enter: aaaaaaaaaaaaaabbbbbbbbbbbbabababbbbbbbbbbb <br/> 
    Come back: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<br/><br/>
    Note: In the case of spaces, the machine will convert them to "a"`
    idiomas.innerHTML="Languages:"
}
function Español(){
    titulo.innerHTML="MAQUINA DE TURING"
    ejemplo.innerHTML="Ejemplos";
    cinta.innerHTML="Iniciar cinta "
    velocidad.innerHTML="Velocidad:"
    correr.innerHTML="Correr";
    detener.innerHTML="Detener";
    cerrar.innerHTML="Cerrar";
    integrantes.innerHTML="Intregantes"
    Ejemplo.innerHTML="Ejemplos"
    Ejemplo1.innerHTML="Ejemplos:"
    textto.innerHTML= ` Cambiar "b" por "a"<br/>
    Ingresa: aaaaaaaaaaaaaabbbbbbbbbbbbabababbbbbbbbbbb<br/>
    Regresa: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<br/><br/>
    Nota: En caso de los espacios, la máquina los convertirá a "a"`
    idiomas.innerHTML="Idiomas:"
    
}
function Frances(){
    titulo.innerHTML="MACHINE À TURING"
    ejemplo.innerHTML="Exemple";
    cinta.innerHTML="Démarrer la bande"
    velocidad.innerHTML="Vitesse:"
    correr.innerHTML="Exécuter";
    detener.innerHTML="Arrêter";
    cerrar.innerHTML="Fermer";
    integrantes.innerHTML="Membres"
    Ejemplo.innerHTML="Exemples"
    Ejemplo1.innerHTML="Exemples"
    textto.innerHTML= `Remplacez "b" par "a" <br/>
    Entrez: aaaaaaaaaaaaaabbbbbbbbbbbbabababbbbbbbbbbbb <br />
    Reviens Retour: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa <br /><br/>
    Remarque: Dans le cas des espaces, la machine les convertira en "a"`
    idiomas.innerHTML="Langues:"
}


