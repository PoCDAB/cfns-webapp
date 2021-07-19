function addDataset({url, popuptitle, popupfields = null, fa_icon = null, image_path = null, color = null, rotationcorrection = 0, isCircle=false}) {
    return new L.GeoJSON.AJAX(url, {
        pointToLayer: function (feature, latlng) { return pointToLayer(feature, latlng, fa_icon, image_path, color, rotationcorrection, isCircle)},
        onEachFeature: function (feature, layer) {
            onEachFeature(feature, layer, popuptitle, popupfields)
        }
    });  
}

function onEachFeature(feature, layer, popuptitle, popupfields) {
    text = ''
    if (popuptitle != null) {
        text += "<h6 class='text-center'><b>" + popuptitle + "</b></h6></br>"
    }
    if (popupfields != null) {
        for (const [key, value] of Object.entries(popupfields)) {
            result = null
            if (key.includes(".") && typeof feature?.properties[key] === 'object' && feature?.properties[key] !== null) {
                subpropertie = feature?.properties[key.split(".")[0]]
                if (subpropertie && subpropertie !== null) {
                    for (var i = 1; i < key.split(".").length; i++) {
                        nextKey = key.split(".")[i]
                        subpropertie = subpropertie[nextKey]
                    }
                    result = subpropertie
                }
            } else if (typeof feature?.properties[key] === 'object' && feature?.properties[key] !== null) {
                result = "Ok!"
            } else {
                result = feature?.properties?.[key]
            }
            text += "<b>" + value + ":</b> " + (result?.toString() || "<i>Niet bekend</i>") + "</br>"
        }
        text += "<b>Location:</b> </br>&nbsp;" + (feature?.geometry?.coordinates?.toString().replaceAll(',',',</br>&nbsp;') || "<i>Niet bekend</i>") + "</br>"

    } else {
        text +=  JSON.stringify(feature.properties,null,'</br>')
        text +=  JSON.stringify(feature.geometry,null,'</br>')
    }
    layer.bindPopup(text)
};

// Edits the point on the layer. Add icon, image or circle at point x,y
function pointToLayer(feature, latlng, fa_icon, image_path, color, rotationcorrection, isCircle) {
    if (image_path || fa_icon || isCircle) {
        icon = null;
        if (fa_icon) {
            icon = faIcon(fa_icon, color)
        } else if (image_path ) {
            icon = imgIcon(image_path)
        }

        if (isCircle) {
            return L.circle(latlng, { radius: feature.properties?.radius, color: color})
        } else {
            return L.marker(latlng, { icon: imgIcon(image_path), icon: icon, rotationAngle: (feature.properties?.course || 0) + rotationcorrection })
        }
    } else {
        return L.marker(latlng)
    }
}

// Add static image via img_path
function imgIcon(img_path) {
    return L.icon({
        iconUrl: img_path,
        iconSize: [38, 38], // size of the ico
        iconAnchor: [19, 19],
        popupAnchor: [0, -10], // point from which the popup should open relative to the iconAnchor
        className: ''
    });
}

// Add Fontawesome icon via fontawesome_icon with some color
function faIcon(fontawesome_icon, color) {
    html = '<i class="fa '+fontawesome_icon+' fa-3x" style="color:'+color+'; text-align: center;width:100%"></i>'
    return L.divIcon({
      html: html,
      iconSize: [40, 40], // size of the ico
      iconAnchor: [20, 20],
      popupAnchor: [0, -20], // point from which the popup should open relative to the iconAnchor
      className: ''
    });
}