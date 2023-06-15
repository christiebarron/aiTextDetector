
    document.addEventListener("DOMContentLoaded", function() {
        const selectParameter1 = document.getElementById('select-essay-set');
        const selectParameter2 = document.getElementById('select-parameter');
        const selectChartType = document.getElementById('select-chart-type');
        const chartContainer = document.getElementById('chart');
    
        function fetchData(parameter1, parameter2) {
            fetch('/data')
                .then(response => response.json())
                .then(raw_data => {
                    const data = raw_data.filter(item => item.essay_set == parameter1);
    
                    const xValues = data.map(item => item.essay_id_sql);
                    const humanYValues = [];
                    const aiYValues = [];
    
                    for (let i = 0; i < data.length; i++) {
                        const essayId = data[i].essay_id_sql;
                        const isHuman = (essayId - 1) % 14 < 7;
    
                        if (isHuman) {
                            humanYValues.push(data[i][parameter2]);
                            aiYValues.push(null);
                        } else {
                            humanYValues.push(null);
                            aiYValues.push(data[i][parameter2]);
                        }
                    }
    
                    if (selectChartType.value === 'bar') {
                        createBarChart(xValues, humanYValues, aiYValues);
                    } else if (selectChartType.value === 'line') {
                        createLineChart(xValues, humanYValues, aiYValues);
                    }
                })
                .catch(error => console.log(error));
        }
    
        function createBarChart(xValues, humanYValues, aiYValues) {
            const trace1 = {
                x: xValues,
                y: humanYValues,
                type: 'bar',
                name: 'Human',
                marker: {
                    color: 'blue'
                }
            };
    
            const trace2 = {
                x: xValues,
                y: aiYValues,
                type: 'bar',
                name: 'AI',
                marker: {
                    color: 'red'
                }
            };
    
            const data = [trace1, trace2];
    
            const layout = {
                title: 'Bar Chart',
                xaxis: {
                    title: 'Essay ID'
                },
                yaxis: {
                    title: selectParameter2.value
                }
            };
    
            Plotly.newPlot(chartContainer, data, layout);
        }
    
        function createLineChart(xValues, humanYValues, aiYValues) {
            const trace1 = {
                x: xValues,
                y: humanYValues,
                mode: 'lines',
                name: 'Human',
                line: {
                    color: 'blue'
                }
            };
    
            const trace2 = {
                x: xValues,
                y: aiYValues,
                mode: 'lines',
                name: 'AI',
                line: {
                    color: 'red'
                }
            };
    
            const data = [trace1, trace2];
    
            const layout = {
                title: 'Line Chart',
                xaxis: {
                    title: 'Essay ID'
                },
                yaxis: {
                    title: selectParameter2.value
                }
            };
    
            Plotly.newPlot(chartContainer, data, layout);
        }
    
        // Initial data fetch and chart creation
        fetchData(selectParameter1.value, selectParameter2.value);
    
        // Event listeners for dropdown change events
        selectParameter1.addEventListener('change', function() {
            let selectedParameter1 = this.value;
            let selectedParameter2 = selectParameter2.value;
            fetchData(selectedParameter1, selectedParameter2);
        });
    
        selectParameter2.addEventListener('change', function() {
            let selectedParameter1 = selectParameter1.value;
            let selectedParameter2 = this.value;
            fetchData(selectedParameter1, selectedParameter2);
        });
    
        selectChartType.addEventListener('change', function() {
            let selectedParameter1 = selectParameter1.value;
            let selectedParameter2 = selectParameter2.value;
            fetchData(selectedParameter1, selectedParameter2);
        });
    });

// Glossary terms and definitions
const glossaryData = [
    {
      term: 'Essay ID',
      definition: 'The unique identifier for each essay in the database from a total of 112 essays.'
    },
    {
      term: 'Essay Set',
      definition: 'The category or prompt to which the essay belongs (From a total of 8 Prompts).'
    },
    {
      term: 'Rare Word Count',
      definition: 'The count of uncommon or infrequently used words in the essay.'
    },
    {
      term: 'Stop Word Count',
      definition: 'The count of common words that are usually excluded from text analysis, such as articles, prepositions, and conjunctions.'
    },
    {
      term: 'Avg Word Length',
      definition: 'The average length of words in the essay, calculated by dividing the total number of characters by the total number of words.'
    },
    {
      term: 'Avg Sentence Length',
      definition: 'The average length of sentences in the essay, calculated by dividing the total number of words by the total number of sentences.'
    },
    {
      term: 'Sentiment Polarity',
      definition: 'The measure of the sentiment or emotion expressed in the essay, ranging from negative to positive.'
    },
    {
      term: 'Flesch Kincaid Grade Level',
      definition: 'The readability score of the essay, indicating the grade level required to understand the text.'
    },
    {
      term: 'TTR',
      definition: 'Type-Token Ratio, which is a measure of lexical richness in the essay, calculated by dividing the number of unique words by the total number of words.'
    },
    {
      term: 'Smog Index',
      definition: 'The SMOG (Simple Measure of Gobbledygook) index, which estimates the years of education required to understand the essay based on the number of polysyllabic words used.'
    }
  ];
  
  
  // Function to generate glossary list
  function generateGlossaryList() {
    const glossaryList = document.getElementById('glossary-list');
    glossaryData.forEach(item => {
      const listItem = document.createElement('li');
      listItem.innerHTML = `<strong>${item.term}</strong>: ${item.definition}`;
      glossaryList.appendChild(listItem);
    });
  }
  
  // Show the glossary modal
  function showGlossaryModal() {
    const glossaryModal = document.getElementById('glossary-modal');
    glossaryModal.style.display = 'block';
  }
  
  // Hide the glossary modal
  function hideGlossaryModal() {
    const glossaryModal = document.getElementById('glossary-modal');
    glossaryModal.style.display = 'none';
  }
  
  // Add event listener for glossary button click
  const glossaryButton = document.getElementById('glossary-button');
  glossaryButton.addEventListener('click', showGlossaryModal);
  
  // Add event listener for close button click
  const closeButton = document.getElementsByClassName('close')[0];
  closeButton.addEventListener('click', hideGlossaryModal);
  
  // Generate the glossary list on page load
  document.addEventListener('DOMContentLoaded', generateGlossaryList);
