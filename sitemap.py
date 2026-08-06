from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/sitemap.xml", include_in_schema=False)
async def sitemap():

    urls = [
        "https://www.ruosystem.co.ke/",
        "https://www.ruosystem.co.ke/about",
        "https://www.ruosystem.co.ke/features",
        "https://www.ruosystem.co.ke/pricing",
        "https://www.ruosystem.co.ke/contact",
        "https://www.ruosystem.co.ke/blog",

        # Blog Posts
        "https://www.ruosystem.co.ke/blog/best-pos-system-kenya",
        "https://www.ruosystem.co.ke/blog/inventory-management-small-retail-shops-kenya",
        "https://www.ruosystem.co.ke/blog/choose-pos-system-small-business-kenya",
        "https://www.ruosystem.co.ke/blog/how-much-does-a-pos-system-cost-in-kenya"
        "https://www.ruosystem.co.ke/blog/best-pos-for-minisupermarkets-in-kenya"
    ]

    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

    for url in urls:
        xml += f"""
    <url>
        <loc>{url}</loc>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>"""

    xml += """
</urlset>
"""

    return Response(content=xml, media_type="application/xml")