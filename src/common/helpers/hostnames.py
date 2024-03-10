from django.conf import settings


def build_frontend_path(*args):
    return '{frontend_hostname}/{path}'.format(
        frontend_hostname=settings.FRONTEND_HOSTNAME,
        path='/'.join(args),
    )
