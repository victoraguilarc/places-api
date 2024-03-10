from django.http import JsonResponse


def healthcheck(_):
    return JsonResponse(
        {
            'name': 'Destinations API',
            'status': 'OK',
        }
    )
