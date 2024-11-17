const navbar = document.querySelector("#nav");
const navBtn = document.querySelector("#nav-btn");
const closeBtn = document.querySelector("#close-btn");
const sidebar = document.querySelector("#sidebar");



window.addEventListener("scroll", function() {
    if (this.window.scrollY > 80) {
        navbar.classList.add("navbar-fixed");
    } else {
        navbar.classList.remove("navbar-fixed");
    }
});

navBtn.addEventListener("click", function() {
    sidebar.classList.add("show-sidebar")
});

closeBtn.addEventListener("click",function(){
    sidebar.classList.remove("show-sidebar")
})

