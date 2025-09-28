# Car Health Monitoring Dashboard 🚗 

A modern, full-stack web application that simulates a digital cockpit system for real-time vehicle diagnostics and health monitoring. Built with React, FastAPI, and modern web technologies.

![Dashboard Preview](https://img.shields.io/badge/Status-Live%20%26%20Running-brightgreen)
![Frontend](https://img.shields.io/badge/Frontend-React%20%2B%20TailwindCSS-blue)
![Backend](https://img.shields.io/badge/Backend-FastAPI%20%2B%20Python-green)

## 🌟 Live Demo

- **🚀 Frontend Application**: [https://quiet-speculoos-8fdeb4.netlify.app](https://quiet-speculoos-8fdeb4.netlify.app)
- **🔧 Backend API**: [https://car-health-backend-4.onrender.com](https://car-health-backend-4.onrender.com)
- **📚 API Documentation**: [https://car-health-backend-4.onrender.com/docs](https://car-health-backend-4.onrender.com/docs)

## ✨ Features

### Real-time Monitoring
- **Speed**: 0-120 km/h with visual gauge
- **Fuel Level**: 0-100% with progress indicators
- **Engine Temperature**: 70-120°C with warning alerts
- **RPM**: 600-4000 with real-time updates
- **Battery Voltage**: 11.8-14.2V with status indicators
- **Tire Pressure**: Individual monitoring for all four wheels

### 🚨 Smart Alert System
- ⚠️ Low Fuel Warning (<20%)
- 🔥 Engine Overheating Alert (>100°C)
- 🔋 Low Battery Voltage Alert (<12.0V)
- 🛞 Low Tire Pressure Alert (<31.0 PSI)

###  Advanced Visualization
- **Animated Radial Gauges** for speed and temperature
- **Progress Bars** with gradient colors
- **Historical Trend Charts** using Recharts
- **Responsive Design** for all devices
- **Glassmorphism UI** with modern aesthetics

###  Live Updates
- **Auto-refresh** every 5 seconds
- **Real-time data** from simulated car sensors
- **WebSocket-ready** architecture

##  Tech Stack

### Frontend
- **React 18** with Hooks and modern patterns
- **TailwindCSS** for responsive styling
- **Recharts** for data visualization
- **Component-based** architecture

### Backend
- **FastAPI** for high-performance API
- **Python** with type hints
- **CORS** enabled for cross-origin requests
- **Automatic API documentation** with Swagger UI

### Deployment
- **Frontend**: Netlify (CDN & Continuous Deployment)
- **Backend**: Render (Cloud Platform)
- **Version Control**: GitHub

## 🏗 Architecture

```
car-health-dashboard/
├── 📁 backend/
│   ├──  app/
│   │   └── main.py              # FastAPI application
│   └── requirements.txt         # Python dependencies
└── 📁 frontend/
    ├── 📁 public/               # Static assets
    ├── 📁 src/
    │   ├── 📁 components/       # React components
    │   │   ├── AnimatedRadialGauge.jsx
    │   │   ├── HistoryChart.jsx
    │   │   ├── EnhancedAlert.jsx
    │   │   └── ParticlesBackground.jsx
    │   ├── App.jsx              # Main application
    │   └── index.js             # Entry point
    ├── package.json             # Node dependencies
    └── tailwind.config.js       # Styling configuration
```

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ and npm
- Python 3.8+

### Backend Development
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### Frontend Development
```bash
cd frontend
npm install
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 📡 API Endpoints

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| `GET` | `/` | Welcome message | `{"message": "Car Health Monitoring API"}` |
| `GET` | `/car/status` | Current vehicle metrics | JSON with all sensor data |
| `GET` | `/car/history` | Historical data (last 10 readings) | Array of car status objects |

### Example Response
```json
{
  "speed": 85,
  "fuel": 45,
  "engineTemp": 92,
  "tirePressure": {
    "frontLeft": 32.5,
    "frontRight": 33.1,
    "rearLeft": 31.8,
    "rearRight": 32.2
  },
  "batteryVoltage": 13.2,
  "rpm": 2450,
  "timestamp": "2023-11-15T10:30:45.123456"
}
```

## 🎨 UI/UX Features

- **Dark Theme** with gradient backgrounds
- **Glassmorphism Effects** with backdrop blur
- **Smooth Animations** and transitions
- **Mobile-First** responsive design
- **Color-coded** status indicators (Green/Yellow/Red)
- **Particle Background** for visual appeal

## 🔧 Configuration

### Environment Variables
```env
# Frontend (.env)
REACT_APP_API_URL=https://car-health-backend-4.onrender.com

# Backend CORS Configuration
ALLOWED_ORIGINS=[
    "http://localhost:3000",
    "https://quiet-speculoos-8fdeb4.netlify.app",
    "https://*.netlify.app"
]
```

## 🚀 Deployment

### Backend (Render)
- Automatic deployment from GitHub main branch
- Free tier with cold start (may take 30-60 seconds on first request)

### Frontend (Netlify)
- Continuous deployment from GitHub
- CDN distribution for fast global access
- Environment variables for API configuration

## 📈 Performance

- **Frontend**: Optimized React build with code splitting
- **Backend**: FastAPI with async capabilities
- **Data Updates**: Polling every 5 seconds
- **Responsive**: Works on desktop, tablet, and mobile

## 🔮 Future Enhancements

- [ ] WebSocket implementation for real-time updates
- [ ] User authentication and multiple vehicles
- [ ] Data persistence with database
- [ ] Mobile app with React Native
- [ ] Predictive maintenance alerts
- [ ] Export functionality for reports

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



---

<div align="center">

**⭐ Star this repository if you find it helpful!**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Click_Here-blue?style=for-the-badge)](https://quiet-speculoos-8fdeb4.netlify.app)
[![API Docs](https://img.shields.io/badge/📚_API_Docs-Open_Swagger-green?style=for-the-badge)](https://car-health-backend-4.onrender.com/docs)

</div>

Built with ❤️ by **Kalaiyarasi Nagarajan**

> Dreamt, Designed, and Developed to revolutionize vehicle monitoring through real-time data visualization, empowering drivers with actionable insights for optimal car health and performance.






