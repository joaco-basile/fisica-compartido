const calcularBtn = document.getElementById("calcularBtn");
const contResponse = document.getElementById("contResponse");

calcularBtn.addEventListener("click", (e) => {
    const masa = document.getElementsByName("masa")[0].value;
    const fuerza = document.getElementsByName("fuerza")[0].value;
    const inclinacion = document.getElementsByName("inclinacion")[0].value;
    const coeficienteDinamico =
        document.getElementsByName("coeficiente1")[0].value;
    const coeficienteEstatico =
        document.getElementsByName("coeficiente2")[0].value;

    let url = `http://localhost:5000/calcular?masa=${masa}&fuerza=${fuerza}&ud=${coeficienteDinamico}&ue=${coeficienteEstatico}&inclinacion=${inclinacion}`;

    console.log(url);

    p = document.createElement("p");

    fetch(url)
        .then((res) => res.json())
        .then((json) => {
            p.textContent = json.message;
            contResponse.appendChild(p);
        })
        .catch((err) => console.log("paso algo:", err));
});
