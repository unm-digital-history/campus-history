---
layout: unm-base
title: UNM Campus History Essay Map
header-image: "/assets/images/1946 map to campus.jpg"
header-height: 0
background-position: "0px -20px"
---

<!-- Leaflet CSS/JS and Omnivore for KML support -->
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script src="https://unpkg.com/leaflet-omnivore@0.3.4/leaflet-omnivore.min.js"></script>

<script src="https://unpkg.com/leaflet-responsive-popup@0.2.0/leaflet.responsive.popup.js"></script>
<link rel="stylesheet" href="https://unpkg.com/leaflet-responsive-popup@0.2.0/leaflet.responsive.popup.css" />

<link href="{{site.baseurl}}assets/css/map.css" rel="stylesheet">


<div style="margin: 2em 0;">
  <label for="year-slider">Show buildings created up to year: <span id="year-value"></span></label>
  <input type="range" id="year-slider" min="1800" max="2025" value="2025" step="1">
</div>

<!-- close the container div for full width map -->
{::nomarkdown}
</div>
{:/nomarkdown}


<div id="map" style="height: 80vh;"></div>

<!-- Hidden data container for essays -->
<div id="map-data" style="display:none;">
  {% assign essays = site.pages | where_exp: "page", "page.path contains 'essays/'" %}
  {% for page in essays %}
  {% assign folder = page.url | split: '/' | slice: 2, 1 | first %}
  <div class="map-point" data-name="{{ page.title | escape }}" data-popup-teaser="{{ page.popup-teaser | escape }}"
    data-kml-path="{{ site.baseurl }}/assets/kml/{{ folder }}.kml"
    data-card-image="{{ site.baseurl }}{{ page.card-image | escape }}" data-start="{{ page.start | escape }}"
    data-url="{{ site.baseurl }}{{ page.url }}" data-folder="{{ folder | downcase | replace: ' ', '-' }}">
  </div>
  {% endfor %}
</div>


<script>
  document.addEventListener("DOMContentLoaded", function () {
    // Initialize map
    var map = L.map('map').setView([35.0844, -106.6198], 16.5);

    // Add OpenStreetMap tiles
L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; OpenStreetMap &copy; CartoDB'
}).addTo(map);

    // Parse essay data from HTML
    var points = [];
    document.querySelectorAll('.map-point').forEach(function (el) {
      var start = parseInt(el.dataset.start);
      var folder = el.dataset.folder;
      var kmlFile = el.dataset.kmlPath;
      if (!isNaN(start)) {
        points.push({
          start: start,
          name: el.dataset.name,
          teaser: el.dataset.popupTeaser,
          image: el.dataset.cardImage,
          url: el.dataset.url,
          folder: folder,
          kmlFile: kmlFile
        });
      }
    });

    // Create KML overlays and store references
    var kmlLayers = [];

    points.forEach(function (pt) {
      var popupHtml = `
  <div class="popup-card">
    ${pt.image ? `<img src="${pt.image}" class="popup-img">` : ""}
    <div class="popup-text">
      <h3>${pt.name}</h3>
      <p>${pt.teaser}</p>
      <a href="${pt.url}">Read more</a>
    </div>
  </div>
`;
      var kmlFile = pt.kmlFile;
      console.log("Loading name:", pt.image); // Add this line
      console.log("Loading KML:", kmlFile); // Add this line

      var kmlLayer = omnivore.kml(kmlFile).on('ready', function () {
        // Attach year and popup to each child layer
        this.eachLayer(function (layer) {
          layer.ptStart = pt.start;
          layer.on('click', function (e) {
            L.popup({ maxWidth: 500 })
              .setLatLng(e.latlng)
              .setContent(popupHtml)
              .openOn(map);
          });
        });
            updateKmlLayers(parseInt(slider.value));

      });
      kmlLayer.addTo(map);
      kmlLayers.push(kmlLayer);
    });

    // Slider logic
    var slider = document.getElementById('year-slider');
    var yearValue = document.getElementById('year-value');
    yearValue.textContent = slider.value;

    function updateKmlLayers(year) {
      kmlLayers.forEach(function (layer) {
        var show = false;
        layer.eachLayer(function (child) {
          if (child.ptStart <= year) show = true;
        });
        if (show) {
          if (!map.hasLayer(layer)) layer.addTo(map);
        } else {
          if (map.hasLayer(layer)) map.removeLayer(layer);
        }
      });
    }

    slider.addEventListener('input', function () {
      yearValue.textContent = slider.value;
      updateKmlLayers(parseInt(slider.value));
    });

    // Initial KML display
    updateKmlLayers(parseInt(slider.value));
  });
</script>


