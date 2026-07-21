from odoo import fields, models


class UikickProject(models.Model):
    _name = 'uikick.project'
    _description = 'UIKick Crowdfunding Project'
    _rec_name = 'title'
    _order = 'sequence, id'

    sequence = fields.Integer(default=10)
    project_code = fields.Char(
        string='Project Code', required=True, index=True, copy=False,
        help="Stable slug used in the public URL /uikick/project/<project_code>.",
    )
    title = fields.Char(string='Title', required=True)
    creator = fields.Char(string='Creator', required=True)
    category = fields.Char(string='Category', required=True, index=True)
    location = fields.Char(string='Location')
    days_left = fields.Integer(string='Days Left')
    percent_funded = fields.Integer(string='Percent Funded')
    amount_raised = fields.Integer(string='Amount Raised (US$)')
    backers = fields.Integer(string='Backers')
    goal = fields.Integer(string='Goal (US$)')
    image = fields.Char(string='Image URL')
    video_url = fields.Char(string='Video URL')
    description = fields.Text(string='Description')
    status = fields.Selection([
        ('live', 'Live'),
        ('upcoming', 'Upcoming'),
        ('ended', 'Ended'),
    ], string='Status', default='live', required=True)
    campaign_number = fields.Integer(string='Campaign Number')
    total_raised = fields.Char(string='Total Raised (all campaigns)')
    total_backers = fields.Char(string='Total Backers (all campaigns)')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('project_code_uniq', 'unique(project_code)', 'Project code must be unique.'),
    ]