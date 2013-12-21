function playMP3(url){
    var audioElement = document.createElement('audio');
    audioElement.setAttribute('src', url);
    audioElement.load();
    audioElement.addEventListener("canplay", function() {
        audioElement.play();
    });
}