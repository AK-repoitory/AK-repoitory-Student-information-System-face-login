
function click() {
  var permission = document.getElementById('face_').checked;

  if (permission == true ){
    alert(permission);
    // document.getElementById('lol').dataset.target="#loginmodel";
    document.getElementById('face_').dataset.target="#face";
  }
  else if (permission == false) {
document.getElementById('face_').dataset.target="#loginmodel";
  }


}
document.getElementById("face_").addEventListener("click", click);
