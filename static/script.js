var img= document.getElementById("img")
var slides = ["/static/images/ecom-banner1.jpg", "/static/images/ecom-banner1.png", "/static/images/ecom-banner3.JPG", "/static/images/ecom-banner4.jpg"];
var start = 0;

function slider(){
    if (start<slides.length){
        start=start+1;
    }
    else{
        start=1;
    }
    console.log(img);
    img.innerHTML = "<img src="+slides[start-1]+">"
}
setInterval(slider,2000);