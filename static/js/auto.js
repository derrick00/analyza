let slideIndex = 0;
let slides = Array.from(document.getElementsByClassName("mySlides"));
let dots = Array.from(document.getElementsByClassName("dot"));
let i;
let alert = document.querySelector(".alert")
alert.style.display = "none"

function showSlides() {
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    alert.style.display = "block"
    return;
  }    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 7000); 
}
function alertButton(){
  slides[i].style.display = "none";  
  return;
}

showSlides();
