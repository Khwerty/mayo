function toggle(){
  menuOptions = document.getElementById("drop")

  menuOptions.classList.toggle("show")
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbutton')) {
    var dropdowns = document.getElementsByClassName("drop");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
} 

function toClipboard( el ) {
  
  text = el.innerHTML

  navigator.clipboard.writeText( text );
}
function showDetail( el ){
  id = el.getAttribute("name")
  document.getElementById( id ).style.display = "flex";
}
function hideDetail( id ){
  ele = document.getElementById( id )
  ele.style.display = "none";
}
function showAdv( id ){
  adv = document.getElementById("adv_"+id)
  adv.style.display = "flex";
}
function hideAdv( id ){
  adv = document.getElementById("adv_"+ id)
  adv.style.display = "none";
}
function showMm(){  
  document.getElementById("message_id").style.display = "flex";
  toggle()
}
function hideMm(){  
  document.getElementById("message_id").style.display = "none";
  
}
