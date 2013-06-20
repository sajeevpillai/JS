
function swapImg(elem, filename, event){
    
    event.stopPropagation();        

    if (document.getElementById(elem).src !== filename){
        document.getElementById(elem).src = filename;                         
    }                            
    
}

function showSlider(params){
  document.getElementById('button-overlay').style.display = "block";
  document.getElementById('sofia-bottom').style.opacity = 0;
  document.getElementById('bottom-img').src = params.content;                         
  document.getElementById('sofia-bottom').style.left = params.left;    
  document.getElementById('sofia-bottom').style.opacity = 1;
  
  $('#sofia-bottom').animate({ 
      left: "0px"
    }, 1000, function(){
      document.getElementById('button-overlay').style.display = "none";
  });
}

function onTouchItem(elem, filename, event, left, width, popup_filename, sliderclass, arrowclass){
    swapImg(elem, filename, event);    
    showSlider({left: left,
                width: width,
                bSlide: false,
                content:popup_filename,
                classname:sliderclass,
                arrowClassname:arrowclass});
}

var bVisible = false;

function didBecomeInvisible() {
    bVisible = false;
    document.getElementById('div#sofia-textslider').style.left = '769px';
}

function didBecomeVisible(){
    
    if (bVisible) { 
        return; 
    } else { 
        bVisible = true; 

        setTimeout(function(){
                    showSlider({left: '-736px', 
                                width:'736px',
                                bSlide: true,
                                content:'../images/lybl_main06_slide_1.png',
                                classname:'B1_content',
                                arrowClassname:'sofia1'});
                },1000);
        
    }
}

window.onload = function(){
    
    didBecomeVisible();
};