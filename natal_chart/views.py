from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
print("About to import immanuel package...")
try:
    from immanuel import charts
    print("Successfully imported immanuel.charts!")
    IMMANUEL_AVAILABLE = True
except ImportError as e:
    print(f"Failed to import immanuel package: {str(e)}")
    IMMANUEL_AVAILABLE = False
    print("Warning: immanuel package not available. Using mock implementation for testing.")
    
    # Mock implementation for testing
    class MockSubject:
        def __init__(self, datetime_str, latitude, longitude):
            self.datetime_str = datetime_str
            self.latitude = latitude
            self.longitude = longitude
            
    class MockSign:
        def __init__(self, name, element, modality):
            self.name = name
            self.element = element
            self.modality = modality
            
    class MockLongitude:
        def __init__(self, deg, min, sec):
            self.degrees = deg
            self.minutes = min
            self.seconds = sec
            
    class MockHouse:
        def __init__(self, name):
            self.name = name
            
    class MockMovement:
        def __init__(self, retrograde=False):
            self.retrograde = retrograde
            
    class MockObject:
        def __init__(self, name, sign, house, sign_longitude, retrograde=False):
            self.name = name
            self.sign = sign
            self.house = house
            self.sign_longitude = sign_longitude
            self.movement = MockMovement(retrograde)
            
    class MockCharts:
        class Subject:
            def __init__(self, datetime_str, latitude, longitude):
                self.datetime_str = datetime_str
                self.latitude = latitude
                self.longitude = longitude
                
        class Natal:
            def __init__(self, subject):
                self.subject = subject
                
                # Create mock objects for testing
                sun_sign = MockSign("Aries", "fire", "cardinal")
                moon_sign = MockSign("Taurus", "earth", "fixed")
                mercury_sign = MockSign("Gemini", "air", "mutable")
                venus_sign = MockSign("Cancer", "water", "cardinal")
                mars_sign = MockSign("Leo", "fire", "fixed")
                jupiter_sign = MockSign("Virgo", "earth", "mutable")
                
                # Mock objects dictionary
                self.objects = {
                    "sun": MockObject("Sun", sun_sign, MockHouse("House 1"), MockLongitude(15, 30, 0)),
                    "moon": MockObject("Moon", moon_sign, MockHouse("House 2"), MockLongitude(10, 45, 0)),
                    "mercury": MockObject("Mercury", mercury_sign, MockHouse("House 3"), MockLongitude(5, 15, 0)),
                    "venus": MockObject("Venus", venus_sign, MockHouse("House 4"), MockLongitude(20, 0, 0)),
                    "mars": MockObject("Mars", mars_sign, MockHouse("House 5"), MockLongitude(25, 30, 0), True),
                    "jupiter": MockObject("Jupiter", jupiter_sign, MockHouse("House 6"), MockLongitude(8, 15, 0)),
                    "saturn": MockObject("Saturn", MockSign("Libra", "air", "cardinal"), MockHouse("House 7"), MockLongitude(12, 0, 0)),
                    "uranus": MockObject("Uranus", MockSign("Scorpio", "water", "fixed"), MockHouse("House 8"), MockLongitude(3, 45, 0)),
                    "neptune": MockObject("Neptune", MockSign("Sagittarius", "fire", "mutable"), MockHouse("House 9"), MockLongitude(17, 30, 0)),
                    "pluto": MockObject("Pluto", MockSign("Capricorn", "earth", "cardinal"), MockHouse("House 10"), MockLongitude(22, 15, 0)),
                    "north_node": MockObject("North Node", MockSign("Aquarius", "air", "fixed"), MockHouse("House 11"), MockLongitude(9, 0, 0)),
                    "south_node": MockObject("South Node", MockSign("Leo", "fire", "fixed"), MockHouse("House 5"), MockLongitude(9, 0, 0)),
                    "ascendant": MockObject("Ascendant", MockSign("Aries", "fire", "cardinal"), MockHouse("House 1"), MockLongitude(0, 0, 0)),
                    "midheaven": MockObject("Midheaven", MockSign("Capricorn", "earth", "cardinal"), MockHouse("House 10"), MockLongitude(0, 0, 0)),
                }
    
    # Replace the charts module with our mock
    charts = MockCharts

