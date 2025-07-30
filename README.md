# My-personal-Assistant

# 🧠 My Personal Assistant (JARVIS-like Project)

This is a **Java-based desktop personal assistant** inspired by **Iron Man's JARVIS**. It uses voice commands to perform tasks like opening applications, speaking responses, and more — making your computer feel intelligent and interactive.

---

## 🚀 Features

- 🎤 Voice recognition and command execution
- 🗣️ Speech output using text-to-speech
- 📂 Opens apps like Chrome, Notepad, VS Code, etc.
- 🧠 Responds like a personal assistant
- 💬 Conversational command handling
- 🎛️ Cross-platform support (Windows focus)
- ✅ Simple, fast, and effective

---

## 🛠️ Technologies Used

- Java (Core)
- Java AWT / Swing (optional for GUI)
- **Text-to-Speech** API (e.g., FreeTTS or pyttsx3 via Jython)
- **Speech Recognition** using voice input
- File and Process handling
- (Optional) Python integration for advanced voice tools

---

## 📁 Project Structure

```

My-personal-Assistant/
├── src/
│   └── assistant/
│       ├── Main.java
│       ├── VoiceCommandProcessor.java
│       ├── SystemCommandHandler.java
│       └── TextToSpeechEngine.java
├── resources/
│   └── sounds/
├── README.md
└── ...

````

---

## ▶️ How to Run

### 🔧 Prerequisites
- Java 11+ installed
- (Optional) Python 3.9+ if using Jython or pyttsx3
- Microphone for voice input
- Speaker for assistant voice output

### 🔨 Steps

```bash
# 1. Clone the project
git clone https://github.com/trivedisahil91/My-personal-Assistant.git
cd My-personal-Assistant

# 2. Compile and run
javac -d bin src/assistant/*.java
java -cp bin assistant.Main
````

🎤 Now, speak to your assistant!

---

## 🧪 Example Commands

* “Open Chrome”
* “What’s the time?”
* “Open Notepad”
* “Shut down system” (careful!)
* “Tell me a joke”

---

## 💡 Future Improvements

* GUI Interface for better control
* Integration with OpenAI or ChatGPT API
* Calendar and Reminder functionalities
* Email and Weather services
* Wake word detection ("Hey Jarvis")

---

## 🙋‍♂️ Author

**Sahil Trivedi**
🔗 [LinkedIn Profile](https://www.linkedin.com/in/trivedi-sahil-5212002b0)

---


