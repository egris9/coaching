import ApexCharts from 'https://cdn.jsdelivr.net/npm/apexcharts@3.49.1/+esm'
fetch('http://127.0.0.1:8000/stats/participent_by_coach').then(async function (v) {
  const res=await v.json()
  let month=[]
  let participent=[]
  res.participent_by_month.forEach((el)=>{
    month.push(el.month)
    participent.push(el.count)
  })
  var options_simple_lines = {
    series: [{
      name: "participent",
      data: participent
  }],

    chart: {
    foreColor: '#a7f3d0',
    height: 370,
    width:1150,
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
    categories: month,
  }
  };
  var chart = new ApexCharts(document.querySelector("#chart"), options_simple_lines);
  chart.render();
})



fetch('http://127.0.0.1:8000/stats/revenue_by_session').then(async function (v) {
  const res=await v.json()
  let month=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  



  const data=res.revenue_by_session.map((el)=>{
  let list=[]
  
    for(const m of month) {

      if (m===el.month) {
         list.push( el.total )

         
         continue
      }
      list.push(null)


    }
    const serie={
      name:el.name,
      data:list
    }
   return serie
  
  })  
  
  const formatedTotalRevnueEachMonth = res.total_each_month.reduce((store, current) =>{
  console.log(store, current)
    store.months.push(current.month)
    store.total.push(current.total_price)
    return store
}, {
    months: [],
    total: []
})

let TotalRevnueEachMonth = []

for(const m of month) {
  
    if (formatedTotalRevnueEachMonth.months.includes(m)) {
      const index=formatedTotalRevnueEachMonth.months.indexOf(m)
        TotalRevnueEachMonth.push( formatedTotalRevnueEachMonth.total[index] )
       continue
    }
    TotalRevnueEachMonth.push(null)
  }

  const TotalRevnueEachMonthSerie = {
    data:TotalRevnueEachMonth,
    name:'total',
  }
  
    data.push(TotalRevnueEachMonthSerie)

  var options_mult_bars = {
    
      series:data,

    chart: {
    foreColor: '#a7f3d0',
    type: 'bar',
    height: 400,
    width:1150,
  },
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: '80%',
      endingShape: 'rounded'
    },
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    show: true,
    width: 1,
    colors: ['transparent']
  },
  xaxis: {
    categories: month,
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
var chart2 = new ApexCharts(document.querySelector("#chart2"), options_mult_bars);
  chart2.render();
  
})

