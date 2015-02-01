from django.conf import settings

def mustaches(request):
    """
    Returns strings representing the mustache.js template tags. This is
    necessary because they are the same as Django templates.
    """
    return {
    "mustache": "{{",
    "mustache_end": "}}"
    }

def env_urls(context):
    return {
        'SITE_URL': settings.SITE_URL,
		'CLIENT_ID': settings.CLIENT_ID,
    }
