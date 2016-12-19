$(function () {
    const startId = "ChIJCflhUV2rNTER4yviDFCvr00";
    const endId = "ChIJLcFRgHisNTERWJwBwSBcev8";
    const outputFormat = "json";
    const origin = "origin=place_id:" + startId;
    const destination = "destination=place_id:" + endId;
    const key = "AIzaSyB7oMQlJ4r30K8Gl4gQuPD0H7G1rkclVWY";
    const clientId = "key=" + key;
    const parameters = "?" + origin + "&" + destination + "&" + clientId;
    let requestURL = "https://maps.googleapis.com/maps/api/directions/" + outputFormat + parameters;
    console.log(requestURL);
    $.ajax({
        url: requestURL,
        type: "GET",
        beforeSend: function (xhr) { xhr.setRequestHeader('Origin', 'http://localhost'); },
        success: function (data) {
            console.log(data);
        }
    });
});