var chart = AmCharts.makeChart("chartdiv", {
    "theme": "dark",
    "type": "serial",
	"startDuration": 2,
    "dataProvider": [{
        "country": "Gurgaon",
        "visits": 14,
        "color": "#FF0F00"
    }, {
        "country": "Hyderabad",
        "visits": 45,
        "color": "#FF6600"
    }, {
        "country": "Pune",
        "visits": 32,
        "color": "#B0DE09"
    }, {
        "country": "Gandhinagar",
        "visits": 85,
        "color": "#04D215"
    }, {
        "country": "Bhopal",
        "visits": 21,
        "color": "#0D8ECF"
    }, {
        "country": "Jaipur",
        "visits": 66,
        "color": "#0D52D1"
    }, {
        "country": "Chennai",
        "visits": 58,
        "color": "#2A0CD0"
    }, {
        "country": "Cochin",
        "visits": 44,
        "color": "#8A0CCF"
    }, {
        "country": "Kolkata",
        "visits": 41,
        "color": "#CD0D74"
    }, {
        "country": "Mumbai",
        "visits": 95,
        "color": "#754DEB"
    }, {
        "country": "Silvassa",
        "visits": 38,
        "color": "#DDDDDD"
    }, {
        "country": "Delhi",
        "visits": 76,
        "color": "#999999"
    }, {
        "country": "Ahemdabad",
        "visits": 80,
        "color": "#000000"
    }],
    "valueAxes": [{
        "position": "left",
        "title": "DONATIONS IN THOUSAND RUPEES"
    }],
    "graphs": [{
        "balloonText": "[[category]]: <b>[[value]]</b>",
        "fillColorsField": "color",
        "fillAlphas": 1,
        "lineAlpha": 0.1,
        "type": "column",
        "valueField": "visits"
    }],
    "depth3D": 20,
	"angle": 30,
    "chartCursor": {
        "categoryBalloonEnabled": false,
        "cursorAlpha": 0,
        "zoomable": false
    },
    "categoryField": "country",
    "categoryAxis": {
        "gridPosition": "start",
        "labelRotation": 90
    },
    "export": {
    	"enabled": true
     }

});