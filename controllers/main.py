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

PROJECTS = [
    {
        "id": "1", "title": "Meet Beni, Your First All-Terrain Camera Robot",
        "creator": "Moxian Robots", "category": "Camera Equipment", "location": "Palo Alto, CA",
        "days_left": 41, "percent_funded": 100, "amount_raised": 394711, "backers": 1842, "goal": 50000,
        "image": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=560&h=315&fit=crop&auto=format",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4",
        "description": "4K Imaging | Smart Auto-following | 119 MPH Max Speed | Obstacle-avoiding | Auto-stitch highlights",
        "status": "live",
    },
    {
        "id": "2", "title": "Paperclip: The Social Accountability App",
        "creator": "Paperclip Team", "category": "Apps", "location": "San Francisco, CA",
        "days_left": 23, "percent_funded": 65, "amount_raised": 32500, "backers": 892, "goal": 50000,
        "image": "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=560&h=315&fit=crop&auto=format",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",
        "description": "Build better habits with social accountability and real community support",
        "status": "live",
    },
    {
        "id": "3", "title": "NanoKVM-Go: World's First All Native CH32V USB-C KVM",
        "creator": "Sipeed", "category": "Technology", "location": "Shenzhen, China",
        "days_left": 16, "percent_funded": 441, "amount_raised": 220500, "backers": 3241, "goal": 50000,
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=560&h=315&fit=crop&auto=format",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/SubaruOutbackOnStreetAndDirt.mp4",
        "description": "Control any computer remotely via USB-C — plug in, no software needed",
        "status": "live",
    },
    {
        "id": "4", "title": "Laverne R9 Dynamic Ergonomic Chair",
        "creator": "Laverne Design", "category": "Design", "location": "Berlin, Germany",
        "days_left": 28, "percent_funded": 234, "amount_raised": 117000, "backers": 567, "goal": 50000,
        "image": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=560&h=315&fit=crop&auto=format",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
        "description": "Premium ergonomic chair that dynamically adapts to your posture throughout the day",
        "status": "live",
    },
    {
        "id": "5", "title": "Disk Pro 2 | Ultimate Choice Cooling Hub for EDC Devices",
        "creator": "SHARGE Tech", "category": "Technology", "location": "Shenzhen, China",
        "days_left": 26, "percent_funded": 828, "amount_raised": 414371, "backers": 4194, "goal": 50000,
        "image": "https://images.unsplash.com/photo-1601524909162-ae8725290836?w=560&h=315&fit=crop&auto=format",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
        "description": "8-ports | Ice-storm Cooler | Magnetic Attachment | Pocket Size | 4 Control Chips | Max 8TB Swappable SSD | 10Gbps | HDMI 2.1 | Lanyard Cable",
        "status": "live",
    },
    {
        "id": "6", "title": "Lumys: Track Your Heart Disease Risk with Style",
        "creator": "Lumys Health", "category": "Health & Fitness", "location": "Austin, TX",
        "days_left": 19, "percent_funded": 178, "amount_raised": 89000, "backers": 1234, "goal": 50000,
        "image": "https://images.unsplash.com/photo-1434494878577-86c23bcb06b9?w=560&h=315&fit=crop&auto=format",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4",
        "description": "Smart health tracker monitoring cardiovascular risk in real-time with clinical accuracy",
        "status": "live",
    },
    {
        "id": "7", "title": "Health Tracker Pro: Advanced Biometric Monitoring",
        "creator": "BioTech Labs", "category": "Health & Fitness", "location": "Boston, MA",
        "days_left": 33, "percent_funded": 145, "amount_raised": 72500, "backers": 987, "goal": 50000,
        "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=560&h=315&fit=crop&auto=format",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
        "description": "Track blood oxygen, heart rate, sleep, and stress in one elegant wearable device",
        "status": "live",
    },
    {
        "id": "8", "title": "100Gbps Transfer Speed Portable SSD Enclosure",
        "creator": "SpeedTech Solutions", "category": "Technology", "location": "Taipei, Taiwan",
        "days_left": 12, "percent_funded": 892, "amount_raised": 446000, "backers": 5678, "goal": 50000,
        "image": "https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=560&h=315&fit=crop&auto=format",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
        "description": "Revolutionary SSD enclosure achieving true 100Gbps transfer speeds in your pocket",
        "status": "live",
    },
    {
        "id": "9", "title": "Mini DTG: Wearable Air Quality Monitor",
        "creator": "AirSense Technologies", "category": "Technology", "location": "Seoul, South Korea",
        "days_left": 45, "percent_funded": 67, "amount_raised": 33500, "backers": 423, "goal": 50000,
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=560&h=315&fit=crop&auto=format",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4",
        "description": "Pocket-sized air quality sensor with real-time PM2.5, CO2, and VOC monitoring",
        "status": "upcoming",
    },
    {
        "id": "10", "title": "MagBlade: World's Thinnest Wireless Charger",
        "creator": "Chroma Tech", "category": "Technology", "location": "Tokyo, Japan",
        "days_left": 38, "percent_funded": 312, "amount_raised": 156000, "backers": 2891, "goal": 50000,
        "image": "https://images.unsplash.com/photo-1512054502232-10a0a035d672?w=560&h=315&fit=crop&auto=format",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4",
        "description": "1.2mm ultra-thin 15W MagSafe compatible wireless charger — stick it anywhere",
        "status": "live",
    },
    {
        "id": "11", "title": "FlowDesk Standing Desk Converter Pro",
        "creator": "Flow Workspace", "category": "Design", "location": "Portland, OR",
        "days_left": 21, "percent_funded": 189, "amount_raised": 94500, "backers": 743, "goal": 50000,
        "image": "https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=560&h=315&fit=crop&auto=format",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",
        "description": "Transform any desk into a sit-stand workstation in under 5 seconds",
        "status": "live",
    },
    {
        "id": "12", "title": "EcoBottle: Smart Self-Cleaning Water Bottle",
        "creator": "PureLife Systems", "category": "Product Design", "location": "Amsterdam, Netherlands",
        "days_left": 52, "percent_funded": 43, "amount_raised": 21500, "backers": 289, "goal": 50000,
        "image": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=560&h=315&fit=crop&auto=format",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/SubaruOutbackOnStreetAndDirt.mp4",
        "description": "UV-C LED self-sterilization, temperature display, and 72-hour insulation",
        "status": "upcoming",
    },
]

