var lineplot_data = [
    {
        x: ['2021-10-06', '2021-10-16', '2021-10-21', '2021-11-04', '2021-11-14', '2021-11-26',
         '2021-12-03', '2021-12-15', '2021-12-25' ],
        y: [10, 5, 10, 4, 5, 6, 6, 7, 9], 
        name: "Gráfico de linea",
    }
];

function create_layout(title, xlabel, ylabel){
    let layout = {
        title: {
            text: title,
            font: {
                family: 'Courier New, monospace',
                size: 24
            },
            xref: 'paper',
            x: 0.05,
        },
        xaxis: {
            title: {
                text: xlabel,
                font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                }
            },
        },
        yaxis: {
            title: {
                text: ylabel,
                font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                }
            }
        }
    };
    return layout;
}

function lineplot() {
    return lineplot_data;
}

let pie_data = [{
    values: [20, 12, 10, 9, 11],
    labels: ['Chilena', 'India', 'Japonesa', 'Italiana', 'China'],
    type: 'pie'
  }];

function pieplot(){
    return pie_data;
}

let bar_data_morning = {
    x: ['Octubre', 'Noviembre', 'Diciembre'],
    y: [8, 3, 6],
    name: 'Eventos que inician por la mañana',
    type: "bar"
}

let bar_data_noon = {
    x: ['Octubre', 'Noviembre', 'Diciembre'],
    y: [7, 6, 9],
    name: 'Eventos que inician al mediodia',
    type: "bar"
}

let bar_data_afternoon = {
    x: ['Octubre', 'Noviembre', 'Diciembre'],
    y: [10, 6, 7],
    name: 'Eventos que inician en la tarde',
    type: "bar"
}

function barplot(){
    return [bar_data_morning, bar_data_noon, bar_data_afternoon];
}
