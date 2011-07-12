var geocoder = new google.maps.Geocoder();

function drawMapThumb(mapdiv,address,label) {
  var canvas = mapdiv;
  var mapOpts = {
	  zoom: 12,
      draggable: false,
	  center: venueLatLng,
	  mapTypeId: google.maps.MapTypeId.ROADMAP,
      mapTypeControl: false,
      scaleControl: false,
      scrollWheel: false,
      streetViewControl: false
  };
    
  var mapCanvas = new google.maps.Map(canvas, mapOpts);
  var markerOpts = {
      map: mapCanvas,
      position: venueLatLng,
      title: label
  };
  var map_marker = new google.maps.Marker(markerOpts);
};

function geocodeCatcher(results,status) {
  // puke if status is not happiness
  // otherwise call drawMapThumb
}

function mapVenue(mapdiv,address,label) {
  geocoder.Geocode(stuff);
}
