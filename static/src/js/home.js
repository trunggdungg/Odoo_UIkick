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
        // form.querySelectorAll("input[type=checkbox], input[type=radio]").forEach(function (input) {
        //     input.addEventListener("change", function () {
        //         form.submit();
        //     });
        // });
        var sortSelect = document.getElementById("uikick-sort-select");
        if (sortSelect) {
            sortSelect.addEventListener("change", function () {
                form.submit();
            });
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
        // Event delegation on document: some Odoo frontend/editor scripts can
        // rebuild the button node after our own DOMContentLoaded handler runs,
        // which would silently drop a listener bound directly to that node.
        document.addEventListener("click", function (ev) {
            var toggle = ev.target.closest("#uikick-filter-toggle");
            if (!toggle) return;
            console.log("Bắt được click vào nút Filter by", toggle);
            var sidebar = document.getElementById("uikick-filter-form");
            if (!sidebar) {
                console.log("Không tìm thấy #uikick-filter-form");
                return;
            }
            var isOpen = sidebar.classList.toggle("is-open");
            toggle.classList.toggle("is-open", isOpen);
            console.log("sidebar class sau khi toggle:", sidebar.className);
        }, true);
    }

    document.getElementById("uikick-filter-toggle").addEventListener("click", function () {
        console.log("xin chào");
    });

      function onReady(fn) {
        // This bundle can load lazily, after DOMContentLoaded has already
        // fired — listening for that event at that point would never call
        // fn again. Run immediately if the DOM is already parsed.
        if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", fn);
        } else {
            fn();
        }
    }

    onReady(function () {
        if (!document.querySelector(".uikick-grid")) return; // chỉ chạy trên trang home
        initCardVideos();
        initFilterForm();
        preserveFiltersOnCategoryLinks();
        initMobileFilterToggle();
    });
})();
