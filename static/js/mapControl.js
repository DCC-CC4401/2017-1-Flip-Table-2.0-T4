/**
 * Created by diego on 6/26/2017.
 */

var image = {
    url: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png',
    // The origin for this image is (0, 0).
    origin: new google.maps.Point(0, 0),
    // The anchor for this image is the base of the flagpole at (0, 32).
    anchor: new google.maps.Point(0, 32)
};
var lineSymbol = {
    path: google.maps.SymbolPath.CIRCLE,
    scale: 8,
    strokeColor: '#ffff00'
};
var shape = {
    coords: [1, 1, 1, 20, 18, 20, 18, 1],
    type: 'poly'
};
var myCenter = new google.maps.LatLng(-33.457684, -70.665032);
var marker, marker2, marker3;
function initialize() {
    var mapProp = {
        center: myCenter,
        zoom: 16,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
    marker = new google.maps.Marker({
        position: myCenter,
        // icon:'themes/assets/images/nepali-momo.png',
        animation: google.maps.Animation.BOUNCE
    });
    marker2 = new google.maps.Marker({
        position: myCenter,
        icon: image,
        shape: shape,
        title: "FavoriteSeller",
        url: "SellerBuyerInterface.html"
    });
    marker3 = new google.maps.Marker({
        position: myCenter,
        icon: lineSymbol,
        shape: shape,
        title: "Seller",
        url: "SellerBuyerInterface.html"
    });
    marker.setMap(map);
    marker2.setMap(map);
    marker3.setMap(map);
    google.maps.event.addListener(marker2, 'click', function () {
        window.location.href = marker2.url;
    });
    google.maps.event.addListener(marker3, 'click', function () {
        window.location.href = marker3.url;
    });
    // Info open
    //var infoWindow = new google.maps.InfoWindow({map: map});
    centerMap(map);
    var centerControlDiv = document.createElement('div');
    var centerControl = new CenterControl(centerControlDiv, map);
    centerControlDiv.index = 1;
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(centerControlDiv);
}
function centerMap(map) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            //infoWindow.setPosition(pos);
            marker.setPosition(pos);
            marker2.setPosition(new google.maps.LatLng(pos.lat - 0.0005, pos.lng - 0.0005));
            marker3.setPosition(new google.maps.LatLng(pos.lat + 0.0005, pos.lng + 0.0005));
            //infoWindow.setContent('Location found.');
            map.setCenter(pos);
        });
    } else {
        // Browser doesn't support Geolocation
        //handleLocationError(false, infoWindow, map.getCenter());
    }
}
function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
        'Error: The Geolocation service failed.' :
        'Error: Your browser doesn\'t support geolocation.');
}
function CenterControl(controlDiv, map) {
    // Set CSS for the control border.
    var controlUI = document.createElement('div');
    controlUI.style.backgroundColor = '#fff';
    controlUI.style.border = '2px solid #fff';
    controlUI.style.borderRadius = '3px';
    controlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
    controlUI.style.cursor = 'pointer';
    controlUI.style.marginBottom = '22px';
    controlUI.style.textAlign = 'center';
    controlUI.title = 'Click to recenter the map';
    controlDiv.appendChild(controlUI);
    // Set CSS for the control interior.
    var controlText = document.createElement('div');
    controlText.style.color = 'rgb(25,25,25)';
    controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
    controlText.style.fontSize = '16px';
    controlText.style.lineHeight = '38px';
    controlText.style.paddingLeft = '5px';
    controlText.style.paddingRight = '5px';
    controlText.innerHTML = 'Center Map';
    controlUI.appendChild(controlText);
    // Setup the click event listeners: simply set the map to Chicago.
    controlUI.addEventListener('click', function () {
        centerMap(map);
    });
}
google.maps.event.addDomListener(window, 'load', initialize);