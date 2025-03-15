from imports import *

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize AI Model for Sentiment Analysis
sentiment_analyzer = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")
EMAIL_ADDRESS = 'kapillju@gmail.com'
EMAIL_PASSWORD = 'hbbo htdp shej iggi'

# Initialize Voice Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Automation Log
automation_log = []

# ======================
# Critical Fixes Section
# ======================
def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        pass
# threading.Thread(target=speak).start()

def clear_audio():
    """Reset audio input component"""
    return None

def analyze_sentiment(text):
    """Robust sentiment analysis with validation"""
    try:
        if not text.strip() or len(text.strip()) < 3:
            return "Input too short for analysis"
        result = sentiment_analyzer(text)[0]
        return f"Emotion: {result['label']} ({result['score']*100:.1f}%)"
    except Exception as e:
        return "Sentiment analysis unavailable"

def background_listener():
    """Error-resistant background command processor"""
    while True:
        try:
            query = takeCommand()
            if query:
                response = handle_command(query)
                sentiment = analyze_sentiment(query)
                automation_log.append(f"{datetime.now()}: {query}")
        except Exception as e:
            pass
            time.sleep(1)

# ======================
# Core Functionality
# ======================

def wishMe():
    hour = datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
        time.sleep(2)
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
        time.sleep(2)   
    else:
        speak("Good Evening!")  
        time.sleep(2)
    speak("I am Jarvis Sir.Open the server for further use")
    time.sleep(2)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in').lower()
        return query
    except Exception as e:
        pass

def sendEmail(to, content):
    try:
        # Validate inputs
        if not all([to.strip(), content.strip()]):
            raise ValueError("Recipient and content cannot be empty")

        # Create message
        msg = MIMEText(content)
        msg['Subject'] = 'Message from JARVIS'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to

        # Secure connection
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            
        return True, "Email sent successfully!"
    
    except smtplib.SMTPAuthenticationError:
        return False, "Authentication failed. Check email/password."
    except smtplib.SMTPException as e:
        return False, f"Email server error: {str(e)}"
    except Exception as e:
        return False, f"General error: {str(e)}"

def playmusic():
    music_dir = r'Music'
    songs = os.listdir(music_dir)
    a = random.randint(0,len(songs)-1)
    song = os.path.join(music_dir, songs[a])
    sp.Popen(["start", "", song], shell=True)
    return "Playing music..."

def open_youtube():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    automation_log.append(f"{datetime.now()}: YouTube opened")
    return "YouTube opened successfully!"

def play_spotify():
    sp.run("start spotify:", shell=True)
    time.sleep(5)
    pyautogui.press('space')
    automation_log.append(f"{datetime.now()}: Spotify started")
    return "Playing Spotify..."

def system_shutdown():
    """Shutdown the computer after 1 minute"""
    sp.run(["shutdown", "/s", "/t", "60"])
    return "System will shutdown in 1 minute (use 'shutdown /a' to abort)"

def open_calculator():
    sp.Popen("calc.exe")
    return "Calculator opened"

def open_notepad(text):
    """Open Notepad and write provided text"""
    try:
        # Open Notepad
        sp.Popen("notepad.exe")
        automation_log.append(f"{datetime.now()}: Notepad opened")
        
        # Wait for Notepad to open
        time.sleep(2)
        
        # Type the text if provided
        if text.strip():
            pyautogui.typewrite(text)
            automation_log.append(f"{datetime.now()}: Wrote text in Notepad")
            return "Notepad opened with text successfully!"
        else:
            return "Notepad opened (no text provided)"
        
    except Exception as e:
        return "Failed to open Notepad"

def open_meet():
    driver = webdriver.Chrome()
    driver.get("https://meet.google.com")
    return "Google Meet opened"

def open_folder(path):
    """Open specific folder in File Explorer"""
    try:
        os.startfile(path)
        return f"Opened folder: {path}"
    except Exception as e:
        return f"Error opening folder: {str(e)}"