TABS = ["Campaign", "Rewards", "Creator", "FAQ", "Updates", "Comments", "Community"]

TOC_ITEMS = [
    "Base Campaign Overview", "Design From Knowledge", "Benefiting: Portability",
    "3rd Gen. Cooling", "Larger Air Intake", "5 Mode Fan Control",
    "Ultimate Choices for Every Device", "4 Brains, Smarter Control",
    "Max 8TB, Swappable SSD", "100Gbps, Transfer Speed",
    "Low Power, High Compatibility", "Demo Test Video", "Timeline",
]

REWARD_TIERS = [
    {"id": 1, "title": "Early Bird Special", "amount": 79,
     "description": "Disk Pro 2 × 1 unit. Save 20% off retail price.",
     "estimated": "January 2026", "backers": 1203, "limited": True, "remaining": 47},
    {"id": 2, "title": "Standard Pledge", "amount": 99,
     "description": "Disk Pro 2 × 1 unit with lanyard cable included.",
     "estimated": "January 2026", "backers": 2104, "limited": False},
    {"id": 3, "title": "Duo Pack", "amount": 185,
     "description": "Disk Pro 2 × 2 units. Perfect for home + office.",
     "estimated": "January 2026", "backers": 487, "limited": False},
    {"id": 4, "title": "Pro Bundle", "amount": 249,
     "description": "Disk Pro 2 × 2 units + 2TB NVMe SSD. Ready to use out of the box.",
     "estimated": "February 2026", "backers": 298, "limited": False},
]


class UikickController(http.Controller):

    @http.route(['/uikick', '/uikick/category/<string:category>'],
                type='http', auth='public', website=True, sitemap=True)
    def home(self, category=None, **kw):
        active_category = category or "Technology"
        projects = [p for p in PROJECTS if p['category'] == active_category]
        if not projects:
            # fallback: no exact category match in mock data, show everything
            projects = PROJECTS
        values = {
            'categories': CATEGORIES,
            'active_category': active_category,
            'projects': projects,
        }
        return request.render('odoo_uikick.home_page', values)

    @http.route(['/uikick/project/<string:project_id>'],
                type='http', auth='public', website=True, sitemap=False)
    def detail(self, project_id, **kw):
        project = next((p for p in PROJECTS if p['id'] == project_id), PROJECTS[4])
        values = {
            'project': project,
            'tabs': TABS,
            'toc_items': TOC_ITEMS,
            'reward_tiers': REWARD_TIERS,
        }
        return request.render('odoo_uikick.detail_page', values)
