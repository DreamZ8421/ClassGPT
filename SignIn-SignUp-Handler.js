// JavaScript code to toggle between Sign In and Sign Up forms
document.addEventListener("DOMContentLoaded", function() {
const tabs = document.querySelectorAll(".nav-link");
const forms = document.querySelectorAll(".card-body > div");

tabs.forEach(function(tab) {
    tab.addEventListener("click", function(e) {
    e.preventDefault();
    const target = this.getAttribute("href").substring(1);
    tabs.forEach(function(t) {
        t.classList.remove("active");
    });
    this.classList.add("active");
    forms.forEach(function(form) {
        if (form.getAttribute("id") === target) {
        form.style.display = "block";
        } else {
        form.style.display = "none";
        }
    });
    });
});
});