from .serializers import NatalChartSerializer
import swisseph as swe
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from datetime import timedelta
from natal_chart.static_collection.collections import (
    immanuel_charts,
    psychological_planets_list,
)
from natal_chart.views_methods.GenerateNatalChartView import (
    get_location,
    get_psychological_insights,
    extract_house_number,
    find_ephemeris_directory,
    extract_data_from_json_file,
    calculate_signs_power,
)
from natal_chart.views_methods.stellium_detection import (
    detect_stelliums,
    get_stellium_descriptions,
    detect_sign_stelliums_only,
    get_sign_stellium_descriptions_only
)
from natal_chart.views_methods.modality_analyzer import generate_modality_analysis
from natal_chart.views_methods.element_analyzer import analyze_elements
from natal_chart.views_methods.element_relationship_analyzer import analyze_element_relationships, get_all_element_relationships
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class CustomToken(RefreshToken):
    @classmethod
    def for_user(cls, user, extra_data=None):
        token = super().for_user(user)
        token.set_exp(lifetime=timedelta(hours=3))
        if extra_data:
            token["data"] = extra_data
        return token


@method_decorator(csrf_exempt, name='dispatch')
class GenerateNatalChartView(APIView):
    def post(self, request):
        serializer = NatalChartSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            date_of_birth = serializer.validated_data["date_of_birth"]
            time_of_birth = serializer.validated_data.get("time_of_birth")
            place_of_birth = serializer.validated_data["place_of_birth"]

            # Check if time is provided
            has_time = time_of_birth is not None

            coordinates = get_location(place_of_birth)
            if not coordinates:
                return Response(
                    {
                        "detail": "Could not determine location for the given place of birth."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            latitude, longitude = coordinates
            datetime_of_birth = (
                f"{date_of_birth} {time_of_birth}"
                if time_of_birth
                else f"{date_of_birth}"
            )
            
            try:
                # Create a Subject and Natal chart
                native = charts.Subject(datetime_of_birth, latitude, longitude)
                natal = charts.Natal(native)

                # Extract planet positions
                planet_positions = []
                psychological_insights = []
                name_mapping = extract_data_from_json_file("name_mapping")
                ordered_psychological_insights = extract_data_from_json_file(
                    "ordered_psychological_insights"
                )
                planet_titles = extract_data_from_json_file("planet_titles")

                planet_sign_info = {}

                for obj_key in immanuel_charts:
                    obj = natal.objects[obj_key]
                    planet_name = name_mapping.get(obj.name, obj.name)
                    
                    # Only include house information if time is provided
                    house_number = None
                    if has_time:
                        house_number = extract_house_number(obj.house.name)

                    sign_info = {
                        "name": obj.sign.name,
                        "modality": obj.sign.modality,
                        "element": obj.sign.element,
                    }

                    planet_data = {
                        "planet": planet_name,
                        "position": {
                            "degrees": obj.sign_longitude.degrees,
                            "minutes": obj.sign_longitude.minutes,
                            "seconds": obj.sign_longitude.seconds,
                        },
                        "sign": sign_info,
                        "house": house_number,
                        "movement": {
                            "retrograde": (
                                obj.movement.retrograde
                                if hasattr(obj, "movement")
                                else None
                            )
                        },
                    }

                    # Skip angles if time is not provided
                    if not has_time and planet_name in ["Ascendant", "Descendant", "Midheaven", "Imum Coeli"]:
                        continue
                    
                    planet_positions.append(planet_data)

                    planet_sign_info[planet_name] = sign_info

                    if obj_key in psychological_planets_list:
                        title = planet_titles.get(planet_name, "")
                        psychological_data = get_psychological_insights(
                            planet_name, obj.sign.name, house_number, title
                        )

                        if psychological_data:
                            # Remove the redundant fields we don't need to display
                            if "planet" in psychological_data:
                                del psychological_data["planet"]
                            if "sign" in psychological_data:
                                del psychological_data["sign"]
                            
                            ordered_psychological_insights[planet_name] = psychological_data

                # Create a new psychological insights array with only the main planets
                # This replaces the previous implementation to avoid duplicates
                psychological_insights = []
                # Only include the main planets we want to show insights for
                main_planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
                for planet in main_planets:
                    if planet in ordered_psychological_insights:
                        insight = ordered_psychological_insights[planet]
                        
                        # Create the base structure
                        formatted_insight = {
                            "title": insight.get("title", f"{planet} in Unknown"),
                            "subtitle": planet_titles.get(planet, ""),
                            "traits": insight.get("traits", ""),
                            "planet": planet,
                            "descriptions": []
                        }
                        
                        # Add descriptions based on planet type
                        if planet == "Sun":
                            # Sun format
                            descriptions = [
                                {"name": "Explanation", "description": insight.get("explanation", "")},
                                {"name": "Innate Talents", "description": insight.get("innate_talents", "")},
                                {"name": "Growth Areas", "description": insight.get("growth_areas", "")},
                                {"name": "Personal Growth", "description": insight.get("personal_growth", "")},
                                {"name": "Closing Affirmation", "description": insight.get("closing_affirmation", "")}
                            ]
                        elif planet == "Moon":
                            # Moon format
                            descriptions = [
                                {"name": "Explanation", "description": insight.get("explanation", "")},
                                {"name": "Emotional Strengths", "description": insight.get("emotional_strengths", "")},
                                {"name": "Emotional Challenges", "description": insight.get("emotional_challenges", "")},
                                {"name": "Actionable Emotional Care", "description": insight.get("actionable_emotional_care", "")},
                                {"name": "Closing Affirmation", "description": insight.get("closing_affirmation", "")}
                            ]
                        elif planet in ["Venus", "Mars", "Mercury"]:
                            # Venus, Mars, Mercury format
                            descriptions = [
                                {"name": "Strengths in Connection", "description": insight.get("strengths_in_connection", "")},
                                {"name": "Challenges to Refine", "description": insight.get("challenges_to_refine", "")},
                                {"name": "Actionable Strategies", "description": insight.get("actionable_strategies", "")},
                                {"name": "Affirmation", "description": insight.get("affirmation", "")}
                            ]
                        elif planet in ["Uranus", "Neptune", "Pluto"]:
                            # Outer planets format
                            descriptions = [
                                {"name": "Core Themes", "description": insight.get("core_themes", "")},
                                {"name": "Collective Purpose", "description": insight.get("collective_purpose", "")},
                                {"name": "Strengths", "description": insight.get("strengths", "")},
                                {"name": "Challenges", "description": insight.get("challenges", "")},
                                {"name": "Actionable Contribution", "description": insight.get("actionable_contribution", "")},
                                {"name": "Affirmation", "description": insight.get("affirmation", "")}
                            ]
                        else:
                            # Default format for other planets like Jupiter, Saturn
                            descriptions = [
                                {"name": "Explanation", "description": insight.get("explanation", "")}
                            ]
                            # Add any available fields
                            for field in insight:
                                if field not in ["title", "subtitle", "traits", "planet"] and field not in [d["name"] for d in descriptions]:
                                    descriptions.append({"name": field.replace("_", " ").title(), "description": insight.get(field, "")})
                        
                        # Filter out empty descriptions
                        formatted_insight["descriptions"] = [d for d in descriptions if d["description"]]
                        psychological_insights.append(formatted_insight)

                # Store user data for passing to tab generators
                user_data = {
                    "name": name,
                    "date_of_birth": str(date_of_birth),
                    "place_of_birth": place_of_birth,
                    "coordinates": {"latitude": latitude, "longitude": longitude}
                }

                # Create response object with only essential fields
                objects_data = {
                    "psychologicalInsights": psychological_insights,
                    "has_time": has_time,
                }
                
                # Add time of birth if provided
                if has_time:
                    objects_data["time_of_birth"] = str(time_of_birth)
                    
                    # Detect stelliums (including houses)
                    stelliums = detect_stelliums(
                        planet_positions, 
                        min_planets=3, 
                        include_points=False,  # Set to True to include points like North Node
                        tight_orb=True  # Detect tight stelliums (planets within 8 degrees)
                    )
                    
                    # Get stellium descriptions
                    stellium_descriptions = get_stellium_descriptions(stelliums)
                else:
                    # For time-less charts, only include sign stelliums
                    sign_stelliums = detect_sign_stelliums_only(
                        planet_positions, 
                        min_planets=3,
                        include_points=False,  # Set to True to include points like North Node
                        tight_orb=True  # Detect tight stelliums (planets within 8 degrees)
                    )
                    
                    # Get only sign stellium descriptions
                    stellium_descriptions = get_sign_stellium_descriptions_only(sign_stelliums)
                
                # Calculate elements power (always include this)
                signs_power = calculate_signs_power(planet_positions)
                
                # Generate modality analysis
                modality_analysis = generate_modality_analysis(planet_positions)
                
                # Generate element analysis (new addition)
                # Convert planet_positions to the format expected by element_analyzer
                formatted_planets = []
                for planet in planet_positions:
                    formatted_planet = {
                        "name": planet["planet"],
                        "sign": planet["sign"]["name"],
                        "house": planet["house"],
                        "movement": planet["movement"]  # Include retrograde information
                    }
                    
                    # Include position information for critical degree detection
                    if "position" in planet:
                        formatted_planet["position"] = planet["position"]
                    
                    formatted_planets.append(formatted_planet)
                
                # Generate elements tab response instead of separate element analysis
                from .views_methods.element_analyzer import generate_elements_tab_response
                elements_tab_data = generate_elements_tab_response(formatted_planets)
                
                # We'll keep allElementRelationships for additional relationship data
                # that might be useful elsewhere in the app
                from .views_methods.element_relationship_analyzer import get_all_element_relationships
                element_analysis = analyze_elements(formatted_planets)
                all_relationships = get_all_element_relationships(element_analysis["percentages"])
                if all_relationships:
                    elements_tab_data["allElementRelationships"] = all_relationships
                
                objects_data["elements_tab"] = elements_tab_data
                
                # Generate overview tab data
                from .views_methods.overview_tab_generator import generate_overview_tab
                overview_tab_data = generate_overview_tab(
                    user_name=user_data["name"],
                    date_of_birth=user_data["date_of_birth"],
                    place_of_birth=user_data["place_of_birth"],
                    coordinates=user_data["coordinates"],
                    psychological_insights=psychological_insights,
                    stellium_descriptions=stellium_descriptions,
                    modality_analysis=modality_analysis,
                    elements_tab=elements_tab_data
                )
                objects_data["overview"] = overview_tab_data
                
                # Generate patterns tab data
                from .views_methods.patterns_tab_generator import generate_patterns_tab
                patterns_tab_data = generate_patterns_tab(
                    stellium_descriptions=stellium_descriptions,
                    modality_analysis=modality_analysis
                )
                objects_data["patterns_tab"] = patterns_tab_data
                
                # Check if user is authenticated before creating a token
                is_authenticated = request.user.is_authenticated
                token = None
                
                if is_authenticated:
                    refresh = CustomToken.for_user(request.user, extra_data=objects_data)
                    token = {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "is_authenticated": is_authenticated,
                    }
                    objects_data["token_with_data"] = token
                
                return Response(objects_data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(
                    {"detail": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExtractDataFromTokenView(APIView):
    def post(self, request):
        token_str = request.data.get("token", None)
        if not token_str:
            return Response(
                {"detail": "Token not provided or invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            token = AccessToken(token_str)
            extra_data = token.get("data", None)
            if not extra_data:
                return Response(
                    {"detail": "No extra data found in token"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            return Response({"data": extra_data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

@method_decorator(csrf_exempt, name='dispatch')
class ElementAnalysisView(APIView):
    def post(self, request):
        serializer = NatalChartSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Import name_mapping
                name_mapping = extract_data_from_json_file("name_mapping")
                
                # Extract data from request
                date_of_birth = serializer.validated_data["date_of_birth"]
                time_of_birth = serializer.validated_data.get("time_of_birth")
                place_of_birth = serializer.validated_data["place_of_birth"]

                # Get coordinates
                coordinates = get_location(place_of_birth)
                if not coordinates:
                    return Response(
                        {"detail": "Could not determine location for the given place of birth."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                latitude, longitude = coordinates
                datetime_of_birth = f"{date_of_birth} {time_of_birth}" if time_of_birth else f"{date_of_birth}"

                # Create chart
                native = charts.Subject(datetime_of_birth, latitude, longitude)
                natal = charts.Natal(native)

                # Format planet positions
                planet_positions = []
                for obj_key in immanuel_charts:
                    obj = natal.objects[obj_key]
                    planet_name = name_mapping.get(obj.name, obj.name)
                    
                    # Only include house information if time is provided
                    house_number = None
                    if time_of_birth:
                        house_number = extract_house_number(obj.house.name)
                    
                    sign_info = {
                        "name": obj.sign.name,
                        "modality": obj.sign.modality,
                        "element": obj.sign.element,
                    }
                    
                    planet_data = {
                        "name": planet_name,
                        "sign": sign_info["name"],
                        "house": house_number,
                        "movement": {
                            "retrograde": obj.movement.retrograde if hasattr(obj, "movement") else None
                        }
                    }
                    
                    if "position" in planet_data:
                        planet_data["position"] = {
                            "degrees": obj.sign_longitude.degrees,
                            "minutes": obj.sign_longitude.minutes,
                            "seconds": obj.sign_longitude.seconds,
                        }
                    
                    planet_positions.append(planet_data)

                # Generate element analysis
                element_analysis = analyze_elements(planet_positions)
                
                # Ensure element_percentages is included in the response
                if "element_percentages" not in element_analysis:
                    # Create it if not already present (for backward compatibility)
                    element_percentages = []
                    for element, value in element_analysis["percentages"].items():
                        element_percentages.append({
                            "name": element.capitalize(),
                            "value": value
                        })
                    # Sort by value in descending order
                    element_percentages = sorted(element_percentages, key=lambda x: x["value"], reverse=True)
                    element_analysis["element_percentages"] = element_percentages
                
                return Response(element_analysis, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(
                    {"detail": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class ElementRelationshipsView(APIView):
    def post(self, request):
        serializer = NatalChartSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Import name_mapping
                name_mapping = extract_data_from_json_file("name_mapping")
                
                # Extract data from request
                date_of_birth = serializer.validated_data["date_of_birth"]
                time_of_birth = serializer.validated_data.get("time_of_birth")
                place_of_birth = serializer.validated_data["place_of_birth"]

                # Get coordinates
                coordinates = get_location(place_of_birth)
                if not coordinates:
                    return Response(
                        {"detail": "Could not determine location for the given place of birth."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                latitude, longitude = coordinates
                datetime_of_birth = f"{date_of_birth} {time_of_birth}" if time_of_birth else f"{date_of_birth}"

                # Create chart
                native = charts.Subject(datetime_of_birth, latitude, longitude)
                natal = charts.Natal(native)

                # Format planet positions
                planet_positions = []
                for obj_key in immanuel_charts:
                    obj = natal.objects[obj_key]
                    planet_name = name_mapping.get(obj.name, obj.name)
                    
                    # Only include house information if time is provided
                    house_number = None
                    if time_of_birth:
                        house_number = extract_house_number(obj.house.name)
                    
                    sign_info = {
                        "name": obj.sign.name,
                        "modality": obj.sign.modality,
                        "element": obj.sign.element,
                    }
                    
                    planet_data = {
                        "name": planet_name,
                        "sign": sign_info["name"],
                        "house": house_number,
                        "movement": {
                            "retrograde": obj.movement.retrograde if hasattr(obj, "movement") else None
                        }
                    }
                    
                    if "position" in planet_data:
                        planet_data["position"] = {
                            "degrees": obj.sign_longitude.degrees,
                            "minutes": obj.sign_longitude.minutes,
                            "seconds": obj.sign_longitude.seconds,
                        }
                    
                    planet_positions.append(planet_data)

                # Generate element analysis
                element_analysis = analyze_elements(planet_positions)
                
                # Get element relationships
                primary_relationship = analyze_element_relationships(element_analysis["percentages"])
                all_relationships = get_all_element_relationships(element_analysis["percentages"])
                
                response_data = {
                    "primaryRelationship": primary_relationship,
                    "allRelationships": all_relationships
                }
                
                return Response(response_data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(
                    {"detail": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class ModalityAnalysisView(APIView):
    def post(self, request):
        serializer = NatalChartSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Import name_mapping
                name_mapping = extract_data_from_json_file("name_mapping")
                
                # Extract data from request
                date_of_birth = serializer.validated_data["date_of_birth"]
                time_of_birth = serializer.validated_data.get("time_of_birth")
                place_of_birth = serializer.validated_data["place_of_birth"]

                # Get coordinates
                coordinates = get_location(place_of_birth)
                if not coordinates:
                    return Response(
                        {"detail": "Could not determine location for the given place of birth."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                latitude, longitude = coordinates
                datetime_of_birth = f"{date_of_birth} {time_of_birth}" if time_of_birth else f"{date_of_birth}"

                # Create chart
                native = charts.Subject(datetime_of_birth, latitude, longitude)
                natal = charts.Natal(native)

                # Format planet positions
                planet_positions = []
                for obj_key in immanuel_charts:
                    obj = natal.objects[obj_key]
                    planet_name = name_mapping.get(obj.name, obj.name)
                    
                    # Only include house information if time is provided
                    house_number = None
                    if time_of_birth:
                        house_number = extract_house_number(obj.house.name)
                    
                    sign_info = {
                        "name": obj.sign.name,
                        "modality": obj.sign.modality,
                        "element": obj.sign.element,
                    }
                    
                    planet_data = {
                        "name": planet_name,
                        "sign": sign_info["name"],
                        "house": house_number,
                        "movement": {
                            "retrograde": obj.movement.retrograde if hasattr(obj, "movement") else None
                        }
                    }
                    
                    if "position" in planet_data:
                        planet_data["position"] = {
                            "degrees": obj.sign_longitude.degrees,
                            "minutes": obj.sign_longitude.minutes,
                            "seconds": obj.sign_longitude.seconds,
                        }
                    
                    planet_positions.append(planet_data)

                # Generate modality analysis
                modality_analysis = generate_modality_analysis(planet_positions)
                
                # Create a response with the consistent format
                response_data = {
                    "dominant_modality": modality_analysis["dominant_modality"],
                    "percentages": modality_analysis["percentages"],
                    "modality_percentages": modality_analysis.get("modality_percentages", []),
                    "description": modality_analysis["description"]
                }
                
                return Response(response_data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(
                    {"detail": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class StelliumDetectionView(APIView):
    def post(self, request):
        serializer = NatalChartSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Import name_mapping
                name_mapping = extract_data_from_json_file("name_mapping")
                
                # Extract data from request
                date_of_birth = serializer.validated_data["date_of_birth"]
                time_of_birth = serializer.validated_data.get("time_of_birth")
                place_of_birth = serializer.validated_data["place_of_birth"]

                # Get coordinates
                coordinates = get_location(place_of_birth)
                if not coordinates:
                    return Response(
                        {"detail": "Could not determine location for the given place of birth."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                latitude, longitude = coordinates
                datetime_of_birth = f"{date_of_birth} {time_of_birth}" if time_of_birth else f"{date_of_birth}"

                # Create chart
                native = charts.Subject(datetime_of_birth, latitude, longitude)
                natal = charts.Natal(native)

                # Format planet positions
                planet_positions = []
                for obj_key in immanuel_charts:
                    obj = natal.objects[obj_key]
                    planet_name = name_mapping.get(obj.name, obj.name)
                    
                    # Only include house information if time is provided
                    house_number = None
                    if time_of_birth:
                        house_number = extract_house_number(obj.house.name)
                    
                    sign_info = {
                        "name": obj.sign.name,
                        "modality": obj.sign.modality,
                        "element": obj.sign.element,
                    }
                    
                    planet_data = {
                        "planet": planet_name,
                        "position": {
                            "degrees": obj.sign_longitude.degrees,
                            "minutes": obj.sign_longitude.minutes,
                            "seconds": obj.sign_longitude.seconds,
                        },
                        "sign": sign_info,
                        "house": house_number,
                        "movement": {
                            "retrograde": obj.movement.retrograde if hasattr(obj, "movement") else None
                        }
                    }
                    
                    planet_positions.append(planet_data)

                # Detect stelliums
                if time_of_birth:
                    stelliums = detect_stelliums(
                        planet_positions,
                        min_planets=3,
                        include_points=False,
                        tight_orb=True
                    )
                    stellium_descriptions = get_stellium_descriptions(stelliums)
                else:
                    stelliums = detect_sign_stelliums_only(
                        planet_positions,
                        min_planets=3,
                        include_points=False,
                        tight_orb=True
                    )
                    stellium_descriptions = get_sign_stellium_descriptions_only(stelliums)

                response_data = {
                    # "stelliums": stelliums,  # Remove stelliums from the response
                    "stelliumDescriptions": stellium_descriptions,
                }
                
                return Response(response_data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(
                    {"detail": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class PatternsTabView(APIView):
    def post(self, request):
        serializer = NatalChartSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Import name_mapping
                name_mapping = extract_data_from_json_file("name_mapping")
                
                # Extract data from request
                date_of_birth = serializer.validated_data["date_of_birth"]
                time_of_birth = serializer.validated_data.get("time_of_birth")
                place_of_birth = serializer.validated_data["place_of_birth"]

                # Get coordinates
                coordinates = get_location(place_of_birth)
                if not coordinates:
                    return Response(
                        {"detail": "Could not determine location for the given place of birth."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                latitude, longitude = coordinates
                datetime_of_birth = f"{date_of_birth} {time_of_birth}" if time_of_birth else f"{date_of_birth}"

                # Create chart
                native = charts.Subject(datetime_of_birth, latitude, longitude)
                natal = charts.Natal(native)

                # Format planet positions
                planet_positions = []
                for obj_key in immanuel_charts:
                    obj = natal.objects[obj_key]
                    planet_name = name_mapping.get(obj.name, obj.name)
                    
                    # Only include house information if time is provided
                    house_number = None
                    if time_of_birth:
                        house_number = extract_house_number(obj.house.name)
                    
                    sign_info = {
                        "name": obj.sign.name,
                        "modality": obj.sign.modality,
                        "element": obj.sign.element,
                    }
                    
                    planet_data = {
                        "planet": planet_name,
                        "position": {
                            "degrees": obj.sign_longitude.degrees,
                            "minutes": obj.sign_longitude.minutes,
                            "seconds": obj.sign_longitude.seconds,
                        },
                        "sign": sign_info,
                        "house": house_number,
                        "movement": {
                            "retrograde": obj.movement.retrograde if hasattr(obj, "movement") else None
                        }
                    }
                    
                    planet_positions.append(planet_data)

                # Step 1: Detect stelliums based on time availability
                if time_of_birth:
                    stelliums = detect_stelliums(
                        planet_positions,
                        min_planets=3,
                        include_points=False,
                        tight_orb=True
                    )
                    stellium_descriptions = get_stellium_descriptions(stelliums)
                else:
                    stelliums = detect_sign_stelliums_only(
                        planet_positions,
                        min_planets=3,
                        include_points=False,
                        tight_orb=True
                    )
                    stellium_descriptions = get_sign_stellium_descriptions_only(stelliums)

                # Step 2: Generate modality analysis
                modality_analysis = generate_modality_analysis(planet_positions)
                
                # Step 3: Generate patterns tab data
                from .views_methods.patterns_tab_generator import generate_patterns_tab
                patterns_tab_data = generate_patterns_tab(
                    stellium_descriptions=stellium_descriptions,
                    modality_analysis=modality_analysis
                )
                
                return Response(patterns_tab_data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(
                    {"detail": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



