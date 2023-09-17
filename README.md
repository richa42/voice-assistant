# Virtual Assistant

A virtual assistant is a software program designed to provide assistance and perform tasks for users based on natural language input, often through speech recognition and text-to-speech capabilities. It aims to simulate human interaction to enhance user experience and productivity.

In the provided code, a virtual assistant is implemented in Python using various libraries:

1. **Speech Recognition (using `speech_recognition`)**:
   The virtual assistant listens to the user's speech input through the microphone and utilizes the `speech_recognition` library to convert the speech into text, enabling the assistant to understand and process the user's commands.

2. **Text-to-Speech (using `pyttsx3`)**:
   The assistant is capable of responding to the user by converting text into speech using the `pyttsx3` library. This allows the assistant to communicate with the user in a natural and audible manner.

3. **Weather Information Retrieval (web scraping)**:
   The assistant can fetch current weather information for a specified location using web scraping. It uses the `requests` and `BeautifulSoup` libraries to scrape weather data from a weather website, providing the user with real-time weather updates.

4. **Web Search Functionalities**:
   The assistant can perform web searches on Wikipedia, YouTube, Google, and Stack Overflow based on user queries. It uses predefined triggers to initiate these searches and opens the respective websites in the default web browser.

5. **System Actions (shutdown, restart, log off)**:
   The assistant can perform system actions such as shutting down, restarting, or logging off the computer. It uses the `os` module to execute system commands based on user input.

The virtual assistant follows a simple interaction flow:
- It greets the user based on the time of day.
- It listens to the user's voice commands.
- It processes the commands to determine the desired action.
- It executes the corresponding action, such as fetching information, performing web searches, or triggering system actions.

Users can interact with the virtual assistant by speaking commands, and the assistant responds accordingly, providing a useful and interactive experience.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

This project demonstrates the implementation of a virtual assistant using various Python libraries.

## Features

- Speech recognition using the `speech_recognition` library.
- Text-to-speech using the `pyttsx3` library.
- Weather information retrieval using web scraping.
- Web search functionalities.
- System actions (shutdown, restart, log off).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/richa42/voice-assistant.git
   cd VirtualAssistant
   ```

2. Install the required packages:
   ```bash
   pip install pyttsx3 speech_recognition wikipedia beautifulsoup4
   ```

## Usage

1. Run the `virtual_assistant.py` script:
   ```bash
   python3 main.py
   ```

2. Follow the instructions provided by the virtual assistant.

## Contributing

Contributions to this project are welcome. Feel free to open an issue or submit a pull request.

