

<!DOCTYPE html>
<head>
<script src="js/FileSaver.js"></script>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
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
        <div class="folium-map" id="map_a620533b73fc4a38880428953e8ae81f"  ></div>
        <div id ="resultat_heuristique"   >  </div>
        <?php
    if(isset($_COOKIE['realloc'] )){
        echo "Hello";
        echo "{$_COOKIE['realloc']}";
    } 
?> 
   
</body>

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
            


fetch("data.json")
.then(response => {
   return response.json();
})
.then(data => myFile(data) )
let myFile = (data) => {
    let stringData = JSON.stringify(data);
    let obj = JSON.parse(stringData) 
     for (var key in obj )
{         if (obj[key] ['url'] == page_type &&     obj[key].hasOwnProperty('realLoc') )
        {
            // var marker = L.marker([obj [key]['realLoc']['Latitude'], obj [key]['realLoc'] ['Longitude'] ])
           // .addTo(map_a620533b73fc4a38880428953e8ae81f)
           // .bindPopup("<p>"+obj [key]['realLoc']['Nomreal']+" </p><img src = "+page_type+"  width='300' height='234' >")
            //.openPopup(); 
          
            
        }
}   
}

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

    $(document).ready(function () {
  createCookie("realloc", localStorage.getItem("realloc"), "1");
});

function createCookie(name, value, days) {
  var expires;
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    expires = "; expires=" + date.toGMTString();
  }
  else {
    expires = "";
  }
  document.cookie = escape(name) + "=" + escape(value) + expires + "; path=/";
}

 function clickrealloc (loc){
     localStorage.setItem("realloc",loc);
     console.log(localStorage.getItem("realloc")); 
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

            if(obj[key]['heuristique 2'] !== undefined)
            {  heuristiques.push( [  obj [key]['heuristique 2'], 'id2' ] );
               marker  (obj [key]['heuristique 2']  );
             }
              

            if(obj[key]['heuristique3_adresse'] !== undefined)
            {    heuristiques.push( [  obj [key]['heuristique3_adresse'], 'id3' ] );
                 marker  (obj [key]['heuristique3_adresse']  );
                 
             }
            
            if(obj[key]['heuristique 5'] !== undefined)
            {    heuristiques.push( [  obj [key]['heuristique 5'], 'id5' ] );
                 marker  (obj [key]['heuristique 5']  );
            }

            if(obj[key]['heuristique_country_cities'] !== undefined)
            {
                heuristiques.push([ obj [key]['heuristique_country_cities'], 'id6' ] );
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
                const map =new Map(heuristiques);
                const tab = Array.from(map);
                console.log(tab);
              // generate the radio groups        
              const group = document.querySelector("#resultat_heuristique");
           
                group.innerHTML = tab.map( (tab) =>  `<div id = "inputGroup"> 
                <input type="radio" name="size" value="${tab[0] }" id="${tab[1]}"   >
                <label onclick="clickrealloc('${tab  [0] }')" for="${tab[0] }"> ${tab  [0] }</label>

            </div>` 
            ).join(' ');
         
         }
    }

}
/// IMPORTANT : EST CE QUE ON SUPPRIME LES MARKER APRES 
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
	        {    
	          var marker = L.marker([obj [key][val][1], obj [key][val] [2] ])
	          .addTo(map_a620533b73fc4a38880428953e8ae81f)
	           .bindPopup("<p>"+obj [key][val][0]+" </p><img src = "+page_type+"  width='300' height='234' >")
	           .openPopup(); 
	           
	                                                                    
	            }
    }
                                                         
         
                                                       }
}
  
               



</script>
