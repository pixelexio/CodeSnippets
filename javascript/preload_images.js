/*
File: preload_images.js
For learning purposes
*/

var images = new Array();
function preloadImages(){
    for (i=0; i < preloadImages.arguments.length; i++){
        images[i] = new Image();
        images[i].src = preloadImages.arguments[i];
    }
}

preloadImages("image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg");
