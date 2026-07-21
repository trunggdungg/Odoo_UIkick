/** UIKick - Campaign detail page interactions */
(function () {
    "use strict";

    function initTabs() {
        var tabs = document.querySelectorAll(".uikick-tab");
        var contents = document.querySelectorAll(".uikick-tab-content");
        if (!tabs.length || !contents.length) return;
        tabs.forEach(function (tab) {
            tab.addEventListener("click", function (ev) {
                ev.preventDefault();
                var target = tab.getAttribute("data-tab");

                tabs.forEach(function (t) {
                    t.classList.remove("active");
                });
                tab.classList.add("active");
                // TODO: nếu tách nội dung mỗi tab thành section riêng,
                // ẩn/hiện tương ứng ở đây bằng data-tab attribute.

                contents.forEach(function (content) {
                    content.classList.toggle("active", content.getAttribute("data-tab") === target);
                });
            });
        });
    }

    function initHeroVideo() {
        var hero = document.getElementById("uikick-hero-video");
        if (!hero) return;
        var video = hero.querySelector(".uikick-hero-video-el");
        if (!video) return;

        hero.addEventListener("click", function () {
            if (hero.classList.contains("is-playing")) {
                video.pause();
                hero.classList.remove("is-playing");
            } else {
                video.play().then(function () {
                    hero.classList.add("is-playing");
                }).catch(function () {
                    /* autoplay blocked, ignore */
                });
            }
        });
    }

    function initRemindMe() {
        var buttons = document.querySelectorAll(".uikick-remind-btn");
        if (!buttons.length) return;
        var reminded = false;

        function render() {
            buttons.forEach(function (btn) {
                btn.classList.toggle("is-reminded", reminded);
                var label = btn.querySelector(".uikick-remind-label");
                if (label) label.textContent = reminded ? "Reminded!" : "Remind me";
            });
        }

        buttons.forEach(function (btn) {
            btn.addEventListener("click", function () {
                reminded = !reminded;
                render();
            });
        });
    }

    function initRewardSelection() {
        document.querySelectorAll(".uikick-reward-card .uikick-reward-select").forEach(function (btn) {
            btn.addEventListener("click", function () {
                document.querySelectorAll(".uikick-reward-card").forEach(function (card) {
                    card.classList.remove("selected");
                });
                btn.closest(".uikick-reward-card").classList.add("selected");
            });
        });
    }


    document.addEventListener("DOMContentLoaded", function () {
        if (!document.querySelector(".uikick-detail")) return; // chỉ chạy trên trang detail
        initTabs();
        initHeroVideo();
        initRemindMe();
        initRewardSelection();
    });
})();
