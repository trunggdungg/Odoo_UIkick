# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

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
        reward_tiers = request.env['uikick.reward.tier'].sudo().search([], order='sequence, id')
        values = {
            'project': project,
            'tabs': TABS,
            'toc_items': TOC_ITEMS,
            'reward_tiers': reward_tiers,
        }
        return request.render('odoo_uikick.detail_page', values)
