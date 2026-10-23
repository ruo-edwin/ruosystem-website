
from fastapi import APIRouter, Response
from xml.sax.saxutils import escape

router = APIRouter()


@router.get("/sitemap.xml", include_in_schema=False)
async def sitemap():

    # Highest priority: Homepage
    urls = [
        {
            "loc": "https://www.ruosystem.co.ke/",
            "priority": "1.0",
            "changefreq": "weekly"
        },

        # Industry-specific service pages
        {
            "loc": "https://www.ruosystem.co.ke/services/pos-for-cosmetic-shops",
            "priority": "0.95",
            "changefreq": "weekly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/services/pos-for-mini-supermarkets",
            "priority": "0.95",
            "changefreq": "weekly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/services/bookshop-pos-system-in-kenya-for-stock-and-sales-management",
            "priority": "0.95",
            "changefreq": "weekly"
        },
         {
                    "loc": "https://www.ruosystem.co.ke/services/stock-taking-services-for-cosmetic-shops",
                    "priority": "0.95",
                    "changefreq": "weekly"
                },
        # Other important website pages
        {
            "loc": "https://www.ruosystem.co.ke/about",
            "priority": "0.6",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/contact",
            "priority": "0.6",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog",
            "priority": "0.8",
            "changefreq": "weekly"
        },

        # Blog posts: informational SEO content
        {
            "loc": "https://www.ruosystem.co.ke/blog/best-pos-system-kenya",
            "priority": "0.8",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog/inventory-management-small-retail-shops-kenya",
            "priority": "0.8",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog/choose-pos-system-small-business-kenya",
            "priority": "0.8",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog/how-much-does-a-pos-system-cost-in-kenya",
            "priority": "0.8",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog/best-pos-for-minisupermarkets-in-kenya",
            "priority": "0.8",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog/where-can-l-buy-cosmetic-products-in-wholesale-in-kenya",
            "priority": "0.7",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog/how-much-does-pos-installation-cost-in-kenya",
            "priority": "0.8",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog/how-to-start-a-profitable-cosmetic-shop-in-kenya",
            "priority": "0.7",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog/best-pos-system-for-small-shops-in-kenya",
            "priority": "0.8",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog/can-you-use-a-pos-system-on-your-phone",
            "priority": "0.8",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog/pos-vs-excel-for-retail-shops-in-kenya",
            "priority": "0.8",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog/best-pos-system-for-multiple-shop-branches-in-kenya",
            "priority": "0.8",
            "changefreq": "monthly"
        },
        {
            "loc": "https://www.ruosystem.co.ke/blog/how-to-track-stock-and-sales-in-small-shop-kenya",
            "priority": "0.8",
            "changefreq": "monthly"
        }
    ]

    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

    for page in urls:
        loc = escape(page["loc"])
        priority = page["priority"]
        changefreq = page["changefreq"]

        xml += f"""
    <url>
        <loc>{loc}</loc>
        <changefreq>{changefreq}</changefreq>
        <priority>{priority}</priority>
    </url>
"""

    xml += """
</urlset>
"""

    return Response(
        content=xml,
        media_type="application/xml"
    )