function main_map_init (map, options) {
    // Use Leaflet API here
    var dataurl = '{% url "ais-data" %}';
    // Download GeoJSON via Ajax
    $.getJSON(dataurl, function (data) {
        // Add GeoJSON layer
        L.geoJson(data).addTo(map);
    });
  }