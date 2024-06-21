from django.shortcuts import redirect
from django.http import HttpResponseForbidden

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/o/secure/') and 'admin-control' in request.path:
            unique_id = request.path.split('/')[3]
            if not request.session.get('uid') or request.session.get('unique_id') != unique_id:
                return HttpResponseForbidden("403 Forbidden: Unauthorized access.")
        elif request.session.get('uid') and request.path == '/':
            return redirect(f"/o/secure/{request.session.get('unique_id')}/admin-control/")
        response = self.get_response(request)
        return response
