<script>
function showFields() {


    let employment = document.querySelector('input[name="employment_type"]:checked').value;

    if (employment === "Salaried") {
        document.getElementById("salariedFields").style.display = "block";
        document.getElementById("selfFields").style.display = "none";
    } else {
        document.getElementById("salariedFields").style.display = "none";
        document.getElementById("selfFields").style.display = "block";
    }

}

</script>