var geocoder = new google.maps.Geocoder();

function mapVenue(mapdiv,venueLatLng) {
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
      position: venueLatLng
  };
  var map_marker = new google.maps.Marker(markerOpts);
};
