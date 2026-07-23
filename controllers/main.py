# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

CATEGORIES = [
    "Art", "Comics", "Crafts", "Dance", "Design", "Fashion",
    "Film & Video", "Food", "Games", "Journalism", "Music",
    "Photography", "Publishing", "Technology", "Theater","Camera Equipment",
]

# Internal ids used for data-tab matching/JS — the visible label is translated
# separately via TAB_LABELS so the tab-switching logic doesn't have to compare
# against Vietnamese strings.
TABS = ["Campaign", "Rewards", "Creator", "FAQ", "Updates", "Comments", "Community"]
TAB_LABELS = {
    "Campaign": "Giới thiệu",
    "Rewards": "Tính năng",
    "Creator": "Tác giả",
    "FAQ": "FAQ",
    "Updates": "Cập nhật",
    "Comments": "Bình luận",
    "Community": "Cộng đồng",
}

TOC_ITEMS = [
    "Tổng quan sản phẩm", "Thiết kế dựa trên tri thức", "Lợi ích: Tính di động",
    "Tản nhiệt thế hệ 3", "Cửa hút gió lớn hơn", "Điều khiển quạt 5 chế độ",
    "Lựa chọn hoàn hảo cho mọi thiết bị", "4 bộ xử lý, điều khiển thông minh hơn",
    "SSD tháo rời tối đa 8TB", "Tốc độ truyền tải 100Gbps",
    "Tiết kiệm điện, tương thích cao", "Video demo", "Lộ trình ra mắt",
]

SORT_OPTIONS = ["Relevance", "Most viewed", "Newest", "End date"]
ORDER_BY_SORT = {
    "Most viewed": "views desc",
    "Newest": "create_date desc",
    "End date": "days_left asc",
}

class UikickController(http.Controller):

    @http.route(['/uikick', '/uikick/category/<string:category>'],
                type='http', auth='public', website=True, sitemap=True)
    def home(self, category=None, **kw):
        Project = request.env['uikick.project'].sudo()

        query_categories = [c for c in request.httprequest.args.getlist('category') if c in CATEGORIES]
        categories_submitted = 'categories_submitted' in request.httprequest.args

        if categories_submitted:
            # the sidebar's checkbox form was submitted — trust it as-is,
            # including an empty selection meaning "show every category"
            selected_categories = query_categories
        elif category:
            selected_categories = [category]
        else:
            selected_categories = ["Technology"]

        domain = [('category', 'in', selected_categories)] if selected_categories else []
        if domain and not Project.search_count(domain):
            # none of the selected categories have any projects – show everything instead
            domain = []

        statuses = [s for s in request.httprequest.args.getlist('status') if s in ('live', 'upcoming')]
        if statuses:
            domain.append(('status', 'in', statuses))

        location = (kw.get('location') or '').strip()
        if location:
            domain.append(('location', 'ilike', location))

        sort = kw.get('sort') or 'Relevance'
        order = ORDER_BY_SORT.get(sort, 'sequence asc, id asc')
        projects = Project.search(domain, order=order)

        if not selected_categories:
            header_label = 'All Projects'
        elif len(selected_categories) == 1:
            header_label = selected_categories[0]
        else:
            header_label = str(len(selected_categories)) + ' Categories'

        values = {
            'categories': CATEGORIES,
            'header_label': header_label,
            'projects': projects,
            'sort_options': SORT_OPTIONS,
            'filters': {
                'categories': selected_categories,
                'status': statuses,
                'location': location,
                'sort': sort,
            },
        }
        return request.render('odoo_uikick.home_page', values)

    @http.route(['/uikick/project/<string:project_id>'],
                type='http', auth='public', website=True, sitemap=False)
    def detail(self, project_id, **kw):
        Project = request.env['uikick.project'].sudo()
        project = Project.search([('project_code', '=', project_id)], limit=1)
        if not project:
            project = Project.search([('project_code', '=', '5')], limit=1) or Project.search([], limit=1)

        if project:
            project.views += 1
        reward_tiers = request.env['uikick.reward.tier'].sudo().search([], order='sequence, id')
        values = {
            'project': project,
            'tabs': TABS,
            'tab_labels': TAB_LABELS,
            'toc_items': TOC_ITEMS,
            'reward_tiers': reward_tiers,
        }
        return request.render('odoo_uikick.detail_page', values)
