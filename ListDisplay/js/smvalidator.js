/*** form validation functions ***/

function require_filled_out(formElement) {
    $(formElement).css('border', '1px solid red');
}

function reset_filled_out(formElement) {
    $(formElement).css('border', '1px solid #cccccc');
}

function check_filled_out(formElement, minChars) {
    var cleanElement = $(formElement).val().trim();
    if ($(formElement).val() != "" && $(formElement).val().length > minChars) {
        reset_filled_out(formElement);
        return true;
    } else {
        require_filled_out(formElement);
        return false;
    }
}

function check_filled_compare(formElement1, formElement2, minChars) {
  var cleanElement1 = $(formElement1).val().trim();  
  var cleanElement2 = $(formElement2).val().trim();
  if ($(formElement1).val() != "" && $(formElement1).val().length > minChars) {
    if (cleanElement1 == cleanElement2) {
      reset_filled_out(formElement1);
      reset_filled_out(formElement2);
      return true;
    }
  }
  require_filled_out(formElement1);
  require_filled_out(formElement2);
  return false;
}


function check_filled_ccnum(formElement) {
  var cleanElement = $(formElement).val().trim().replace(/-/g, '');
  cleanElement = cleanElement.replace(/ /g, '');
  //alert(cleanElement);

  if (cleanElement != "" && cleanElement.length > 15) {
    for (i=0; i<cleanElement.length; i++) {
        var isnum = cleanElement.charAt(i);
        if (isnum >= 0 && isnum <= 9) {
            continue;
        } else {
            require_filled_out(formElement);
            return false;
        }
    }
    reset_filled_out(formElement);
    return true;
  }
  require_filled_out(formElement);
  return false;  
}


function check_filled_year(formElement) {
  var cleanElement = $(formElement).val().trim();

  //alert(cleanElement);
  
  if (cleanElement < 2010) {
    require_filled_out(formElement);
    return false; 
  }

  if (cleanElement != "" && cleanElement.length == 4) {
    for (i=0; i<cleanElement.length; i++) {
        var isnum = cleanElement.charAt(i);
        if (isnum >= 0 && isnum <= 9) {
            continue;
        } else {
            require_filled_out(formElement);
            return false;
        }
    }
    reset_filled_out(formElement);
    return true;
  }
  require_filled_out(formElement);
  return false;  
}


function check_filled_select(formElement) {
  var cleanElement = $(formElement).val().trim();
  //alert(cleanElement);

  if (cleanElement != "" && cleanElement.length > 0 && cleanElement != "0") {
    reset_filled_out(formElement);
     return true;
  }
  
  require_filled_out(formElement);
  return false;  
}

function check_date(formElement, errorId){
  var validformat=/^\d{2}\/\d{2}\/\d{4}$/ //Basic check for format validity
  var date_input = $(formElement).val().trim();
  var returnval=false
  if (!validformat.test(date_input)){
    document.getElementById(errorId).innerHTML = "Invalid date format. Please use the mm/dd/yyyy format."
  }else{ //Detailed check for valid date ranges
    var monthfield=date_input.split("/")[0]
    var dayfield=date_input.split("/")[1]
    var yearfield=date_input.split("/")[2]
    var dayobj = new Date(yearfield, monthfield-1, dayfield)
    if ((dayobj.getMonth()+1!=monthfield)||(dayobj.getDate()!=dayfield)||(dayobj.getFullYear()!=yearfield) || yearfield < 1900)
      document.getElementById(errorId).innerHTML = "Invalid day, month or year detected. Please correct and submit again."
    else
      returnval=true
  }
  if (returnval==false) {
    require_filled_out(formElement);
  } else {
    reset_filled_out(formElement);
    document.getElementById(errorId).innerHTML = "";
  }

  return returnval
}




