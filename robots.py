from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/robots.txt", include_in_schema=False)
async def robots():
    content = """User-agent: *
Allow: /

Sitemap: https://www.ruosystem.co.ke/sitemap.xml
"""

    return Response(content=content, media_type="text/plain")