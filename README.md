# AI shorts generator

Dette er et værktøj til generering af videoer, der skaber video shorts (reels eller shorts) ved hjælp af scripts genereret af GPT-4, indtalt af Elevenlabs tale syntese eller OpenAIs tekst-til-tale, mens DALL-E 3 genererer baggrundsbilleder, som sammensættes af OpenCV til en Short.

Der er mulighed for at bruge open source LLM'er som Mistral-7b og open source stable diffusion modeller, men dette kræver adgang til GPU ressourcer, og er derfor undladt for simplhedens skyld. (ihvertfald i første omgang)

## Rettigheder
Dette kode repo er under MIT-license og kan derfor bruges frit af enhver der skulle have lyst men der gives ingen garantier og softwaren kan bruges 'as is' og MainAI tager ingen ansvar for det indhold du bruger denne software til at producere eller måtte komme i problemer med ophavsrettigheder for at genere.

## Quick Start


1. **Klon repo**  
   ```
   git clone https://github.com/MainAIdk/ai-short-video-generator
   ```

2. **Naviger til folder**  
   ```
   cd ai-shorts
   ```

3. **Installer et virtuelt miljø**  

   ```
   python -m venv myvenv
   ```

4. **Start miljøet**
Skriv dette i din terminal
   ```
   myvenv\Scripts\activate
   ```

4. **Installer requirements i dit miljø**  

   ```
   pip install -r requirements.txt
   ```
5. **Sæt miljøvariabler**  

   ```
   Åben .env copy og indsæt dine api keys derefter slet copy så navnet på filen er .env
   ```

6. **Opret txt fil til GPT**
Opret en fil og kald den eksempelvis
    ```
    source.txt
    ```

7. **instruere GPT i din source fil**
Skriv i din source.txt hvad din short skal omhandle
    ```
    En short video omkring delfiner om hvor højt de kan springe i forhold til mennesker.
    ```

8. **Genere din short video**

    ```
    main.py source.txt
    ```
    Og vent på scriptet genere din video.
    Det skulle gerne se sådan her ud i din terminal
    ```console
    main.py source.txt
    Genererer manuskript...
    Genererer fortælling...
    Genererer billeder...
    Genererer video...
    FÆRDIG! Her er din video: shorts/1701788183/short.avi
    ``````
