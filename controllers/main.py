# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

# NOTE: Trong dự án thật, danh sách này nên được thay bằng một model Odoo
# (vd: uikick.project) và load qua request.env['uikick.project'].sudo().search([]).
# Ở đây giữ dạng dữ liệu tĩnh để bám sát 1:1 với src/data/projects.ts gốc.

CATEGORIES = [
    "Art", "Comics", "Crafts", "Dance", "Design", "Fashion",
    "Film & Video", "Food", "Games", "Journalism", "Music",
    "Photography", "Publishing", "Technology", "Theater",
]


TABS = ["Campaign", "Rewards", "Creator", "FAQ", "Updates", "Comments", "Community"]

TOC_ITEMS = [
    "Base Campaign Overview", "Design From Knowledge", "Benefiting: Portability",
    "3rd Gen. Cooling", "Larger Air Intake", "5 Mode Fan Control",
    "Ultimate Choices for Every Device", "4 Brains, Smarter Control",
    "Max 8TB, Swappable SSD", "100Gbps, Transfer Speed",
    "Low Power, High Compatibility", "Demo Test Video", "Timeline",
]

SORT_OPTIONS = ["Relevance", "Most funded", "Most backed", "Newest", "End date"]
ORDER_BY_SORT = {
    "Most funded": "percent_funded desc",
    "Most backed": "backers desc",
    "Newest": "create_date desc",
    "End date": "days_left asc",
}

GOAL_BUCKETS = {
    "under_1000": [("goal", "<", 1000)],
    "1000_10000": [("goal", ">=", 1000), ("goal", "<=", 10000)],
    "10000_100000": [("goal", ">=", 10000), ("goal", "<=", 100000)],
}


def _to_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None

class UikickController(http.Controller):

    @http.route(['/uikick', '/uikick/category/<string:category>'],
                type='http', auth='public', website=True, sitemap=True)
    def home(self, category=None, **kw):
        Project = request.env['uikick.project'].sudo()
        requested_category = category or "Technology"

        # fall back to the full catalog if the requested category has no projects
        domain = [('category', '=', requested_category)]
        if not Project.search_count(domain):
            domain = []

        statuses = [s for s in request.httprequest.args.getlist('status') if s in ('live', 'upcoming')]
        if statuses:
            domain.append(('status', 'in', statuses))

        location = (kw.get('location') or '').strip()
        if location:
            domain.append(('location', 'ilike', location))

        goal_bucket = kw.get('goal') or ''
        if goal_bucket in GOAL_BUCKETS:
            domain += GOAL_BUCKETS[goal_bucket]

        amount_min = _to_int(kw.get('amount_min'))
        if amount_min is not None:
            domain.append(('amount_raised', '>=', amount_min))
        amount_max = _to_int(kw.get('amount_max'))
        if amount_max is not None:
            domain.append(('amount_raised', '<=', amount_max))

        sort = kw.get('sort') or 'Relevance'
        order = ORDER_BY_SORT.get(sort, 'sequence asc, id asc')
        projects = Project.search(domain, order=order)
        values = {
            'categories': CATEGORIES,
            'active_category': requested_category,
            'projects': projects,
            'sort_options': SORT_OPTIONS,
            'filters': {
                'status': statuses,
                'location': location,
                'goal': goal_bucket,
                'amount_min': kw.get('amount_min') or '',
                'amount_max': kw.get('amount_max') or '',
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
        reward_tiers = request.env['uikick.reward.tier'].sudo().search([], order='sequence, id')
        values = {
            'project': project,
            'tabs': TABS,
            'toc_items': TOC_ITEMS,
            'reward_tiers': reward_tiers,
        }
        return request.render('odoo_uikick.detail_page', values)
