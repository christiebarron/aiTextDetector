////1. read in data


//READ AND PROCESS THE STUDENT METADATA
let studentData = "../project3.json";
console.log(studentData);


//STEP 1

function init() {
    //get data
    d3.json(studentData).then(function (data) {
      //console.log(data); //works

      let studentArray = []
  
      //extract names

      for (let index = 0; index < data.length; index++){
        let studentName = data[index]["student_name"];
        studentArray.push(studentName)
        console.log(studentName)
      }

      console.log(studentArray)
  
      //create drop-down menu
      let namesSelect = d3.select("#selDataset");
  
      //for loop
      for (let index = 0; index < sampleNames.length; index++) {
        const element = studentArray[index];
  
        // Append the text id, add a property to it.
        namesSelect.append("option").text(element).property("value", element);
      }
      buildCharts(sampleNames[0]);
    });
  }
  
  init ()
  
  //step 2: build charts
  function buildCharts(id) {
    console.log(id);
  
    //access data
    d3.json(studentData).then(function (data) {
  
      //extract metadata
      let metadata = ;
      //extract samples
      let samples = data.samples;
  
    //METADATA PANEL
      //step 2: create metadata panel
      let metadataPanel = d3.select("#sample-metadata")
  
      //overwrite the html of metadataPanel with nothing
      metadataPanel.html("")
      
      //select relevant id sample. use arrow function to loop through all ids and select the id that matches.
      let sampleMetadata = metadata.filter(o => o.id == id)[0]
  
      console.log(sampleMetadata) //works!
  
      //extract key-value pair for each key and value pair in the sample metadata and append to the panel
      for (key in sampleMetadata) {
        
        metadataPanel.append("h6").text(`${key} : ${sampleMetadata[key]}`)
        console.log(key) //key
        console.log(sampleMetadata[key]) //value
      }
  
    // BAR CHART CODE
      //select relevant object for bar chart
      let horizontalBarChart = d3.select("#bar")
  
      //select relevant id data. use arrow function to loop through all ids and select first id that matches
      let idBarData = samples.filter(object => object.id == id)[0]
  
      //acquire relevant data for bar graph
      let otu_labels = idBarData.otu_labels;
      let otu_ids = idBarData.otu_ids;
      let sample_values = idBarData.sample_values;
      let otuIdText = otu_ids.slice(0, 10).reverse().map(object => `OTU ${object}`)
  
      console.log(`otu_labels: ${otu_labels}`)
      console.log(`otu_ids: ${otu_ids}`)
      console.log(`sample_values : ${sample_values}`)
      console.log(otuIdText)
  
      let barData = [
            {
              x: sample_values.slice(0,10).reverse(),
              y:  otuIdText.slice(0, 10).reverse(),
              text: otu_labels.slice(0,10).reverse(),
              type: 'bar',
              orientation: 'h'
            }
          ]
  
        let barLayout = {
          title: `${id}'s Highest Ten OTU Values`,
              }
            
        Plotly.newPlot("bar", barData, barLayout)
  
    //BUBBLE CHART CODE
      var bubbleData = [{
        x: otu_ids,
        y: sample_values,
        mode: 'markers',
        marker: {
          color: otu_ids,
          size: sample_values
        }
      }];
          
      var bubbleLayout = {
        title: `${id}'s OTU Sample Values`,
        xaxis: {title: "OTU IDs"},
        height: 600,
        width: 1000
      };
    
    Plotly.newPlot('bubble', bubbleData, bubbleLayout);
  
    });
  }
  
  //loop over and key-value pair.
  
  
  //step 3: option change
  
  function optionChanged(id){
    buildCharts(id)
  }