function displayOneOfSameClass(classname, id) {
      var cn = document.querySelectorAll('.'+classname);
        
      for (i = 0; i < cn.length; ++i) {        
          cn[i].style.display='none';          
      }        
    
      document.getElementById(id).style.display="block";
}

function displayOneOfClass(classname, id) {
      var cn = document.querySelectorAll('.'+classname);
        
      for (i = 0; i < cn.length; ++i) {        
          cn[i].style.display='none';          
      }        
    
      document.getElementById(id).style.display="block";
}

function hideAll(classname) {
      var cn = document.querySelectorAll('.'+classname);
        
      for (i = 0; i < cn.length; ++i) {        
          cn[i].style.display='none';          
      }        
}

function showAll(classname) {
      var cn = document.querySelectorAll('.'+classname);
        
      for (i = 0; i < cn.length; ++i) {        
          cn[i].style.display='block';          
      }        
}

function displayNone(id){
    document.getElementById(id).style.display="none";
    
}

function display(id){
    document.getElementById(id).style.display="block";
    
}

function makeHidden(id){
    document.getElementById(id).style.visibility="hidden";
    
}

function makeVisible(id){
    document.getElementById(id).style.visibility="visible";
    
}

function selectItem(id) {
    var pops = document.querySelectorAll('.pop');
        
    for (i = 0; i < pops.length; ++i) {        
          pops[i].style.display='none';          
    }        
    
    document.getElementById(id).style.display="block";
    showLinks();
}

function showLinks() {
      var links = document.querySelectorAll('.links');
      for (i = 0; i < links.length; ++i) {        
            links[i].style.display='block';          
      }
}

function swapImg(id, img){
      if (document.getElementById(id).src != img){
            document.getElementById(id).src = img;                         
      }
}

function toggleImg(id, img1, img2){
      if (document.getElementById(id).getAttribute('src') == img1){
            document.getElementById(id).setAttribute('src', img2);                         
      } else {
            if (document.getElementById(id).getAttribute('src') == img2){
                  document.getElementById(id).setAttribute('src', img1);                         

            }
      }
}

function toggleDisplay(id){
      if (document.getElementById(id).style.display=='block' ){
            document.getElementById(id).style.display='none';                 
      } else {
            document.getElementById(id).style.display='block'; 
      }
}

function opacityShow(id){
    document.getElementById(id).style.opacity=1;

}
function opacityHide(id){
    document.getElementById(id).style.opacity=0;
}
function toggleOpacity(id){
    if (document.getElementById(id).style.opacity==0){
      document.getElementById(id).style.opacity=1; 
    } else {
      document.getElementById(id).style.opacity=0; 
    }
}