def custom_website(url):
    """Open any website using Chrome"""
    try:
        sp.run(f"start chrome {url}", shell=True)
        return f"Opened {url}"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_command(query):
    """Command handler with improved error handling"""
    response = ""
    if not query:
        return "No command detected"
    
    try:
        query = query.lower()
            
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            response = f"According to Wikipedia:\n{results}"
            speak(results)
            time.sleep(2)

        elif 'search' in query and 'google' in query:
            query = query.replace("search", "").replace("in google", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            response = f"Searching Google for {query}"

        elif 'open chrome' in query:
            sp.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            response = f"User Said - {query} : Opening Chrome..."

        elif 'play music' in query:
            response = playmusic()

        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")    
            response = f"Current time: {strTime}"
            speak(f"Sir, the time is {strTime}")
            time.sleep(2)

        elif 'open whatsapp' in query:
            sp.run("start whatsapp:", shell=True)
            response = f"User Said - {query} : Opening WhatsApp..."

        elif 'open calculator' in query:
            return open_calculator()
        
        elif 'shutdown' in query:
            return system_shutdown()

        else:
            response = f"User Said - {query} : Command not recognized"
            
    except Exception as e:
        response = f"Error processing command"
    
    return response

# ======================
# Gradio UI Implementation
# ======================

with gr.Blocks(title="JARVIS Assistant") as ui:
    gr.Markdown("# 🤖 JARVIS Voice Assistant")
    
    with gr.Tab("Voice Control"):
        with gr.Row():
            audio_input = gr.Audio(
                sources="microphone",
                type="filepath",
                label="Speak Now",
                elem_id="mic_input",
                interactive=True
            )
            process_btn = gr.Button("Process Command", variant="primary")
        with gr.Row():
            output_text = gr.Textbox(label="Command Response", interactive=False)
            sentiment_output = gr.Textbox(label="Sentiment Analysis", interactive=False)
    
    with gr.Tab("Automation Controls"):
        gr.Markdown("### Quick Access Panel")
        with gr.Row():
            gr.Button("🎵 Play Spotify").click(
                fn=play_spotify,
                outputs=gr.Textbox(label="Status", value="Playing Spotify...")
            )
            gr.Button("▶️ Open YouTube").click(
                fn=open_youtube,
                outputs=gr.Textbox(label="Status", value="Opening YouTube...")
            )
            gr.Button("🎶 Random Music").click(
                fn=playmusic,
                outputs=gr.Textbox(label="Status", value="Playing random music...")
            )
        
        with gr.Row():
            gr.Button("🖥️ System Shutdown").click(
                fn=system_shutdown,
                outputs=gr.Textbox(label="Status")
            )
            with gr.Column():
                notepad_text = gr.Textbox(
                    label="Notepad Content",
                    placeholder="Enter text to write in Notepad...",
                    lines=3
                )
                gr.Button("📝 Open Notepad with Text").click(
                    fn=open_notepad,
                    inputs=notepad_text,
                    outputs=gr.Textbox(label="Status")
                )
            gr.Button("🧮 Calculator").click(
                fn=open_calculator,
                outputs=gr.Textbox(label="Status")
            )
        
        # Web Automation
        with gr.Row():
            gr.Button("📅 Google Meet").click(
                fn=open_meet,
                outputs=gr.Textbox(label="Status")
            )
            gr.Button("📁 Open Music Folder").click(
                fn=lambda: open_folder(r"Music"),
                outputs=gr.Textbox(label="Status")
            )
        
        # Custom Command Section
        with gr.Row():
            custom_url = gr.Textbox(
                placeholder="Enter website URL",
                label="Custom Web Command"
            )
            gr.Button("🌐 Open Custom Site").click(
                fn=custom_website,
                inputs=custom_url,
                outputs=gr.Textbox(label="Status")
            )
    
    with gr.Tab("Email"):
        gr.Markdown("## Send Email")
        with gr.Row():
            email_to = gr.Textbox(label="Recipient Email")
            email_content = gr.Textbox(label="Message Content", lines=4)
        email_status = gr.Textbox(label="Email Status", interactive=False)
        email_btn = gr.Button("Send Email", variant="primary")

    def send_email_ui(to, content):
        success, message = sendEmail(to, content)
        return message

    email_btn.click(
        fn=send_email_ui,
        inputs=[email_to, email_content],
        outputs=email_status
    )
    
    with gr.Tab("System Logs"):
        log_display = gr.Textbox(label="Activity Log", lines=15, interactive=False)

    def process_audio(audio_path):
        """Audio processing pipeline"""
        try:
            if not audio_path:
                return "No audio detected", "", ""
            
            r = sr.Recognizer()
            with sr.AudioFile(audio_path) as source:
                audio = r.record(source)
            query = r.recognize_google(audio).lower()
            
            response = handle_command(query)
            sentiment = analyze_sentiment(query)
            automation_log.append(f"{datetime.now()}: {query}")
            
            return response, sentiment, "\n".join(automation_log[-10:])
        
        except sr.UnknownValueError:
            return "Could not understand audio", "", "\n".join(automation_log[-10:])
        except Exception as e:
            return f"Error: {str(e)}", "", "\n".join(automation_log[-10:])

    process_btn.click(
        fn=process_audio,
        inputs=[audio_input],
        outputs=[output_text, sentiment_output, log_display]
    ).then(
        fn=clear_audio,
        outputs=[audio_input]
    )

# Start background listener
threading.Thread(target=background_listener, daemon=True).start()

if __name__ == "__main__":
    wishMe()
    ui.launch(show_error=True)
