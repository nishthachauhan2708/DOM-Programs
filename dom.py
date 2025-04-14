<textarea id= "textArea" maxlength="100"></textarea>
<p>Characters: <span id="charCount">0</span>/100</p>
<script>
const textArea = document.getElementById("textArea");
const charCount = document.getElementById("charCount");
textArea.addEventListener("input", ()=>{
let count = textArea.value.length;
charCount.textContent = count;
charCount.style.color = count>=100?"red":"black"
});
</script>
<button id="darkModeToggle">Toggle Dark Mode</button>
<script>
const button = document.getElementById("darkModeToggle");
const body = document.body;
button.addEventListener("click", () => {
body.classList.toggle("dark-mode");
localStorage.setItem("darkMode", body.classList.contains("dark-mode"));
});
if (localStorage.getItem("darkMode") === "true") {
body.classList.add("dark-mode");
}
</script>
<style>
.dark-mode {
background-color: black;
color: white;
}
</style>