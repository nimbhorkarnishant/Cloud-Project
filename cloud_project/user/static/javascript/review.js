var x=document.getElementsByTagName("span");
for(var i=0;i<x.length;i++){
  x[i].addEventListener("click",function(){
    var value=this.getAttribute("value");
    clearClass();
    for(var j=value;j>0;j--){
      x[j].classList.toggle('a');
    }
  })
};

function clearClass(){
  var x=document.getElementsByTagName("span");
  for(var i=0;i<x.length;i++){
      x[i].classList.remove('a');
  };
}