# AI Shorts Generator

AI Shorts Generator is an innovative tool designed to create short videos. The tool utilizes scripts powered by GPT-4 and voices by either Elevenlabs' speech synthesis or OpenAI's text-to-speech. DALL-E 3 generates background images which are carefully assembled by OpenCV, culminating into a compelling short video or reel.

The tool offers an option to use open-source language models like Mistral-7b and open-source stable diffusion models, but this requires access to significant GPU resources.

## License

This code is released under the MIT license, implying it's free to be used by anyone. Nevertheless, it comes with no warranties and is provided 'as is'. The responsibility for the content you generate using this software, including potential copyright issues, rests solely with you. 

## Getting Started

Getting started with AI Shorts Generator involves a few expenses, primarily for generating images via DALL-E 3. Anticipate spending approximately $0.10-0.45 in OpenAI credits per video.

You will initially need an OpenAI API key and an Elevenlabs key (which may not be immediately necessary, but will be after generating a few videos).

* Obtain an OpenAI API key [here](https://platform.openai.com/api-keys)
* Get an Elevenlabs API key [here](https://elevenlabs.io/speech-synthesis) (not immediately necessary)

### Installation and Usage

Here are the steps to install and use the AI Shorts Generator:

1. **Clone the Repository**  
```
git clone https://github.com/MainAIdk/AI-Shorts-Generator.git
```
2. **Navigate to the Directory**
```
cd AI-Shorts-Generator
```
3. **Setup a Python Virtual Environment**
```
python -m venv myvenv
```
4. **Activate the Environment**
```
source myvenv/bin/activate
```
5. **Install Required Packages**
```
pip install -r requirements.txt
```
6. **Set Environment Variables**
```
Open .env copy, insert your API keys and rename to .env.
```
7. **Create GPT Input File**
```
Create a file (e.g. source.txt) and provide a brief about your short video.
```
8. **Generate Your Short Video**
```
python main.py source.txt
```
The script will generate your video. A successful operation should output:  
```console
Generating script...
Generating narration...
Generating images...
Generating video...

FINISHED! Here is your video: shorts/1701788183/short.avi
```

## Need Assistance?

If you need help setting up this project or require assistance for your personal or company's AI project, we are just an email away. Reach us at contact@mainai.dk. Happy Generating!
