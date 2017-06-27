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
var user;
var markers = new Array();
var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';
function initialize() {
    var mapProp = {
        center: myCenter,
        zoom: 18,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
    user = new google.maps.Marker({
        position: myCenter,
        icon: iconBase + 'target.png'
    });
    user.setMap(map);
    centerMap(map);
    var centerControlDiv = document.createElement('div');
    var centerControl = new CenterControl(centerControlDiv, map);
    centerControlDiv.index = 1;
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(centerControlDiv);
}

function addMarker(lt, lng, id) {
    var pos = new google.maps.LatLng(lt, lng);
    var marker = new google.maps.Marker({
        position: pos,
        icon: iconBase + 'dining.png',
        url: "/showcase/" + id
    });
    google.maps.event.addListener(marker, 'click', function () {
        window.location.href = marker.url;
    });
    marker.setMap(map);
    markers.push(marker)
}

function addFavoriteMarker(lt, lng, id) {
    var pos = new google.maps.LatLng(lt, lng);
    var marker = new google.maps.Marker({
        position: pos,
        icon: iconBase + 'star.png',
        animation: google.maps.Animation.BOUNCE,
        url: "/showcase/" + id
    });
    google.maps.event.addListener(marker, 'click', function () {
        window.location.href = marker.url;
    });
    marker.setMap(map);
    markers.push(marker)
}

function centerMap(map) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function (position) {
                var pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };
                //infoWindow.setPosition(pos);
                user.setPosition(pos);
                //infoWindow.setContent('Location found.');
                map.setCenter(pos);
                map.setZoom(18);
            }
        );
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