from django.http import HttpResponse
from django.shortcuts import render
from django.urls import get_resolver


def home_view(request):
    return render(request, 'home.html')

def endpoints_view(request):
    """Display all available endpoints in the project as a web page."""
    try:
        url_patterns = extract_views_from_urlpatterns(get_resolver().url_patterns)
        
        # Group endpoints by app
        endpoints_by_app = {}
        
        for pattern in url_patterns:
            url = pattern['pattern']
            name = pattern.get('name', '')
            app_name = pattern.get('app_name', '')
            app_name = app_name if app_name else 'Root'
            
            if app_name not in endpoints_by_app:
                endpoints_by_app[app_name] = []
                
            endpoints_by_app[app_name].append({
                'url': url,
                'name': name
            })
        
        context = {
            'endpoints_by_app': endpoints_by_app,
        }
        
        try:
            # Try to use the template
            return render(request, 'endpoints.html', context)
        except Exception as e:
            # If template fails, generate HTML directly
            html = generate_endpoints_html(endpoints_by_app)
            return HttpResponse(html)
    except Exception as e:
        # If anything fails, return a simple error message
        return HttpResponse(f"<h1>Error retrieving endpoints</h1><p>{str(e)}</p>")

def generate_endpoints_html(endpoints_by_app):
    """Generate HTML for endpoints if template loading fails."""
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Astrology API Endpoints</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f7f4ff;
            }
            header {
                background: linear-gradient(135deg, #4a2882 0%, #7b5db2 100%);
                color: white;
                padding: 30px;
                text-align: center;
                border-radius: 12px;
                margin-bottom: 30px;
                box-shadow: 0 8px 16px rgba(74, 40, 130, 0.2);
            }
            h1 {
                margin: 0;
                font-size: 2.5em;
                text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
            }
            h2 {
                color: #4a2882;
                border-bottom: 2px solid #4a2882;
                padding-bottom: 10px;
                margin-top: 30px;
                font-size: 1.8em;
            }
            h3 {
                color: #7b5db2;
                margin-top: 20px;
                margin-bottom: 15px;
                font-size: 1.4em;
            }
            .endpoint-section {
                background-color: white;
                border-radius: 12px;
                padding: 25px;
                margin-bottom: 30px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            }
            .endpoint-category {
                background-color: #f9f6ff;
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 20px;
                border-left: 4px solid #4a2882;
            }
            .endpoint {
                background-color: #f9f9f9;
                border-left: 4px solid #7b5db2;
                padding: 15px;
                margin-bottom: 15px;
                border-radius: 0 8px 8px 0;
            }
            .endpoint-url {
                font-family: monospace;
                font-weight: bold;
                color: #2c3e50;
                font-size: 1.1em;
            }
            .endpoint-name {
                display: inline-block;
                background-color: #4a2882;
                color: white;
                font-size: 0.8em;
                padding: 3px 8px;
                border-radius: 4px;
                margin-left: 10px;
            }
            .endpoint-method {
                font-size: 0.9em;
                color: #666;
                margin-top: 5px;
            }
            .try-button {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                padding: 5px 10px;
                text-decoration: none;
                border-radius: 4px;
                font-size: 0.9em;
                float: right;
            }
            footer {
                margin-top: 50px;
                text-align: center;
                color: #777;
                font-size: 0.9em;
                padding: 20px;
            }
            .badge {
                display: inline-block;
                padding: 3px 8px;
                border-radius: 12px;
                font-size: 0.8em;
                margin-right: 8px;
                margin-top: 8px;
                font-weight: bold;
            }
            .badge-main {
                background-color: #e0d6f9;
                color: #4a2882;
            }
            .badge-element {
                background-color: #d6f9e0;
                color: #2b823a;
            }
            .badge-modality {
                background-color: #f9e0d6;
                color: #823a2b;
            }
            .badge-stellium {
                background-color: #d6e0f9;
                color: #2b3a82;
            }
            .category-header {
                display: flex;
                align-items: center;
                margin-bottom: 15px;
            }
            .description {
                font-size: 0.9em;
                color: #555;
                margin-top: 5px;
                margin-bottom: 15px;
            }
            .endpoint-description {
                font-size: 0.85em;
                color: #666;
                margin-top: 8px;
                line-height: 1.4;
            }
            .stars {
                margin-top: 15px;
                font-size: 1.5em;
                letter-spacing: 10px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Astrology API Endpoints</h1>
            <p>Documentation of all available endpoints in the application</p>
            <div class="stars">✨ 🌙 ⭐ 🪐 ✨</div>
        </header>

        <main>
    """
    
    # First add natal chart endpoints in organized categories
    html += """
        <div class="endpoint-section">
            <h2>NATAL CHART ENDPOINTS</h2>
            <p class="description">These endpoints provide detailed astrological analysis based on birth information.</p>
            
            <!-- Main endpoint -->
            <div class="endpoint-category">
                <div class="category-header">
                    <h3>Main Chart Analysis</h3>
                </div>
                <p class="description">Generate complete natal chart data with planetary placements and aspects.</p>
                
                <div class="endpoint">
                    <div class="endpoint-url">
                        http://localhost:8000/natal-chart/
                        <span class="endpoint-name">generate_natal_chart</span>
                        <span class="badge badge-main">Main</span>
                        <a href="http://localhost:8000/natal-chart/test/" class="try-button">Try it</a>
                    </div>
                    <div class="endpoint-method">
                        Method: POST - Requires JSON data with user birth information
                    </div>
                    <div class="endpoint-description">
                        Provides a complete natal chart analysis including planet positions, aspects, and psychological insights.
                    </div>
                </div>
            </div>
            
            <!-- Elements endpoints -->
            <div class="endpoint-category">
                <div class="category-header">
                    <h3>Elements Analysis</h3>
                </div>
                <p class="description">Analyze the distribution and relationships between elemental energies (Fire, Earth, Air, Water).</p>
                
                <div class="endpoint">
                    <div class="endpoint-url">
                        http://localhost:8000/natal-chart/elements/
                        <span class="endpoint-name">element_analysis</span>
                        <span class="badge badge-element">Elements</span>
                        <a href="http://localhost:8000/natal-chart/elements/" class="try-button">Try it</a>
                    </div>
                    <div class="endpoint-method">
                        Method: POST - Requires JSON data with user birth information
                    </div>
                    <div class="endpoint-description">
                        Analyzes the distribution of elemental energies in the chart, showing percentages and identifying dominant and weakest elements.
                    </div>
                </div>
                
                <div class="endpoint">
                    <div class="endpoint-url">
                        http://localhost:8000/natal-chart/elements/relationships/
                        <span class="endpoint-name">element_relationships</span>
                        <span class="badge badge-element">Elements</span>
                        <a href="http://localhost:8000/natal-chart/elements/relationships/" class="try-button">Try it</a>
                    </div>
                    <div class="endpoint-method">
                        Method: POST - Requires JSON data with user birth information
                    </div>
                    <div class="endpoint-description">
                        Provides insights into how the different elemental energies interact within the chart, focusing on the relationship between dominant elements.
                    </div>
                </div>
            </div>
            
            <!-- Modalities endpoint -->
            <div class="endpoint-category">
                <div class="category-header">
                    <h3>Modality Analysis</h3>
                </div>
                <p class="description">Analyze the distribution of modalities (Cardinal, Fixed, Mutable) in the natal chart.</p>
                
                <div class="endpoint">
                    <div class="endpoint-url">
                        http://localhost:8000/natal-chart/modalities/
                        <span class="endpoint-name">modality_analysis</span>
                        <span class="badge badge-modality">Modalities</span>
                        <a href="http://localhost:8000/natal-chart/modalities/" class="try-button">Try it</a>
                    </div>
                    <div class="endpoint-method">
                        Method: POST - Requires JSON data with user birth information
                    </div>
                    <div class="endpoint-description">
                        Analyzes the distribution of modal energies (Cardinal, Fixed, Mutable) in the chart, showing percentages and identifying dominant modality.
                    </div>
                </div>
            </div>
            
            <!-- Stelliums endpoint -->
            <div class="endpoint-category">
                <div class="category-header">
                    <h3>Stellium Detection</h3>
                </div>
                <p class="description">Detect and analyze stelliums (3+ planets in the same sign or house) in the natal chart.</p>
                
                <div class="endpoint">
                    <div class="endpoint-url">
                        http://localhost:8000/natal-chart/stelliums/
                        <span class="endpoint-name">stellium_detection</span>
                        <span class="badge badge-stellium">Stelliums</span>
                        <a href="http://localhost:8000/natal-chart/stelliums/" class="try-button">Try it</a>
                    </div>
                    <div class="endpoint-method">
                        Method: POST - Requires JSON data with user birth information
                    </div>
                    <div class="endpoint-description">
                        Identifies stelliums (3+ planets in the same sign or house) and provides detailed interpretations of their influence on the chart.
                    </div>
                </div>
            </div>
            
            <!-- Test form -->
            <div class="endpoint-category">
                <div class="category-header">
                    <h3>Test Interface</h3>
                </div>
                <p class="description">Interactive form for testing the natal chart API.</p>
                
                <div class="endpoint">
                    <div class="endpoint-url">
                        http://localhost:8000/natal-chart/test/
                        <span class="endpoint-name">test_form</span>
                        <span class="badge badge-main">Testing</span>
                        <a href="http://localhost:8000/natal-chart/test/" class="try-button">Try it</a>
                    </div>
                    <div class="endpoint-method">
                        Method: GET - Interactive web form for testing the API
                    </div>
                    <div class="endpoint-description">
                        Provides a user-friendly web interface for inputting birth data and testing the natal chart API endpoints.
                    </div>
                </div>
            </div>
        </div>
    """
    
    # Add the other app sections (except natal_chart which we already handled)
    for app_name, endpoints in endpoints_by_app.items():
        if app_name != 'natal_chart':
            html += f"""
            <div class="endpoint-section">
                <h2>{app_name.upper()} ENDPOINTS</h2>
            """
            
            for endpoint in endpoints:
                url = endpoint['url']
                name = endpoint.get('name', '')
                
                html += f"""
                <div class="endpoint">
                    <div class="endpoint-url">
                        {url}
                        {f'<span class="endpoint-name">{name}</span>' if name else ''}
                    </div>
                    
                    <div class="endpoint-method">
                        Method: GET/POST
                    </div>
                </div>
                """
            
            html += """
            </div>
            """
    
    # Add footer and close tags
    html += """
        </main>

        <footer>
            <p>Astrology API - All rights reserved &copy; 2023</p>
        </footer>
    </body>
    </html>
    """
    
    return html

def extract_views_from_urlpatterns(urlpatterns, base='', app_name=''):
    """
    Extract views from URL patterns recursively.
    """
    patterns = []
    for pattern in urlpatterns:
        if hasattr(pattern, 'url_patterns'):
            # This is an include - recurse into it
            namespace = getattr(pattern, 'namespace', app_name)
            patterns.extend(extract_views_from_urlpatterns(
                pattern.url_patterns,
                base + str(pattern.pattern),
                namespace
            ))
        else:
            # This is a URL pattern
            view_name = ''
            if hasattr(pattern, 'name') and pattern.name:
                view_name = pattern.name
                
            pattern_str = str(pattern.pattern)
            # Remove ^ and $ from the regex pattern
            pattern_str = pattern_str.replace('^', '').replace('$', '')
            
            patterns.append({
                'pattern': base + pattern_str,
                'name': view_name,
                'app_name': app_name
            })
    return patterns
