var geocoder = new google.maps.Geocoder();

function drawMapThumb(mapdiv, venueLatLng, label, venueAddress) {
  var mapOpts = {
    zoom: 12,
    draggable: false,
    center: venueLatLng,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    disableDefaultUI: 1,
    mapTypeControl: false,
    scaleControl: false,
    scrollWheel: false,
    streetViewControl: false
  };
  
  // make the map pop
  var mapCanvas = new google.maps.Map(mapdiv, mapOpts);
  var markerOpts = {
      map: mapCanvas,
      position: venueLatLng,
      clickable: true,
      title: label
  };
  var map_marker = new google.maps.Marker(markerOpts);
  var google_maps_url = "http://maps.google.com/maps?q=" + venueAddress + "&sll=" + venueLatLng + "&z=16"
  google.maps.event.addListener(map_marker, 'click', function() {
      window.open(google_maps_url);
  });
};


