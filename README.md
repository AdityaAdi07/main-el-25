# Disaster Information Aggregator & Verifier (DIAV)

A comprehensive disaster management system that combines real-time IoT data, social media analytics, and advanced graph algorithms to provide accurate, verified disaster information for emergency response teams.

## 🌟 Features

### Core Functionality
- **Real-time Disaster Monitoring**: Live feed of disaster events across India
- **Intelligent Data Verification**: AI-powered verification system for disaster reports
- **Interactive Mapping**: Visual representation of disaster locations and emergency services
- **Weather-based Risk Prediction**: Advanced algorithms to predict disaster risks
- **Emergency Service Coordination**: Mapping and coordination of emergency services
- **Multi-role Access**: Separate interfaces for administrators and general users

### Advanced Analytics
- **Graph Algorithm Simulations**: Network analysis for disaster response optimization
- **IoT Sensor Integration**: Real-time sensor data collection and analysis
- **Mathematical Modeling**: Statistical models for disaster prediction
- **Communication Network Simulation**: Emergency communication system modeling

## 🏗️ Architecture

### Frontend Components
- **Main Dashboard** (`frontend/`): Primary user interface with live feeds and analytics
- **Landing Page** (`landing-page/`): Project introduction and feature showcase
- **Authentication System** (`auth/`): User login and role-based access
- **User Panel** (`user/`): Dedicated user interface

### Backend Services
- **Flask API** (`backend/app.py`): Main REST API server
- **Data Collection** (`datacollect.py`): Weather and disaster data aggregation
- **Web Visualization** (`simulation/web_visualization/`): Interactive mapping system

### Data Management
- **Structured Data** (`data/`): Organized disaster and event datasets
- **JSON Storage**: Flexible data storage for various disaster types
- **CSV Integration**: Historical data analysis capabilities

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js (for frontend dependencies)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd main-el-25-pruts-fin
   ```

2. **Install Python dependencies**
   ```bash
   # Main application
   pip install -r user/requirements.txt
   
   # Web visualization
   pip install -r simulation/web_visualization/requirements.txt
   ```

3. **Install Node.js dependencies**
   ```bash
   cd frontend
   npm install
   cd ../landing-page
   npm install
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   WEATHER_API_KEY=your_weather_api_key
   GEMINI_API_KEY=your_gemini_api_key
   NEWS_API_KEY=your_news_api_key
   ```

### Running the Application

1. **Start the main backend server**
   ```bash
   cd backend
   python app.py
   ```
   The main dashboard will be available at `http://localhost:5000`

2. **Start the web visualization server**
   ```bash
   cd simulation/web_visualization
   python app.py
   ```
   The interactive map will be available at `http://localhost:5001`

3. **Launch the landing page**
   ```bash
   cd landing-page
   # Open index.html in a web browser
   ```

## 📊 System Components

### 1. Main Dashboard (`frontend/`)
- **Live Feed**: Real-time disaster news and updates
- **Interactive Map**: Geographic visualization of disaster locations
- **Analytics Panel**: Statistical analysis and trends
- **Admin Panel**: Administrative controls and data management
- **Alert System**: Real-time notifications and warnings

### 2. Data Collection System (`datacollect.py`)
- **Weather API Integration**: Real-time weather data collection
- **Risk Assessment**: AI-powered disaster risk prediction
- **Historical Analysis**: Past weather pattern analysis
- **Report Generation**: Automated disaster summary reports

### 3. Web Visualization (`simulation/web_visualization/`)
- **Interactive Maps**: Folium-based geographic visualization
- **Emergency Services**: Mapping of hospitals, fire stations, police stations
- **Disaster Locations**: Real-time disaster event plotting
- **Route Planning**: Emergency response route optimization

### 4. Authentication System (`auth/`)
- **User Management**: Role-based access control
- **Admin Interface**: Administrative user management
- **Security**: Secure login and session management

## 🔧 Configuration

### API Keys Required
- **WeatherAPI**: For weather data collection
- **Gemini API**: For AI-powered analysis and summaries
- **NewsAPI**: For real-time disaster news

### Database Configuration
The system uses JSON files for data storage:
- `data/disaster_news.json`: Disaster news articles
- `data/event_data_india.json`: Historical event data
- `data/structured_disaster_data.json`: Processed disaster information

## 📈 Usage Examples

### For Emergency Responders
1. Access the main dashboard at `http://localhost:5000`
2. View real-time disaster alerts and live feed
3. Use the interactive map to locate emergency services
4. Monitor risk assessments and weather conditions

### For Administrators
1. Access the admin panel at `http://localhost:5000/admin`
2. Manage user accounts and permissions
3. Verify and approve disaster reports
4. Monitor system analytics and performance

### For Data Analysts
1. Use the analytics panel for detailed statistical analysis
2. Access simulation tools for disaster modeling
3. Generate reports using the mathematical models
4. Analyze communication network efficiency

## 🛠️ Development

### Project Structure
```
main-el-25-pruts-fin/
├── auth/                    # Authentication system
├── backend/                 # Main Flask API
├── data/                    # Data storage
├── frontend/               # Main dashboard
├── landing-page/           # Project landing page
├── simulation/             # Simulation tools
├── user/                   # User panel
└── datacollect.py         # Data collection script
```

### Adding New Features
1. **Frontend**: Add new components in `frontend/js/` and `frontend/css/`
2. **Backend**: Extend API endpoints in `backend/app.py`
3. **Data**: Add new data sources in `datacollect.py`
4. **Visualization**: Create new map features in `simulation/web_visualization/`

## 🔒 Security Features

- **Role-based Access Control**: Different interfaces for different user types
- **Data Verification**: AI-powered verification of disaster reports
- **Secure API Endpoints**: Protected REST API with CORS support
- **Input Validation**: Comprehensive data validation and sanitization

## 📊 Analytics & Reporting

### Available Reports
- **Disaster Risk Assessment**: Weather-based risk prediction
- **Emergency Service Coverage**: Geographic analysis of service availability
- **Response Time Analysis**: Performance metrics for emergency response
- **Trend Analysis**: Historical disaster pattern analysis

### Simulation Tools
- **Graph Algorithm Simulation**: Network analysis for response optimization
- **IoT Sensor Simulation**: Real-time sensor data modeling
- **Communication Network Simulation**: Emergency communication system modeling
- **Mathematical Model Simulation**: Statistical disaster prediction models

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation in each component directory

## 🔄 Updates & Maintenance

### Regular Maintenance Tasks
- Update API keys and credentials
- Refresh disaster data sources
- Monitor system performance
- Update dependencies and security patches

### Data Backup
- Regular backup of JSON data files
- Version control for configuration changes
- Disaster recovery procedures

---

**Note**: This system is designed for educational and research purposes. For production deployment, additional security measures and infrastructure considerations should be implemented.
