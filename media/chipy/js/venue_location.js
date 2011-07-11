
function mapVenue(venueLatLng) {
  var canvas = document.getElementById("map_canvas_venue");
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
      position: venueLatLng
  };
  var map_marker = new google.maps.Marker(markerOpts);
};
