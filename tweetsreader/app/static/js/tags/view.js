$(function () {
    /* ChartJS
     * -------
     * Here we will create a few charts using ChartJS
     */

    var areaChartOptions = {
        showScale               : true,
        //Boolean - Whether grid lines are shown across the chart
        scaleShowGridLines      : true,
        //String - Colour of the grid lines
        scaleGridLineColor      : 'rgba(0,0,0,.05)',
        //Number - Width of the grid lines
        scaleGridLineWidth      : 1,
        //Boolean - Whether to show horizontal lines (except X axis)
        scaleShowHorizontalLines: true,
        //Boolean - Whether to show vertical lines (except Y axis)
        scaleShowVerticalLines  : true,
        //Boolean - Whether the line is curved between points
        bezierCurve             : true,
        //Number - Tension of the bezier curve between points
        bezierCurveTension      : 0.3,
        //Boolean - Whether to show a dot for each point
        pointDot                : true,
        //Number - Radius of each point dot in pixels
        pointDotRadius          : 1,
        //Number - Pixel width of point dot stroke
        pointDotStrokeWidth     : 1,
        //Number - amount extra to add to the radius to cater for hit detection outside the drawn point
        pointHitDetectionRadius : 1,
        //Boolean - Whether to show a stroke for datasets
        datasetStroke           : true,
        //Number - Pixel width of dataset stroke
        datasetStrokeWidth      : 1,
        //Boolean - Whether to fill the dataset with a color
        datasetFill             : true,
        //String - A legend template
        legendTemplate          : '<ul class="<%=name.toLowerCase()%>-legend"><% for (var i=0; i<datasets.length; i++){%><li><span style="background-color:<%=datasets[i].lineColor%>"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>',
        //Boolean - whether to maintain the starting aspect ratio or not when responsive, if set to false, will take up entire container
        maintainAspectRatio     : true,
        //Boolean - whether to make the chart responsive to window resizing
        responsive              : true,
        scales: {
            xAxes: [{
                    type: "time",
                    time: {
                        format: "HH:mm",
                        unit: 'hour',
                        unitStepSize: 2,
                        displayFormats: {
                            'minute': 'HH:mm', 
                            'hour': 'HH:mm'
                        },
                        tooltipFormat: 'HH:mm'
                    },
                    gridLines: {
                        display: false
                    }
                }],
        }
    }

    var tags = $("#tags").val()
    $.ajax({
        url: ".",
        data: {"cmd": "get_timeline_graph", "tags": tags},
        success: function(graph_data) {
            if (tags.split(",").length == 1) {
                var ctx = $('#lineChart').get(0).getContext('2d')
                
                var areaChartData = {
                    labels  : graph_data["labels"],
                    datasets: [
                        {
                        label               : 'Digital Goods',
                        fillColor           : 'rgba(60,141,188,0.9)',
                        strokeColor         : 'rgba(60,141,188,0.8)',
                        pointColor          : '#3b8bba',
                        pointStrokeColor    : 'rgba(60,141,188,1)',
                        pointHighlightFill  : '#fff',
                        pointHighlightStroke: 'rgba(60,141,188,1)',
                        data                : graph_data["values"]
                        }
                    ]
                }

                var lineChartCanvas          = $('#lineChart').get(0).getContext('2d')
                var lineChart                = new Chart(lineChartCanvas)
                var lineChartOptions         = areaChartOptions
                lineChartOptions.datasetFill = false
                lineChart.Line(areaChartData, lineChartOptions)               
                
            } else {
                var ctx = $('#lineChart').get(0).getContext('2d')
                
                var areaChartData = {
                    labels  : graph_data["labels"],
                    datasets: [
                        {
                        label               : 'Digital Goods',
                        fillColor           : 'rgba(60,141,188,0.9)',
                        strokeColor         : 'rgba(60,141,188,0.8)',
                        pointColor          : '#3b8bba',
                        pointStrokeColor    : 'rgba(60,141,188,1)',
                        pointHighlightFill  : '#fff',
                        pointHighlightStroke: 'rgba(60,141,188,1)',
                        data                : graph_data["values"]
                        }
                    ]
                }

                var lineChartCanvas          = $('#lineChart').get(0).getContext('2d')
                var lineChart                = new Chart(lineChartCanvas)
                var lineChartOptions         = areaChartOptions
                lineChartOptions.datasetFill = false
                lineChart.Line(areaChartData, lineChartOptions)               
                
            }
        }
    })
    
    //-------------
    //- LINE CHART -
    //--------------


  })