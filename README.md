# 🍅 Pomodoro Timer

A sleek, browser-based Pomodoro Technique timer built with Streamlit. Boost your productivity with customizable focus sessions and an engaging visual progress tracker.

## ✨ Features

- **Customizable Timer**: Set focus sessions from 1 to 60 minutes
- **Dynamic Progress Bar**: Real-time visual feedback that scales perfectly with your selected duration
- **Smooth Animations**: 100-step progress updates for fluid user experience
- **Celebration Effects**: Balloon animation upon session completion
- **Responsive Design**: Clean, modern interface that works across devices
- **Zero Configuration**: No setup required - just run and focus!

## 🚀 Quick Start

### Prerequisites
```bash
pip install streamlit
```

### Running the Application
```bash
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`

## 🛠️ How It Works

### The Challenge: Dynamic Progress Bar Timing

Creating a progress bar that accurately reflects different time durations required solving a key technical challenge: how to make the progress complete in exactly the selected time, regardless of duration.

### The Solution: Mathematical Time Scaling

#### 1. Time Conversion
```python
total_seconds = time_minutes * 60
steps = 100
```
Convert user input to seconds and establish a fixed number of progress steps for consistent visual experience.

#### 2. Dynamic Sleep Calculation
```python
sleep_per_step = total_seconds / steps
```
Calculate the exact sleep duration needed between each progress update to ensure accurate timing.

#### 3. Percentage-Based Progress Updates
```python
progress = step / steps  # Always between 0.0 and 1.0
time_bar.progress(progress, text=time_text)
```
Use normalized progress values (0-1) for smooth, predictable progress bar behavior.

### State Management in Streamlit

Streamlit reruns the entire script on each user interaction. To handle timer state effectively:

```python
starter = 0
if st.button("Start"):
    starter = 1

if starter == 1:
    # Timer logic here
```

This approach uses flags to manage application state across Streamlit's execution model.

## 📊 Technical Specifications

| Feature | Implementation |
|---------|----------------|
| **Framework** | Streamlit |
| **Dependencies** | `streamlit`, `time` |
| **Progress Steps** | 100 (optimized for smooth animation) |
| **Time Range** | 1-60 minutes |
| **Update Frequency** | Dynamic (based on selected duration) |
| **Browser Compatibility** | All modern browsers |

## 📁 Project Structure

```
pomodoro-timer/
├── app.py          # Main Streamlit application
├── base.py         # Vanilla Python countdown timer (reference implementation)
├── README.md       # This file
└── requirements.txt # Python dependencies
```

## 🎯 Usage Examples

### Quick 5-Minute Break Timer
1. Set slider to 5 minutes
2. Click "Start"
3. Progress updates every 3 seconds

### Standard 25-Minute Pomodoro
1. Set slider to 25 minutes (default)
2. Click "Start"  
3. Progress updates every 15 seconds

### Extended 45-Minute Deep Work
1. Set slider to 45 minutes
2. Click "Start"
3. Progress updates every 27 seconds

## 🔧 Customization Options

### Adjusting Progress Smoothness
Modify the `steps` variable in the main application:
```python
steps = 100  # Default: smooth animation
steps = 50   # Faster updates, less smooth
steps = 200  # Ultra-smooth, more CPU intensive
```

### Custom Time Ranges
Adjust the slider parameters:
```python
time_minutes = st.slider(
    "Select focus time:",
    min_value=1,    # Minimum time
    max_value=120,  # Maximum time (2 hours)
    value=25        # Default value
)
```

## 🤝 Contributing

Contributions are welcome! Here are some areas for improvement:

- [ ] Sound notifications when timer completes
- [ ] Break timer integration (5/15 minute breaks)
- [ ] Session statistics and tracking
- [ ] Custom themes and color schemes
- [ ] Keyboard shortcuts (spacebar to start/pause)
- [ ] Task management integration

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Inspired by the [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) developed by Francesco Cirillo
- Built with [Streamlit](https://streamlit.io/) - the fastest way to build data apps

## 📞 Support

If you encounter any issues or have suggestions:
1. Check the [Issues](../../issues) page
2. Create a new issue with detailed description
3. Include your Python version and browser information

---

**⭐ Star this repository if you found it helpful!**

*Happy focusing! 🍅*