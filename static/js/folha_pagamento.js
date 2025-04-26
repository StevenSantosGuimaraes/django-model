document.addEventListener("DOMContentLoaded", function () {

    if (document.getElementById("folhaChart")) {
        
        const competencias = JSON.parse(document.getElementById("competencias").textContent);
        const totais = JSON.parse(document.getElementById("totais").textContent);

        const data = [
            {
                x: competencias,
                y: totais,
                type: "bar",
                marker: {
                color: "rgba(75, 192, 192, 0.7)",
                line: {
                    color: "rgba(75, 192, 192, 1)",
                    width: 1,
                },
                },
            },
        ];

        const layout = {
            title: "Total Pago por Competência",
            xaxis: {
                title: "Competência"
            },
            yaxis: {
                title: "Total Pago (R$)",
                rangemode: "tozero"
            },
        };

        Plotly.newPlot("folhaChart", data, layout);
        
    }

});
