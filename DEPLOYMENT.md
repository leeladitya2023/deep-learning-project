# 🌱 Plant Disease Detection - Deployment Guide

This guide will help you deploy the Plant Disease Detection application to Streamlit Cloud.

## 🚀 Quick Deploy to Streamlit Cloud

### Option 1: Deploy via GitHub (Recommended)

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy to Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository: `Plant-Disease-Detection-main`
   - Set the main file path: `main_app.py`
   - Click "Deploy!"

### Option 2: Deploy via Streamlit CLI

1. **Install Streamlit:**
   ```bash
   pip install streamlit
   ```

2. **Deploy directly:**
   ```bash
   streamlit deploy main_app.py
   ```

## 📋 Prerequisites

- Python 3.8 or higher
- All dependencies listed in `requirements.txt`
- The model file `plant_disease_model.h5` (included in the repository)

## 🔧 Local Testing

Before deploying, test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main_app.py
```

The app will be available at `http://localhost:8501`

## 📁 Project Structure

```
Plant-Disease-Detection-main/
├── main_app.py              # Main Streamlit application
├── plant_disease_model.h5   # Pre-trained model
├── requirements.txt         # Python dependencies
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── Test Image/             # Sample images for testing
└── README.md              # Project documentation
```

## 🌐 Deployment Platforms

### Streamlit Cloud (Recommended)
- **Pros:** Free, easy setup, automatic deployments
- **Cons:** Limited resources, model size restrictions

### Heroku
- **Pros:** More resources, custom domains
- **Cons:** Requires credit card, more complex setup

### Google Cloud Platform
- **Pros:** Scalable, powerful
- **Cons:** Costs money, complex setup

## ⚠️ Important Notes

1. **Model Size:** The `plant_disease_model.h5` file is ~2.7MB, which is within Streamlit Cloud limits
2. **Dependencies:** All required packages are specified in `requirements.txt`
3. **File Uploads:** The app supports JPG, JPEG, and PNG image formats
4. **Performance:** First load may take a few seconds due to model loading

## 🐛 Troubleshooting

### Common Issues:

1. **Model Loading Error:**
   - Ensure `plant_disease_model.h5` is in the root directory
   - Check file permissions

2. **Dependency Issues:**
   - Verify all packages in `requirements.txt` are compatible
   - Try updating to latest versions

3. **Memory Issues:**
   - Reduce image size before processing
   - Use smaller model if available

## 📞 Support

If you encounter issues:
1. Check the Streamlit Cloud logs
2. Test locally first
3. Verify all files are properly committed to GitHub

## 🎉 Success!

Once deployed, your app will be available at a URL like:
`https://your-app-name.streamlit.app`

Share this URL with others to let them use your Plant Disease Detection system! 