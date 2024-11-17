const navbar = document.querySelector("#nav");

window.addEventListener("scroll", function() {
    if (this.window.scrollY > 80) {
        navbar.classList.add("navbar-fixed");
    } else {
        navbar.classList.remove("navbar-fixed");
    }
});