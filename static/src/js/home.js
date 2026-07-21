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

    function initSort() {
        var sortSelect = document.querySelector(".uikick-sort select");
        if (!sortSelect) return;
        sortSelect.addEventListener("change", function () {
            var url = new URL(window.location.href);
            url.searchParams.set("sort", sortSelect.value);
            window.location.href = url.toString();
        });
    }

    function initFilterCounters() {
        // Ví dụ điểm nối để sau này gọi API lọc project theo checkbox/radio
        // mà không cần reload toàn trang (fetch + render lại .uikick-grid).
        document.querySelectorAll(".uikick-sidebar input[type=checkbox], .uikick-sidebar input[type=radio]")
            .forEach(function (input) {
                input.addEventListener("change", function () {
                    // TODO: gọi controller /uikick/filter (JSON-RPC) và render lại grid
                });
            });
    }

    document.addEventListener("DOMContentLoaded", function () {
        if (!document.querySelector(".uikick-grid")) return; // chỉ chạy trên trang home
        initCardVideos();
        initSort();
        initFilterCounters();
    });
})();
