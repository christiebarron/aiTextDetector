// var width = 750,
//     height = 400;

// List of words (teacher 4)
var myWords = ['paragraph','parents', 'building', 'would', 'dirigibles', 'author', 'computer', 'obstacle', 'state', 'builders', 'tether', 'life', 'time', 'happy','home', 'empire', 'friends', 'mood']

// List of words (teacher 3)
var myWords3 = ['people', 'help', 'building', 'money', 'dirigibles', 'internet', 'around', 'math', 'money', 'college', 'school', 'country', 'another', 'reason', 'learn', 'faced', 'world']

// List of words (teacher 2)
var myWords2 = ['building', 'offensive', 'material', 'memoir', 'empire', 'parents', 'state', 'author', 'problems', 'mood', 'everyone', 'would', 'family', 'always', 'life', 'think', 'faced', 'going', 'shelf']

// List of words (teacher 1)
var myWords1 = ['computer', 'obesity', 'sexual', 'people', 'school' , 'reasons', 'positive', 'websites', 'world', 'coordination', 'building', 'empire', 'state', 'passionate', 'obstacle', 'memoir', 'internet', 'created', 'mood', 'time']

// set the dimensions and margins of the graph
var margin = {top: 10, right: 10, bottom: 10, left: 10}
    width = 850 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

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
  .padding(10)
  .fontSize(60)
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