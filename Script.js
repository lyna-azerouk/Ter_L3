function foo(file){
    const img= document.getElementById('img');
    let data=fetch(file)
    .then(response => response.json())
    .then(data => { img.src = data.image0.url
        return data})

    }  
foo("data.json")
        