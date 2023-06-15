// var width = 750,
//     height = 400;

// List of words
var myWords = ['paragraph','parents', 'building', 'would', 'dirigibles', 'author', 'computer', 'obstacle', 'state', 'builders', 'tether', 'life', 'time', 'happy','home', 'empire', 'friends', 'mood']
  
// set the dimensions and margins of the graph
var margin = {top: 10, right: 10, bottom: 10, left: 10}
    width = 1000 - margin.left - margin.right,
    height = 1000 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#wordcloud").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// Constructs a new cloud layout instance. It run an algorithm to find the position of words that suits your requirements
var layout = d3.layout.cloud()
  .size([width, height])
  .words(myWords.map(function(d) {return {text: d}; }))
  .padding(5)
  .fontSize(40)
  .on("end", draw);
layout.start();
//define a color scale
var wordColor="#ff0000";

// This function takes the output of 'layout' above and draw the words
// Better not to touch it. To change parameters, play with the 'layout' variable above
function draw(words) {
  svg
    .append("g")
      .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
      .selectAll("text")
        .data(words)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("fill",wordColor)
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
}