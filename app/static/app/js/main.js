function ChangeCheckboxLabel(ckbx)
    {
       var d = ckbx.id;
       if( ckbx.checked )
       {
        document.getElementById(d+"-checked").style.display = "none";
          document.getElementById(d+"-unchecked").style.display = "inline";
          
       }
       else
       {
        document.getElementById(d+"-checked").style.display = "inline";
          document.getElementById(d+"-unchecked").style.display = "none";
       }
    }


function setmin1(){
    var today = new Date();
    var h = today.getHours().toString(); 
    var m = today.getMinutes().toString();
    if (h.length== 1) {
        h = '0' + h;
    }
    if (m.length== 1) {
        m = '0' + m;
    }
    time = h + ':' + m
    document.getElementById('start-time').min = new Date().toISOString().split("T")[0] + "T" + time;
    document.getElementById('start-time').value = new Date().toISOString().split("T")[0] + "T" + time;

}

function setmin2(){
    var today = new Date();
    var h = today.getHours().toString(); 
    var m = today.getMinutes().toString();
    if (h.length== 1) {
        h = '0' + h;
    }
    if (m.length== 1) {
        m = '0' + m;
    }
    time = h + ':' + m
    document.getElementById('end-time').min = new Date().toISOString().split("T")[0] + "T" + time;
    document.getElementById('end-time').value = new Date().toISOString().split("T")[0] + "T" + time;
}