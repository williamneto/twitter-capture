$(function () {
    /* ChartJS
     * -------
     * Here we will create a few charts using ChartJS
     */

    var areaChartOptions = {
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
                        display: true
                    }
                }],
        },
        legend: {
            display: true,
            position: 'bottom',
            labels: {
              fontColor: "#000080",
            }
          },
    }

    var tags = $("#tags").val()
    $.ajax({
        url: ".",
        data: {"cmd": "get_timeline_graph", "tag": tags},
        success: function(graph_data) {
            if (tags.split(",").length == 1) {
                var ctx = $('#lineChart').get(0).getContext('2d')
                
                var areaChartData = {
                    labels  : graph_data["labels"],
                    datasets: [
                        {
                        label               : tags[0],
                        backgroundColor: "#3b8bba",
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