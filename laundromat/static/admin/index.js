//detail.html
document.addEventListener("DOMContentLoaded", function () {
    var addressLink = document.querySelector('[data-bs-target="#address"]');
    var orderLink = document.querySelector('[data-bs-target="#order"]');
    var addressSection = document.getElementById("address");
    var orderSection = document.getElementById("order");

    addressLink.addEventListener("click", function () {
        addressSection.style.display = "block";
        orderSection.style.display = "none";

        addressLink.classList.add("active");
        orderLink.classList.remove("active");
    });

    orderLink.addEventListener("click", function () {
        addressSection.style.display = "none";
        orderSection.style.display = "block";

        addressLink.classList.remove("active");
        orderLink.classList.add("active");
    });

    var hash = window.location.hash;
    if (hash === "#address") {
        addressLink.click();
    } else if (hash === "#order") {
        orderLink.click();
    }
});

//edit.html
document.addEventListener("DOMContentLoaded", function () {
    var addressLink = document.querySelector('[data-bs-target="#address"]');
    var userLink = document.querySelector('[data-bs-target="#user"]');
    var addressSection = document.getElementById("address");
    var userSection = document.getElementById("user");

    addressLink.addEventListener("click", function () {
        addressSection.style.display = "block";
        userSection.style.display = "none";

        addressLink.classList.add("active");
        userLink.classList.remove("active");
    });

    userLink.addEventListener("click", function () {
        addressSection.style.display = "none";
        userSection.style.display = "block";

        addressLink.classList.remove("active");
        userLink.classList.add("active");
    });

    var hash = window.location.hash;
    if (hash === "#address") {
        addressLink.click();
    } else if (hash === "#user") {
        orderLink.click();
    }
});