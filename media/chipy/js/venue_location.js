
function mapVenue(mtgLatLng) {
  var canvas = document.getElementById("map_canvas_mtg");
  var mapOpts = {
	  zoom: 12,
      draggable: false,
	  center: mtgLatLng,
	  mapTypeId: google.maps.MapTypeId.ROADMAP,
      mapTypeControl: false,
      scaleControl: false,
      scrollWheel: false,
      streetViewControl: false
  };
  var mapCanvas = new google.maps.Map(canvas, mapOpts);
  var markerOpts = {
      map: mapCanvas,
      position: mtgLatLng
  };
  var map_marker = new google.maps.Marker(markerOpts);
};
