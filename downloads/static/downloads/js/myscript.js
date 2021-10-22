

const api_url =  "https://api.quotable.io/random";
  
// Defining async function
async function getapi(url) {

    // Storing response
    const response = await fetch(url);
    
    // Storing data in form of JSON
    var data = await response.json();
    var i = 0;
    var contents = '"  '+ data['content'] + '  "';
    var speed = 60;
    
  function typeWriter() {
      if (i < contents.length) {
        document.getElementById("quote").innerHTML += contents.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
      }
     
    }

typeWriter();
document.getElementById("author").innerHTML ='-'+ data['author'];
}

getapi(api_url);





