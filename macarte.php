<!DOCTYPE html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <title>FindLoc</title>
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>

        <script>
    function affichertexte() {
        
document.getElementById("texte").innerHTML=`<div class='fond'>
<div class='affichage'>texte cliquable (clique sur le 1er texte pour fermer)<br><br>
<p  onclick='cacher();'> Les localisations ont été extraites avec différentes heuristiques : </p>
 <ul class='list-style-position-outside'>
  <li>Heuristique Spacy: consiste à utiliser les localisations de Spacy grâce a ses labels GPE et LOC.</li> <br> 
  <li> Heuristique adresse-LT : Lors du traitement d'un champs de texte ou un URL par LocationTagger, on a plusieurs entites en retour : country-cities, countries, régions, adresse.<br> Cette heuristique retourne le résultat contenu dans le champs Address, et cela si il n''est pas vide. </li> <br>
   <li> Heuristique country cities: Qui rend le résultat de country cities retourner par LocationTagger. </li> <br> 
   <li> Heuristique 3 (ordre) : Cette heuristique retourne un résultat dans le cas ou dans la phrase on a un LOC suivi d'un GPE grâce à Spacy. Exemple : Kootenai River   </li> <br> 
   <li> Heuristique emplacement-localisation : Pour construire cette heuristique nous avons d’abord procédé à une analyse des images
qui contiennent une seule localisation (résultat retourné par spaCy) dans le but de savoir
l’emplacement des indicateurs de localisation dans la phrase, plutôt à la fin ou au début. <br>
Après analyse on a déduit que c'était plutôt vers la fin dans le cas où on a plusieurs localisations. </li> <br>
   <li> Heuristique mots composés : Cette heuristique réalise une analyse du texte associé à l''image puis met en évidence les mots qui représentent des noms propres 'PROPN' et ceci grâce à la bibliothèque Spacy.</li> 
    </ul> 
    <p style='texte-align:left;'>Selectionnez le choix le plus pertinent puis Confirmez le</p>Le choix des couleurs va du vert clair au rouge. Le vert clair étant l'heuristique la plus forte.<br> En ce qui concerne la localisation figurant sur la carte corresponds à l'heuristique la plus forte.</div></div> `;
}
 
function cacher(){
document.getElementById("texte").innerHTML="";
}
</script> 
    <style>
    html, body {width: 100%;height: 100%;margin: 0;padding: 0;} </style>
    <style> 
    #texte {
        margin:0;
        padding:0;
        position:absolute;
        z-index:25;
    }
    .fond{
      width:100%;
      position:fixed;
      height:100%;
      background-color:rgba(0,0,0,0.8);
      z-index:2;
      }
       
      .affichage{
      width: 66%;
      height:85%;
      margin:auto;
      margin-top:5%;
      z-index:3;
      border:2px solid black;
      background-color:white;
      text-align:center;
      }
       
      .affichage p{
      width:100%;
      }

      .list-style-position-outside{ list-style-position : outside }
</style>
    <style>#map {position:relative;top:0;bottom:0;right:0;left:0;}</style>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="stylesheet" href="styleMaCarte.css">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Questrial&display=swap" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />

      
</head>

<body>  

      
        <div class="folium-map" id="map_a620533b73fc4a38880428953e8ae81f"></div>
        <div id="texte"></div>
        
        <p style='font-style:italic;font-size:16px;text-align: center;'>  Veuillez saisir la bonne localisation de l'image figurant sur la carte :</p>
         
         <div id ="resultat_heuristique"></div> 
         
         <form action="macarte.php" method="POST">
            <button class = "submit" name = "my_button" value="before" id="button"  onclick="miseenattente()" >Confirmer</button>
            <p></p>    
        </form>

        
        <button  id="aide" value="buttonA" onclick="affichertexte()"> Aide </button>
        
        
</body>

<?php 

$url = "";
$value = "";
    if(isset($_GET["ul"]))
    {
        $url = $_GET["ul"];

    }

    if(isset($_POST["my_button"]))
    {

        $value = $_POST["my_button"];

    }
    $myfile = fopen("teste.txt", "a") or die("Unable to open file!");
    if(!empty($url))
    {
        fwrite($myfile, "{");
        fwrite($myfile, $url);
        fwrite($myfile, ",");
    
    }
    if(!empty($value))
    {
        fwrite($myfile, $value);
        fwrite($myfile, "}");
        fwrite($myfile, "\n");
        $command = escapeshellcmd('majvalid.py');
        $output = shell_exec($command);
    }
    fclose($myfile);
    

