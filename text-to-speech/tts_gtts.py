# =============================================================================
# gTTS (google API, Internet connexion required)
# =============================================================================
from gtts import gTTS
import vlc

#create 2 hellos, in english and french
tts_en = gTTS(text='Good morning', lang='en')
tts_fr = gTTS('bonjour', lang='fr')

#save them on on mp3 file
with open('hello_bonjour.mp3', 'wb') as f:
    tts_en.write_to_fp(f)
    tts_fr.write_to_fp(f)
    
#play with vlc
p = vlc.MediaPlayer("hello_bonjour.mp3")
p.play()


# =============================================================================
# long text, checking pronunciation
# Google API limits to 100 cars, chunking automatically
# =============================================================================

text = """DÉCRYPTAGE - Les jusqu'au-boutistes du Brexit s'apprêtent à refuser 
        une nouvelle fois d'entériner l'accord signé entre Theresa May et les
        Européens."""

#chunking text for short chunks (Google API < 100 cars)
def split_length(text, max_length):
    return [text[i:i+max_length] + '|' for i in range(0, len(text), max_length)]
    
goo_api_cars_limit = 100
chunked_text = split_length(text.replace('\n', ' '), goo_api_cars_limit)
print(chunked_text)

##chunking text for grammar separator (, . ...)        
#def split_grammar(text, seps):
#    default_sep = seps[0]
#    for sep in seps[1:]:
#            text = text.replace(sep, default_sep)
#    return [chunk.strip() for chunk in text.split(default_sep)]

#seps = [',', '\n', '.', ' - ']
#chunked_text = split_grammar(, seps)
#print(chunked_text)

#chunked_text = [item for sublist in chunked_text for item in sublist]
#print(chunked_text)

chunked_text = [gTTS(entry, lang='fr') for entry in chunked_text if 
                entry != '']

with open('hello_bonjour.mp3', 'wb') as f:
    for chunk in chunked_text:
        chunk.write_to_fp(f)
p = vlc.MediaPlayer("hello_bonjour.mp3")
p.play()        
    