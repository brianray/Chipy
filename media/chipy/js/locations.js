$(function() {
  // Google Map options
  // var myLatLng = new google.maps.LatLng(lat,lng);
  var myLatLng = new google.maps.LatLng(41.965972,-87.690372);
  var myCanvas = document.getElementById("map_canvas");
  var myMapOpts = {
	  zoom: 12,
	  center: myLatLng,
	  mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  var map_canvas = new google.maps.Map(myCanvas, myMapOpts);

  // Add markers to the map_canvas from the _geo array of points
  //
  if(map_canvas) {
	// add location markers from the _geo tuple to the map
	var markers = new Array();
	for(var i = 0; i < _geo.length; ++i) {
		var g = _geo[i];
		var markerLatLng = new google.maps.LatLng(g[0], g[1]);
		markers[i] = new google.maps.Marker({
											position: markerLatLng,
											map: map_canvas,
											title: g[2]
											});
		}
	}
});