?>

<script type="text/javascript">
    
            var map_a620533b73fc4a38880428953e8ae81f = L.map(
                "map_a620533b73fc4a38880428953e8ae81f",
                {
                    center: [45.41117, -75.69812],
                    crs: L.CRS.EPSG3857,
                    zoom: 5,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );
            var tile_layer_1c5f64abefd34f14b7599eb45775d961 = L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_a620533b73fc4a38880428953e8ae81f);
 

            const queryString = window.location.search;
            const urlParams = new URLSearchParams(queryString);
            const page_type = urlParams.get('ul');
            



function createRadioElement(name, checked) {
    var radioHtml = '<input type="radio" name="' + name + '"';
    if ( checked ) {
        radioHtml += ' checked="checked"';
    }
    radioHtml += '/>';

    var radioFragment = document.createElement('div');
    radioFragment.innerHTML = radioHtml;

    return radioFragment.firstChild;
}


function marker(liste)
{  if (liste.length ==3)

	{  if ( typeof liste[0]=="string")
	   { 
	    var mrk=L.marker([liste[1],liste[2]]).addTo(map_a620533b73fc4a38880428953e8ae81f)
	                .bindPopup("<br>"+liste[0]+" </br>" )
	                .openPopup();
	    }
	  else {// dans le cas ou c une liste exp heuristique3

	    var   adr='';
	    for (i in liste[0]){
	      adr=adr+liste[0][i]+' ';
	    }
	    
	    var mrk=L.marker([liste[1],liste[2]]).addTo(map_a620533b73fc4a38880428953e8ae81f)
	                .bindPopup("<br>"+adr+" </br>" )
	                .openPopup();
        }
	}
	}



fetch("data.json")
.then(response => {
   return response.json();
})
.then(data => affichage(data) )
let affichage = (data) => {
    let stringData = JSON.stringify(data);
    let obj = JSON.parse(stringData) 
    for (var key in obj) {
        var myDiv = document.getElementById("resultat_heuristique");
        if(obj[key]['url'] == page_type)
        {
        const heuristiques = [];

            if(obj[key].hasOwnProperty('heuristique 2'))
            {  heuristiques.push( [  obj [key]['heuristique 2'][0], 'id2' ] );
               marker  (obj [key]['heuristique 2']  );

             }
              

            if(obj[key].hasOwnProperty('heuristique3_adresse'))
            {    heuristiques.push( [  obj [key]['heuristique3_adresse'][0], 'id3' ] );
                 marker  (obj [key]['heuristique3_adresse']  );
                 
             }
            
            if(obj[key].hasOwnProperty('heuristique 5'))
            {    heuristiques.push( [  obj [key]['heuristique 5'][0], 'id5' ] );
                 marker  (obj [key]['heuristique 5']  );
            }

            if(obj[key].hasOwnProperty('heuristique_country_cities'))
            {
                heuristiques.push([ obj [key]['heuristique_country_cities'][0], 'id6' ] );
               marker (obj[key]['heuristique_country_cities']);
                    
            } 
            if(obj[key].hasOwnProperty('heuristique_adresse_LT'))
            { 
              heuristiques.push(  [  obj [key]['heuristique_adresse_LT'][0]   ,  'id7'] );  
              marker (obj[key]['heuristique_adresse_LT'] );  // on lui passe l'adresse et lat et lng 
              
            }

            if(obj[key].hasOwnProperty('resultat_Spacy'))
            {
                heuristiques.push([ obj [key]['resultat_Spacy'][0],'id8' ] );  
                marker (obj [key]['resultat_Spacy'] );
              }

              heuristiques.push(['Aucune','id9']);

              const map =new Map(heuristiques);
              const tab = Array.from(map);

              // generate the radio groups        
              const group = document.querySelector("#resultat_heuristique");
           
              group.innerHTML = tab.map( (tab) =>  ` <div id="inputGroup"> 
              <div id="${tab[1]}" style = "
    position: absolute; 
    width: 30px;
    height: 30px;
    border-radius: 20px;
    right: 60px;
    z-index:2;
    margin-top: 9px;

    "> </div> 


                <input type="radio" name="size" value="${tab[0] }" id="${tab[1]}"   >
                <label onclick="cbclick('${tab[0] }','${tab[1]}')" for="${tab[0] }"> ${tab[0] }</label> 
            </div>`
            ).join(' ');
         
         }
    }

}
function miseenattente(){ window.open('boutonconfirmation.html?ul='+ page_type);
    window.open('boutonconfirmation.html?ul='+ page_type);
    window.open('boutonconfirmation.html?ul='+ page_type);
    window.open('boutonconfirmation.html?ul='+ page_type);

}

