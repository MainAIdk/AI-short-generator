# AI shorts generator

Dette er et værktøj til generering af videoer, som skaber video shorts (reels eller shorts) ved hjælp af scripts genereret af GPT-4, indtalt af Elevenlabs tale syntese eller OpenAIs tekst-til-tale, mens DALL-E 3 genererer baggrundsbilleder, som sammensættes af OpenCV til en Short.

Der er mulighed for at bruge open-source LLM'er som Mistral-7b og open-source stable diffusion modeller, men dette kræver adgang til GPU-ressourcer og er derfor undladt for enkelhedens skyld (i hvert fald i første omgang).

## Rettigheder
Dette kode-repositorium er under MIT-licensen og kan derfor bruges frit af enhver, der måtte ønske det. Der gives dog ingen garantier, og softwaren leveres 'as is'. MainAI påtager sig intet ansvar for det indhold, du bruger denne software til at producere, eller de eventuelle ophavsretlige problemer, der kan opstå ved generering af kopi-indholdet.

## Hurtig start


1. **Klon Repositoriet**  
   ```
   git clone https://github.com/MainAIdk/ai-short-video-generator
   ```

2. **Naviger til Mappen**  
   ```
   cd ai-shorts
   ```

3. **Installer et Virtuelt Miljø**  

   ```
   python -m venv myvenv
   ```

4. **Aktiver Miljøet**
Skriv dette i din terminal
   ```
   myvenv\Scripts\activate
   ```

5. **Installer Kravene i Dit Miljø**  

   ```
   pip install -r requirements.txt
   ```
6. **Sæt Miljøvariabler**  

   ```
   Åbn .env copy og indsæt dine API-nøgler. Slet derefter 'copy', så filnavnet bliver .env.
   ```

7. **Opret en Tekstfil til GPT**
Opret en fil og navngiv den, eksempelvis:
    ```
    source.txt
    ```

8. **Instruer GPT i Din Source-Fil**
Skriv i din source.txt, hvad din short skal omhandle, for eksempel:
    ```
    En short video omkring delfiner og hvor højt de kan springe i forhold til mennesker.
    ```

9. **Generer din short video**

    ```
    main.py source.txt
    ```
    Vent på, at scriptet genererer din video.
    Processen skulle gerne se sådan ud i din terminal:
    ```console
    main.py source.txt
    Genererer manuskript...
    Genererer fortælling...
    Genererer billeder...
    Genererer video...
    FÆRDIG! Her er din video: shorts/1701788183/short.avi
    ``````
