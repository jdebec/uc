# =============================================================================
# pyttsx3 (relies on microsoft Speech service)
# =============================================================================
import pyttsx3 as pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
for voice in voices:
    print(voice.id, voice.age, voice.gender, voice.languages, voice.name)
    engine.setProperty('voice', voice.id)
    engine.setProperty('rate', rate - 75)
    engine.say('The quick brown fox jumped over the lazy dog.')
engine.setProperty('rate', rate)
engine.runAndWait()



# =============================================================================
# try with long text
# pronunciation not great :/
# =============================================================================
txt = """India Fights Diabetic Blindness With Help From A.I.
 A technician screening a patient at the Aravind Eye 
 Hospital in Madurai, India. The hospital is using a 
 Google system that relies on artificial intelligence to 
 diagnose a retinal problem from such a scan"""
 
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 75)
engine.say(txt)
engine.runAndWait()

# =============================================================================
# try in french? 
# not working, need download add ressource :/
# =============================================================================
#engine = pyttsx.init()
#voices = engine.getProperty('voices')[0]
#engine.setProperty('voice', voice.id)
#
#engine.say('Je lui ai dit, fait gaffe a ton nez') # perfect
#
#engine.say(u'Tu as bien mangé?') # it works!!
#
#engine.runAndWait()   