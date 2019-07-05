console.log("Working");

var refresh = document.getElementById('b')
var cells = document.getElementsByTagName('td')

refresh.addEventListener('click',resetGrid)

function resetGrid(){
  for (var i=0; i < cells.length; i++){
    cells[i].textContent=''
  }
  console.log("Grid reset!");
}

function rotateStep(){
  console.log("Rotate executed!");
  if (this.textContent===''){
    this.textContent='X';
  } else if (this.textContent==='X'){
    this.textContent='O';
  } else if (this.textContent==='O'){
    this.textContent='';
  }
}

for (var i=0; i < cells.length; i++){
  cells[i].addEventListener('click',rotateStep);
}
console.log("Game setup done!");
