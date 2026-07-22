/** UIKick - Home page interactions (thay cho useState/hover logic của React ProjectCard) */
(function () {
    "use strict";

    function initCardVideos() {
        document.querySelectorAll(".uikick-card").forEach(function (card) {
            var video = card.querySelector(".uikick-card-video");
            if (!video) return;

            card.addEventListener("mouseenter", function () {
                video.currentTime = 0;
                video.play().then(function () {
                    card.classList.add("is-playing");
                }).catch(function () {
                    /* autoplay blocked, ignore */
                });
            });

            card.addEventListener("mouseleave", function () {
                card.classList.remove("is-playing");
                video.pause();
                video.currentTime = 0;
            });
        });
    }

    function initFilterForm() {
        var form = document.getElementById("uikick-filter-form");
        if (!form) return;
        form.querySelectorAll("input[type=checkbox], input[type=radio]").forEach(function (input) {
            input.addEventListener("change", function () { form.submit(); });
        });
        var sortSelect = document.getElementById("uikick-sort-select");
        if (sortSelect) {
            sortSelect.addEventListener("change", function () { form.submit(); });
        }
    }

    function preserveFiltersOnCategoryLinks() {
        var query = window.location.search;
        if (!query) return;
        document.querySelectorAll(".uikick-cat-item").forEach(function (link) {
            link.href = link.getAttribute("href") + query;
        });
    }

    function initMobileFilterToggle() {
        var toggle = document.getElementById("uikick-filter-toggle");
        var sidebar = document.getElementById("uikick-filter-form");
        if (!toggle || !sidebar) return;
        toggle.addEventListener("click", function () {
            var isOpen = sidebar.classList.toggle("is-open");
            toggle.classList.toggle("is-open", isOpen);
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        if (!document.querySelector(".uikick-grid")) return; // chỉ chạy trên trang home
        initCardVideos();
        initFilterForm();
        preserveFiltersOnCategoryLinks();
        initMobileFilterToggle();
    });
})();
