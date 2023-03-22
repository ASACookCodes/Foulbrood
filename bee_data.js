//Heatmap data stored as an array of google.maps.LatLng objects.
var heatmapData;

function init()
{
	heatmapData=[];
}

//Loads the Google map
function loadMap()
{
	//Center the map somewhere over Sheffield which is vaguely in the middle of the UK
	var uk = new google.maps.LatLng(53.3811, -1.4701);
	
	//Create a map and position it in the container
	map = new google.maps.Map(document.getElementById('map'), {
	  center: uk,
	  zoom: 6,
	  mapTypeId: 'satellite'
	});

	//Layer the heatmap over the satellite map.
	var heatmap = new google.maps.visualization.HeatmapLayer({
	  data: heatmapData
	});
	heatmap.setMap(map);

}

//Takes two floating point latitude and longitude values
//Positions a heat-dot on the heatmap.
function createPoint(lat,lng)
{
	heatmapData.push(new google.maps.LatLng(lat,lng));
};



