JARVIS Voice Assistant Documentation
====================================

I. Overview
-----------
A Python-based voice-controlled assistant with AI integration and automation capabilities. Features include:
- Voice command processing
- Sentiment analysis of commands
- System/application automation
- Email functionality
- Activity logging
- Gradio-based UI

II. Core Components
-------------------
A. Voice Engine
1. speak(audio): Non-blocking text-to-speech using pyttsx3
2. takeCommand(): Speech recognition via microphone input
3. wishMe(): Time-based greeting system

B. AI/ML Integration
1. analyze_sentiment(text): Emotion detection using Hugging Face's DistilBERT model
   - Returns: Emotion label with confidence percentage

C. Automation Features
1. Media Control:
   - playmusic(): Random music playback
   - play_spotify(): Spotify automation
   - open_youtube(): Browser automation for YouTube

2. System Tools:
   - open_calculator(): Launch Windows Calculator
   - open_notepad(text): Notepad with optional text input
   - system_shutdown(): Scheduled system shutdown
   - open_folder(path): File Explorer integration

3. Web Automation:
   - custom_website(url): Open any URL in Chrome
   - open_meet(): Direct access to Google Meet

D. Email System
1. sendEmail(to, content): Secure SMTP email sending
   - Uses Gmail SMTP server
   - MIME text formatting

E. UI Components (Gradio)
1. Voice Control Tab:
   - Microphone input
   - Command response display
   - Real-time sentiment analysis

2. Automation Controls Tab:
   - Quick-access buttons for common tasks
   - Custom website opener
   - Notepad with text input
   - System controls

3. Email Tab:
   - Recipient/content fields
   - Send button with status feedback

4. System Logs Tab:
   - Activity history (last 10 entries)

III. Key Features
-----------------
A. Voice Commands
- "Wikipedia [query]" - Summary from Wikipedia
- "Search [query] in google" - Google search
- "Open chrome" - Launch Chrome browser
- "Play music" - Random music playback
- "The time" - Current time announcement
- "Open calculator" - System calculator
- "Shutdown" - Schedule system shutdown

B. Automation Controls
- One-click access to:
  - Spotify/YouTube
  - Google Meet
  - System tools (Notepad, Calculator)
  - File Explorer locations
  - Custom websites

C. Security Features
- App password authentication for email
- Input validation for critical operations
- Error handling for SMTP connections

IV. Technical Requirements
--------------------------
A. Dependencies
- Python 3.8+
- Required packages (see requirements.txt):
  gradio, pyttsx3, SpeechRecognition, transformers, 
  selenium, pyautogui, wikipedia

B. Configuration
1. Email Setup:
   - Replace EMAIL_ADDRESS and EMAIL_PASSWORD
   - Use app password for Gmail

2. Path Configuration:
   - Update music_dir path in playmusic()
   - Set ChromeDriver path if not in system PATH

V. Usage Guide
--------------
1. Initialization:
   - Run main script: python jarvis.py
   - System greets user and opens Gradio UI

2. Voice Commands:
   - Click microphone icon
   - Wait for "Speak Now" prompt
   - View results in Command Response

3. Automation Panel:
   - Use buttons for common tasks
   - Enter custom URLs/text as needed

4. Email System:
   - Complete recipient/content fields
   - Click "Send Email"
   - Check status box for results

VI. Error Handling
------------------
- Failed commands logged in System Logs
- Clear error messages for:
  - Email authentication failures
  - Invalid file paths
  - Website unreachable
  - Voice recognition errors

VII. Limitations & Future Improvements
--------------------------------------
Current Limitations:
- Windows-specific path handling
- Chrome dependency for web automation
- Basic error recovery

Planned Features:
- Multi-language support
- Calendar integration
- Weather API integration
- Voice command customization
- Cross-platform compatibility

VIII. Security Notes
--------------------
- Never commit actual email credentials
- Use virtual environments
- Regular ChromeDriver updates recommended
- Consider using environment variables for secrets

IX. Support
-----------
For issues/questions, contact: budhanikapil0015@gmail.com