function cbclick(d,id)
{  num_heur=id[2];
	
	fetch("data.json")
	.then(response => {
   return response.json();
    })
    .then(data => func(data) )
    let func = (data) => {
     let stringData = JSON.stringify(data);
     let obj = JSON.parse(stringData) 
     for (var key in obj )
    {   let liste_heuristique = ['heuristique 2','heuristique3_adresse','heuristique 4','heuristique 5','heuristique_country_cities','heuristique_adresse_LT','resultat_Spacy'] ; 
        val=liste_heuristique[Number(num_heur)-2];
        

           if (obj[key] ['url'] == page_type )
	        {  if ( obj [key][val].length ==3)  
	          { var marker = L.marker([obj [key][val][1], obj [key][val] [2] ])
	          .addTo(map_a620533b73fc4a38880428953e8ae81f)
	           .bindPopup("<p>"+obj[key]['title'].slice(0, obj[key]['title'].length-17)  +"\r\n\tLocalisation:"+ obj[key][val][0] +" </p><img src = "+page_type+"  width='300' height='234' >")
	           .openPopup(); 
            //    change value of button
                document.getElementById("button").value =obj [key][val];
              }else {     alert('coordonées introuvables');
                    }
	        }
    }
     }
}

function  image_heur(h ,pg )
{  
var marker = L.marker([h[1], h[2] ])
              .addTo(map_a620533b73fc4a38880428953e8ae81f)
               .bindPopup("<p>"+h[0]+" </p><img src = "+pg+"  width='300' height='234' >")
               .openPopup();  
console.log(h[1]);
document.getElementById("button").value =h[0]+","+h[1]+","+h[2];
}
fetch("data.json")
.then(response => {
   return response.json();
})
.then(data => myFile(data) )
let myFile = (data) => {
    let stringData = JSON.stringify(data);
    let obj = JSON.parse(stringData) 
     for (var key in obj )
{         if (obj[key] ['url'] == page_type  )
        {     if ( obj[key]['heuristique_adresse_LT'] !== undefined &&  obj [key]['heuristique_adresse_LT'].length==3  )
              {
                 image_heur( obj [key]['heuristique_adresse_LT']  ,page_type);
              }
              else { if (obj[key]['heuristique 5'] !== undefined &&  obj [key]['heuristique 5'].length==3 )
                    {  
                           image_heur(obj [key]['heuristique 5'],page_type);
                    }
                    else
                     {  if(obj[key].hasOwnProperty('heuristique_country_cities') && obj [key]['heuristique_country_cities'].length==3  )
                           {
                             image_heur(obj [key]['heuristique_country_cities'],page_type);    
                           }
                           else {
                                   if (obj [key].hasOwnProperty('resultat_Spacy') && obj [key]['resultat_Spacy'].length==3)
                                    {
                                        image_heur( obj [key]['resultat_Spacy'],page_type );  
                                    }else 
                                    {  if (obj [key].hasOwnProperty('heuristique3_adresse') && obj [key]['heuristique3_adresse'].length==3)
                                        {
                                           image_heur( obj [key]['heuristique3_adresse'],page_type);  
                                         }else{
                                             if (obj [key].hasOwnProperty('heuristique 2') && obj [key]['heuristique 2'].length==3)
                                             {
                                                image_heur( obj [key]['heuristique 2'],page_type); 
                                             }
                                         }
                                     }
                                 }
                    }
                    }
}   
}
}
  
function bt()
{    
    <?php
       echo "var jsvar ='$url';";
   ?>
  document.getElementById("button").innerHTML= "index.html"    ;
   
    console.log(jsvar);

}  
</script>
