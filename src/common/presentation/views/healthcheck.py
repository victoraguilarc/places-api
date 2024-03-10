from django.http import JsonResponse


def healthcheck(_):
    return JsonResponse(
        {
            'name': 'Places API',
            'status': 'OK',
        }
    )
