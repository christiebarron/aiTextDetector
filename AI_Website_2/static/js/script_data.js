document.addEventListener("DOMContentLoaded", function() {
    const selectParameter1 = document.getElementById('select-essay-set');
    const selectParameter2 = document.getElementById('select-parameter');
    const chartContainer = document.getElementById('chart');

    function fetchData(parameter1, parameter2) {
        fetch('http://127.0.0.1:8001/data')
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

                createBarChart(xValues, humanYValues, aiYValues);
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

        // Calculate average values
        const avgHuman = calculateAverage(humanYValues);
        const avgAI = calculateAverage(aiYValues);

        // Add average lines to the chart
        const avgTraceHuman = {
            x: xValues,
            y: Array(xValues.length).fill(avgHuman),
            type: 'line',
            name: 'Average (Human)',
            marker: {
                color: 'green'
            }
        };

        const avgTraceAI = {
            x: xValues,
            y: Array(xValues.length).fill(avgAI),
            type: 'line',
            name: 'Average (AI)',
            marker: {
                color: 'orange'
            }
        };

        data.push(avgTraceHuman, avgTraceAI);

        const avgLayout = Object.assign({}, layout, { showlegend: true });

        Plotly.newPlot(chartContainer, data, avgLayout);
    }

    function calculateAverage(values) {
        const sum = values.reduce((a, b) => a + b, 0);
        return sum / values.length;
    }

    // Initial data fetch and chart creation
    fetchData(selectParameter1.value, selectParameter2.value);

    // Event listener for dropdown change event
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
});
