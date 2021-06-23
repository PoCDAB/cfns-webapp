
function map_init (map, options) {
    // Use Leaflet API here
    var datasets = new L.GeoJSON.AJAX("{% url 'ais-data' %}", {

    });

    datasets.addTo(map);

    // Download GeoJSON via Ajax
    //$.getJSON(dataurl, function (data) {
        // Add GeoJSON layer
       // L.geoJson(data).addTo(map);
    //});
}