# Astrology Application - Site Map, User Flows & Dashboard Design

## I. Site Map

### A. Public Area
1. **Home Page**
   - Introduction to the application
   - Features overview
   - Testimonials
   - Call to action (Create Chart)

2. **About**
   - Methodology
   - Team/Creators
   - Philosophy

3. **Features**
   - Element Analysis
   - Modality Analysis
   - Stellium Detection
   - Psychological Insights
   - Conscious vs. Unconscious Elements

4. **Pricing**
   - Free tier
   - Premium tier
   - Enterprise options

5. **Blog/Learning Center**
   - Astrological concepts
   - Case studies
   - Updates

6. **Contact/Support**

### B. User Area (Requires Authentication)
1. **Dashboard**
   - Overview of saved charts
   - Recent analyses
   - Account status

2. **Chart Creation**
   - Birth data entry
   - Chart generation

3. **Chart Analysis Hub**
   - Main chart view
   - Analysis sections (detailed below)

4. **Saved Charts**
   - List view
   - Comparison tool

5. **Account Management**
   - Profile settings
   - Subscription management
   - Preferences

6. **Learning Path**
   - Personalized learning based on chart
   - Educational content

## II. User Flows

### A. New User Flow
1. **Landing → Sign Up**
   - Enter email/create password
   - Confirm email

2. **Onboarding**
   - Brief tutorial on astrology basics
   - Enter first birth chart data
   - Generate first chart

3. **First Chart Experience**
   - Guided tour of main features
   - Highlight key insights
   - Prompt to save chart

4. **Account Completion**
   - Complete profile
   - Set preferences
   - Explore premium features

### B. Returning User Flow
1. **Login → Dashboard**
   - View saved charts
   - See any new features/updates

2. **Chart Selection**
   - Choose existing chart or create new

3. **Analysis Exploration**
   - Navigate between analysis sections
   - Dive deeper into specific insights

4. **Action Steps**
   - Save insights
   - Export/share chart
   - Schedule follow-up

### C. Chart Creation Flow
1. **Enter Birth Data**
   - Name
   - Date of birth
   - Time of birth (optional)
   - Place of birth

2. **Verification**
   - Confirm location (map)
   - Verify time zone
   - Adjust for daylight savings

3. **Chart Options**
   - Select analysis features
   - Include optional elements (asteroids, etc.)

4. **Generate Chart**
   - Processing indicator
   - Preview of basic chart wheel

5. **View Complete Analysis**
   - Redirect to Chart Analysis Hub

## III. Dashboard & UI Components

### A. Main Dashboard
1. **Header**
   - Logo
   - Navigation menu
   - User profile/settings
   - Notifications

2. **Quick Actions**
   - Create new chart
   - Access saved charts
   - Compare charts
   - Educational content

3. **Recent Charts**
   - Card view with thumbnails
   - Basic info (name, date)
   - Quick access buttons

4. **Insights Feed**
   - Recent or important insights
   - Astrological events relevant to user's chart
   - Learning recommendations

### B. Chart Analysis Hub
1. **Chart Overview Panel**
   - Interactive chart wheel
   - Basic chart data
   - Navigation to analysis sections

2. **Analysis Sections** (Tab or Accordion Style)
   - **Planet Positions**
     * Table view of all planets
     * Position details (sign, house, degrees)
     * Retrograde status
     * Critical degrees highlighted

   - **Element Analysis**
     * Element distribution chart
     * Planets by element
     * Element balance analysis
     * Conscious vs. Unconscious elements comparison

   - **Modality Analysis**
     * Modality distribution chart
     * Planets by modality
     * Modality pattern interpretation
     * Special cases highlighted

   - **Stellium Detection**
     * Visual representation of stelliums
     * Stellium strength indicators
     * Detailed interpretations
     * Impact on chart balance

   - **Psychological Insights**
     * Key personality traits
     * Emotional patterns
     * Cognitive style
     * Growth opportunities

   - **Element Relationships**
     * Primary relationship visualization
     * All significant relationships
     * Integration strategies
     * Psychological implications

3. **Detail Panel** (Context-sensitive)
   - Expanded information based on selection
   - Educational content
   - Practical applications
   - Related insights

### C. Conscious vs. Unconscious Elements Dashboard
1. **Educational Header**
   - Concept explanation
   - Legend for personal/social/transpersonal planets

2. **Comparison Visualization**
   - Side-by-side charts for conscious/unconscious elements
   - Difference indicators
   - Color-coded by element

3. **Element Categories**
   - **Conscious Elements (Personal Planets)**
     * Percentage breakdown
     * Planet list
     * Interpretation
     * Absent elements highlighted

   - **Bridging Elements (Social Planets)**
     * Percentage breakdown
     * Planet list
     * Interpretation
     * Transition role explanation

   - **Unconscious Elements (Transpersonal Planets)**
     * Percentage breakdown
     * Planet list
     * Interpretation
     * Hidden influences

4. **Significant Differences Panel**
   - Highlighted elements with major disparities
   - Detailed psychological interpretation
   - Integration suggestions
   - Growth opportunities

5. **Practical Applications**
   - Personal development suggestions
   - Relationship insights
   - Career implications
   - Health considerations

## IV. Responsive Design Considerations

### A. Desktop View (1200px+)
- Full chart wheel with detailed information
- Multi-column layout for analysis sections
- Side-by-side comparisons
- Expanded educational content

### B. Tablet View (768px-1199px)
- Slightly simplified chart wheel
- Collapsible sections for analysis
- Stacked comparisons with toggle options
- Condensed educational content

### C. Mobile View (320px-767px)
- Simplified chart representation
- Single column layout
- Progressive disclosure of information
- Essential insights prioritized
- Swipe navigation between sections

## V. Interactive Elements

### A. Chart Wheel
- Zoom functionality
- Planet selection for details
- Aspect line toggles
- House highlighting
- Animation options (planet movement)

### B. Data Visualizations
- Interactive pie/bar charts
- Toggles for different data views
- Highlight significant features
- Comparison sliders

### C. Educational Components
- Tooltips for astrological terms
- Expandable explanations
- "Learn more" links to detailed content
- Visual examples

### D. User Customization
- Color scheme options
- Detail level preferences
- Focus area selection
- Saved view configurations

## VI. Implementation Priorities

### Phase 1: Core Experience
1. User authentication
2. Chart creation flow
3. Basic chart wheel
4. Planet positions table
5. Element analysis (basic)
6. Simple dashboard

### Phase 2: Enhanced Analysis
1. Modality analysis
2. Stellium detection
3. Psychological insights
4. Element relationships
5. Expanded dashboard

### Phase 3: Advanced Features
1. Conscious vs. unconscious elements
2. Chart comparison tool
3. Predictive insights
4. Learning path
5. Social sharing

### Phase 4: Optimization
1. Performance improvements
2. Advanced customization
3. API integrations
4. Mobile app development
5. Enterprise features 