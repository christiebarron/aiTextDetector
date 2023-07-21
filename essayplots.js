console.log(jsonData);

let trace = {
    x: jsonData.map(item => item.teacher_name), 
    y: jsonData.map(item => item.total_word_count), 
    type: 'bar'
}

let graphData = [trace]

let layout = {
  title: "<b>Total word count</b>",
  showlegend: false,
  xaxis: { tickangle: 45, zeroline: true },
  yaxis: { gridwidth: 1, zeroline: true },
  height: 400,
  width: 500,

};

Plotly.newPlot("bar", graphData, layout)



let donuttrace = {
  x: jsonData.map(item => item.teacher_name), 
  y: jsonData.map(item => item.stop_word_count), 
  type: 'bar'
}

let donutData = [donuttrace]

let donutLayout = {
  title: "<b>Stop word count</b>",
  showlegend: false,
  xaxis: { tickangle: 45, zeroline: true },
  yaxis: { gridwidth: 1, zeroline: true },
  height: 400,
  width: 500,

};

Plotly.newPlot("plot", donutData, donutLayout)

var data = [{
  values: jsonData.map(item => item.unique_word_count),
  labels: jsonData.map(item => item.teacher_name),
  type: 'pie'
}];

var Layout = {
  title: "<b>Unique word count</b>",
  height: 400,
  width: 500,
  margin: {"t": 0, "b": 0, "l": 0, "r": 0},
  showlegend: true
};

Plotly.newPlot('pie', data, Layout);

var trace3 = [{
  values: jsonData.map(item => item.avg_sentence_length),
  labels: jsonData.map(item => item.teacher_name),
  type: 'pie'
}];

var trace4 = [{
  values: jsonData.map(item => item.rare_word_count),
  labels: jsonData.map(item => item.teacher_name),
  type: 'pie'
}];

var data = [trace,donuttrace];

var layouts = {
  grid: {rows: 1, columns: 2, pattern: 'independent'},
};

Plotly.newPlot('myDiv', data, layouts);

var trace1 = {
  x: jsonData.map(item => item.avg_sentence_length),
  type: 'box',
  name: 'Set 1'
};

var trace2 = {
  x: jsonData.map(item => item.avg_verbs_per_sentence),
  type: 'box',
  name: 'Set 2'
};

var data = [trace1, trace2];

var layoutb = {
  title: 'Box Plot for Avg sentence length vs verbs '
};

Plotly.newPlot('NewDiv', data, layoutb);


var traceh = {
    x: jsonData.map(item => item.avg_nouns_per_sentence),
    type: 'histogram',
  };
var datah = [traceh];

var layoutb = {
  bargap: 0.05, 
  bargroupgap: 0.2, 
  title: 'Histogram for avg nouns per sentence '
};
Plotly.newPlot('NewDiv2', datah,layoutb);


var trace10 = {
  x: jsonData.map(item => item.rare_word_count),
  type: 'histogram',
};

var trace20 = {
  x: jsonData.map(item => item.unique_word_count),
  xaxis: 'x2',
  yaxis: 'y2',
  type: 'histogram',
};

var trace30 = {
  x: jsonData.map(item => item.avg_sentence_length),
  xaxis: 'x3',
  yaxis: 'y3',
  type: 'histogram',
};

var trace40 = {
  x: jsonData.map(item => item.avg_nouns_per_sentence),
  xaxis: 'x4',
  yaxis: 'y4',
  type: 'histogram',
};

var datas = [trace10, trace20, trace30, trace40];

var layouts = {
  grid: {rows: 2, columns: 2, pattern: 'independent'},
  title: 'Histograms for rare_word vs unique_word vs avg_sentence_length vs avg_nouns_per_sentence'
};

Plotly.newPlot('NewDiv3', datas, layouts);