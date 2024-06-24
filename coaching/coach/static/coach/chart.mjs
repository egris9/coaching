import ApexCharts from 'https://cdn.jsdelivr.net/npm/apexcharts@3.49.1/+esm'

var options_simple_lines = {
    series: [{
      name: "participent",
      data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
  }],
    chart: {
    height: 370,
    width:600,
    type: 'line',
    zoom: {
      enabled: false
    }
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    curve: 'straight'
  },
  title: {
    text: 'participents count each month',
    align: 'left',
           
  },
  
  grid: {
    row: {
      colors: ['#bbf7d0', 'transparent'], // takes an array which will be repeated on columns
      opacity: 0.5
    },
  },
  xaxis: {
    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
  }
  };



  var options_mult_bars = {
    series: [{
    name: 'session2',
    data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
  },{
    name: 'total',
    data: [116, 116, 116, 116, 116, 116, 116, 116,116]
  }, {
    name: 'session1',
    data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
  },],
    chart: {
    type: 'bar',
    height: 400,
    width:1150,
  },
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: '55%',
      endingShape: 'rounded'
    },
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    show: true,
    width: 2,
    colors: ['transparent']
  },
  xaxis: {
    categories: ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
  },
  yaxis: {
    title: {
      text: 'revenues'
    }
  },
  fill: {
    opacity: 1
  },
  tooltip: {
    y: {
      formatter: function (val) {
        return "$ " + val + " thousands"
      }
    }
  }
  };

  var pie_options = {
    series: [44, 55, 13, 43, 22],
    chart: {
    height: 500,
    width: 500,
    type: 'pie',
  },
  labels: ['session1', 'session2', 'session3', 'session4', 'session5'],
  responsive: [{
    breakpoint: 480,
    options: {
      chart: {
        height: 500,
        width: 500
      },
      legend: {
        position: 'bottom'
      }
    }
  }]
  };



  
  var chart3 = new ApexCharts(document.querySelector("#chart3"), pie_options);
  chart3.render();

  var chart2 = new ApexCharts(document.querySelector("#chart2"), options_mult_bars);
  chart2.render();

  var chart = new ApexCharts(document.querySelector("#chart"), options_simple_lines);
  chart.render();


