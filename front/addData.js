const friccionbtn = document.getElementById("friccionbtn");
const contFriccion = document.getElementById("contFriccion");
const inclinacionbtn = document.getElementById("inclinacionbtn");
const contInclinacion = document.getElementById("contInclinacion");

friccionbtn.addEventListener("click", () => {
    console.log(contFriccion);
    if (contFriccion.classList.length == 3) {
        console.log("entro al if");
        contFriccion.classList.remove("off");
        return;
    }
    contFriccion.classList.add("off");
});

inclinacionbtn.addEventListener("click", () => {
    console.log(contInclinacion);
    if (contInclinacion.classList.length == 3) {
        console.log("entro al if");
        contInclinacion.classList.remove("off");
        return;
    }
    contInclinacion.classList.add("off");
});
