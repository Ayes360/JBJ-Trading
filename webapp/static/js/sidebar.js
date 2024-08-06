// const hamBurger = document.querySelector(".toggle-btn");

// hamBurger.addEventListener("click", function () {
//   document.querySelector("#sidebar").classList.toggle("expand");
// });
function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}

document.querySelectorAll('.sidebar-link').forEach(function(link) {
  link.addEventListener('click', function() {
      var icon = this.querySelector('.dropdown-icon');
      var isExpanded = this.getAttribute('aria-expanded') === 'true';
      if (isExpanded) {
          icon.classList.remove('fa-chevron-left');
          icon.classList.add('fa-chevron-down');
      } else {
          icon.classList.remove('fa-chevron-down');
          icon.classList.add('fa-chevron-left');
      }
  });
})
scripts.js

