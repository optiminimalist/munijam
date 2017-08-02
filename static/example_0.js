$(function() {
    // Setup leaflet map
    var map = new L.Map('map');

    var basemapLayer = new L.TileLayer('http://{s}.tiles.mapbox.com/v3/github.map-xgq2svrz/{z}/{x}/{y}.png');

    // Center map and default zoom level
    map.setView([37.757921, -122.434762], 13);

    // Adds the background layer to the map
    map.addLayer(basemapLayer);

    // =====================================================
    // =============== Playback ============================
    // =====================================================

    // Playback options
    var playbackOptions = {
        playControl: true,
        dateControl: true,
        sliderControl: true
    };


    // Initialize playback
    $.get("/by_vehicle_geojson", function(r){
        console.log(r);
        var playback = new L.Playback(map, r, null, playbackOptions);
        playback.start();

    });
});