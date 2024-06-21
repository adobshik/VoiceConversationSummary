# Voice Conversation Summary

## Overview

This repository contains scripts to summarize voice conversations stored in an audio format (mp3, wav, m4a, etc.) into SOAP (Subjective, Objective, Assessment, Plan) notes format using opensource speaker diarization model, OpenAI's Whisper and GPT-4 model via API.

## Features

Input: recording of dialogue stored in audio format (mp3, wav, m4a, etc.)

Output: summary in SOAP format (*Subjective*: Reason for appointment, Chief complaint
*Objective*: Findings from radiographs or any other tests, Medical History Updates
*Assessment*: Summary of findings
*Plan*: Completed treatment, home care instruction, and next steps)

## Getting Started
1. Clone repository:

```python
git clone https://github.com/adobshik/VoiceConversationSummary.git
cd VoiceConversationSummary
```
2. Install dependencies:
```python
pip install -r requirements.txt
```

3. Set up OpenAI API Key:

Obtain your OpenAI API key from OpenAI. Set it directly in the config.py script.

4. Run the test.ipynb to get SOAP summarization of your audio.
