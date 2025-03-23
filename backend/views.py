from django.http import HttpResponse


def home_view(request):
    endpoints = """
    <h1>Welcome to the Astrology API</h1>
    <p>Available endpoints:</p>
    <ul>
        <li><a href="/natal-chart/">/natal-chart/</a> - Generate a natal chart</li>
        <li><a href="/natal-chart/extract-data/">/natal-chart/extract-data/</a> - Extract data from token generated in natal-chart/</li>
        <li><a href="/accounts/register/">/accounts/register/</a> - Register a new user</li>
        <li><a href="/accounts/login/">/accounts/login/</a> - Login a user</li>
        <li><a href="/accounts/request-reset-email/">/accounts/request-reset-email/</a> - Request password reset email</li>
        <li><a href="/accounts/password-reset/&lt;uidb64&gt;/&lt;token&gt;/">/accounts/password-reset/&lt;uidb64&gt;/&lt;token&gt;/</a> - Password reset confirmation</li>
        <li><a href="/accounts/password-reset-complete/">/accounts/password-reset-complete/</a> - Complete password reset</li>
        <li><a href="/accounts/token/refresh/">/accounts/token/refresh/</a> - Refresh JWT token</li>
        <li><a href="/admin/">/admin/</a> - Admin interface</li>
    </ul>
    """
    return HttpResponse(endpoints)
