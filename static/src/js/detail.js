/** UIKick - Campaign detail page interactions */
(function () {
    "use strict";

    function initTabs() {
        var tabs = document.querySelectorAll(".uikick-tab");
        if (!tabs.length) return;
        tabs.forEach(function (tab) {
            tab.addEventListener("click", function (ev) {
                ev.preventDefault();
                tabs.forEach(function (t) { t.classList.remove("active"); });
                tab.classList.add("active");
                // TODO: nếu tách nội dung mỗi tab thành section riêng,
                // ẩn/hiện tương ứng ở đây bằng data-tab attribute.
            });
        });
    }

    function initRewardSelection() {
        document.querySelectorAll(".uikick-reward-card .uikick-btn-outline").forEach(function (btn) {
            btn.addEventListener("click", function () {
                document.querySelectorAll(".uikick-reward-card").forEach(function (card) {
                    card.classList.remove("selected");
                });
                btn.closest(".uikick-reward-card").classList.add("selected");
            });
        });
    }

    function initSmoothScrollTOC() {
        document.querySelectorAll(".uikick-toc a").forEach(function (link) {
            link.addEventListener("click", function (ev) {
                var target = document.querySelector(link.getAttribute("href"));
                if (!target) return;
                ev.preventDefault();
                target.scrollIntoView({ behavior: "smooth", block: "start" });
            });
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        if (!document.querySelector(".uikick-detail")) return; // chỉ chạy trên trang detail
        initTabs();
        initRewardSelection();
        initSmoothScrollTOC();
    });
})();
