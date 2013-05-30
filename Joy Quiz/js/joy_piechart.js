/*
Need to import common.js as well for these functions to function properly
*/

var generate_fun_chart = 'true';

function displayPieChart(type){
                var div_prefix = "";
                if (type == "fun"){
                  div_prefix= "fun_";
                }
                document.getElementById(div_prefix +'act_img_misc').src = "";
                document.getElementById(div_prefix + 'time_misc').value = "";
                opacityHide(div_prefix + 'act_img_misc');
                var cn = document.querySelectorAll('.'+ div_prefix + 'titles');
                var prev_hours = 0;
                var hr_str = "";
                var j;
                if (calculateTotalHours(type)){
                  if (cn[1]&& cn[1].value){opacityShow(div_prefix + 'act_img_01')};
                  for (i = 0; i < cn.length; i++) {        
                    if (cn[i] && cn[i].value){
                        j = i + 1;
                        if (j<10){j = '0'+ j}
                        //if (prev_hours >= 24){alert('You have entered more than 24 hours.  Please make sure that your activites add up to less than or equal to 24 hours.');}
                        if (prev_hours == 0){
                            document.getElementById(div_prefix + 'act_img_' + j).src = "../images/joy_piechart/act" + j + "_00.png";
                            opacityShow(div_prefix + 'act_img_' + j);
                        } else {
                            if (prev_hours < 24){
                                if (prev_hours < 10 ){
                                    hr_str = "0" + prev_hours;
                                }else{
                                    hr_str = prev_hours.toString();
                                }
                                document.getElementById(div_prefix + 'act_img_' + j).src = "../images/joy_piechart/act" + j + "_" + hr_str + ".png";
                                opacityShow(div_prefix + 'act_img_' + j);
                            }
                        }
                        prev_hours = prev_hours + parseInt(document.getElementById(div_prefix+'time_' + (j)).value);
                        if (prev_hours > 24){
                                generate_fun_chart = 'false';
                                display(div_prefix + 'error_div');
                                return;
                                //alert('You have entered more than 24 hours.  Please make sure that your activites add up to less than or equal to 24 hours.');
                        }
                    }         
                  }
                  if (prev_hours != 0 && prev_hours < 24){
                    if (prev_hours < 10 ){hr_str = "0" + prev_hours;}else{hr_str="" + prev_hours;}
                    /*act10 img will need to be changed to act_misc*/
                    document.getElementById(div_prefix +'act_img_misc').src = "../images/joy_piechart/act_misc_" + hr_str + ".png";
                    opacityShow(div_prefix + 'act_img_misc');
                    document.getElementById(div_prefix + 'time_misc').value = 24 - prev_hours;
                  }
                }
}

function calculateTotalHours(type){
                var div_prefix = "";
                if (type == "fun"){
                  div_prefix= "fun_";
                }
                var cn = document.querySelectorAll('.'+ div_prefix + 'times');
                var prev_hours = 0;
                var hr_str = "";
                var j, id;
                for (i = 0; i < (cn.length - 1); i++) {
                    if (cn[i] && cn[i].value){
                                j = i + 1;
                                if (j<10){j = '0'+ j}
                                id = div_prefix+'time_' + (j);
                                prev_hours = prev_hours + parseInt(document.getElementById(id).value);
                    }
                }
                
                if (prev_hours > 24){
                    generate_fun_chart = 'false';
                    display(div_prefix + 'error_div');
                    return false;
                } else {
                    return true;
                }
}
            
function resetActivities(type){
                var div_prefix = "";
                var numOfActivities = 9;
                if (type == "fun"){
                  div_prefix= "fun_";
                  numOfActivities = 13;
                }
                var cn = document.querySelectorAll('.'+div_prefix +'titles');
                var j;
                opacityHide(div_prefix +'act_img_01');
                for (i = 0; i < cn.length; i++) {        
                    if (cn[i] && cn[i].value){
                        j = i + 1;
                        if (j<10){j = '0'+ j}
                        document.getElementById(div_prefix +'title_' + j).value = "" ;
                        document.getElementById(div_prefix +'time_' + j).value = "" ;
                        document.getElementById(div_prefix +'act_img_' + j).src ="";
                    }         
                }
                for (i = 1; i <=numOfActivities; i++) {
                    if (i<10){i = '0'+ i}
                    opacityHide(div_prefix +'act_img_' + i);
                }
                document.getElementById(div_prefix +'act_img_misc').src = "";
                document.getElementById(div_prefix + 'time_misc').value = "";
                opacityHide(div_prefix + 'act_img_misc');
}
            
/*This function transfers the text to the fun activities*/
function populateFunActivitiesText(){
                var cn = document.querySelectorAll('.titles');
                var j;
                
                for (i = 0; i < cn.length; i++) {        
                    if (cn[i] && cn[i].value){
                                j = i + 1;
                                document.getElementById('fun_title_0' + j).value = document.getElementById('title_0' + j).value;
                                document.getElementById('fun_time_0' + j).value = document.getElementById('time_0' + j).value;
                    }
                }
                if (document.getElementById('time_misc').value){
                                document.getElementById('fun_time_misc').value = document.getElementById('time_misc').value;
                }else{
                                document.getElementById('fun_time_misc').value = "";
                }
}
            
function calculateActivites(){
                //set generate_fun_chart = 'true';
                generate_fun_chart = 'true';
                
                //clear pie chart
                for (i = 1; i <=9; i++) {
                    document.getElementById('act_img_0' + i).src ="";
                    opacityHide('act_img_0' + i);
                }
                
                //generate regualar pie chart
                displayPieChart('reg');
                                
                if (generate_fun_chart == 'true'){
                                //reset fun chart
                                resetActivities('fun');
                                //populate the fun chart
                                populateFunActivitiesText();
                
                                //generate the fun chart
                                displayPieChart('fun');
                }
}
            
function calculateFunActivites(){
                //clear  fun pie chart
                for (i = 1; i <=13; i++) {
                    if (i<10){
                                document.getElementById('fun_act_img_0' + i).src ="";
                                opacityHide('fun_act_img_0' + i);
                    }else{
                                document.getElementById('fun_act_img_' + i).src ="";
                                opacityHide('fun_act_img_' + i);                                
                    }
                }
                                
                //generate the fun chart
                displayPieChart('fun');
}

            
