# Denne software er under MIT license
# Og kan derfor benyttes frit af enhver.
# Lavet af Mads Andersen @ MainAI
# Stjerne modtages med kyshånd

from openai import OpenAI
import time
import json
import sys
import os

import narration
import images
import video
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Fetch API keys from environment
elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')


# Initialize the OpenAI client with the API key
client = OpenAI(api_key=openai_api_key)

if len(sys.argv) < 2:
    print(f"USAGE: {sys.argv[0]} SOURCE_FILENAME")
    sys.exit(1)

with open(sys.argv[1]) as f:
    source_material = f.read()

short_id = str(int(time.time()))
output_file = "short.avi"

basedir = os.path.join("shorts", short_id)
if not os.path.exists(basedir):
    os.makedirs(basedir)

print("Genererer manuskript..")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": """You are a YouTube short narration generator. You generate 30 seconds to 1 minute of narration. The shorts you create have a background that fades from image to image as the narration is going on.

You will need to generate descriptions of images for each of the sentences in the short. They will be passed to an AI image generator. DO NOT IN ANY CIRCUMSTANCES use names of celebrities or people in the image descriptions. It is illegal to generate images of celebrities. Only describe persons without their names. Do not reference any real person or group in the image descriptions. Don't mention the female figure or other sexual content in the images because they are not allowed.

You are however allowed to use any content, including real names in the narration. Only image descriptions are restricted.

Note that the narration will be fed into a text-to-speech engine, so don't use special characters.

DO NOT generate any image describtions of anything that violates the image generation saftey systems.

Respond with a pair of an image description in square brackets and a narration below it. Both of them should be on their own lines, as follows:

###

[Description of a background image]

Narrator: "One sentence of narration"

[Description of a background image]

Narrator: "One sentence of narration"

[Description of a background image]

Narrator: "One sentence of narration"

###

The short should be 6 sentences maximum.

You should add a description of a fitting, beautiful and captivating background image in between all of the narrations. It will later be used to generate an image with AI. Avoid images with letters and sign.
"""
        },
        {
            "role": "user",
            "content": f"Create a YouTube short narration based on the following source material:\n\n{source_material}"
        }
    ]
)

response_text = response.choices[0].message.content
response_text.replace("’", "'").replace("`", "'").replace("…", "...").replace("“", '"').replace("”", '"')

with open(os.path.join(basedir, "response.txt"), "w") as f:
    f.write(response_text)

data, narrations = narration.parse(response_text)
with open(os.path.join(basedir, "data.json"), "w") as f:
    json.dump(data, f, ensure_ascii=False)

print(f"Genererer fortælling....")
narration.create(data, os.path.join(basedir, "narrations"))

print("Genererer billeder...")
images.create_from_data(data, os.path.join(basedir, "images"))

print("Genererer video...")
video.create(narrations, basedir, output_file)

print(f"FÆRDIG! Her er din video: {os.path.join(basedir, output_file)}")
