let RunEmotionDetection = ()=>{
    textToAnalyse = document.getElementById("textToAnalyse").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyse"+"="+textToAnalyse, true);
    xhttp.send();
}
