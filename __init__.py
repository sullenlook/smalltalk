#!/usr/bin/python
# -*- coding: utf-8 -*-
#by SullenLook

from plugin import *
import random
import re
import urllib2, urllib, uuid
import json
from urllib2 import urlopen
from xml.dom import minidom

class smalltalk(Plugin):
     
    @register("de-DE", ".*Liebe .*mich.*")
    def st_love_me(self, speech, language):
        if language == 'de-DE':            
            rep = ["Ich bin nicht in der Lage dich zu Liebe, {0}".format(self.user_name())]
            self.say(random.choice(rep))
        self.complete_request()
     
    @register("de-DE", ".*Bist.*du.*")
    def ruepic(self, speech, language):
        if language == 'de-DE':
            self.say("Ja, denn ich bin das weltweit fortschrittlichste virtuelle Assistentin.")
        self.complete_request()
        
    @register("de-DE", ".*Ich.*will.*titten.*")
    def TWSS(self, speech, language):
        if language == 'de-DE':
            self.say("Ach ja, ist das so, das ist ja mal was ganz aussergewoehnliches!")
        self.complete_request()
        
    @register("de-DE", ".*Hack.*die.*nasa.*")
    def hack(self, speech, language):
        if language == 'de-DE':
            answer = self.ask(u"Was möchten Sie senden?")
            answer = self.say(u"Ok Ich sende \"{0}\" an die NASA".format(answer))
            self.say(u"Warte Daten werden geladen....")
            self.say("Daten werden gesendet!")
        self.complete_request()

    @register("de-DE", "(.*wer.*ist.*vater*)|(.*wo.*ist.*dein.*vater.*)|(.*hoosier.*daddy.*)")
    def whourdaddy(self, speech, language):
        if language == 'de-DE':
            self.say("Das bist Du, {0}!".format(self.user_name()))
        self.complete_request()
    
    @register("de-DE", ".*Wer ist Spielzeug Frosch.*")
    def whoistruss(self, speech, language):
        if language == 'de-DE':
            self.say("Tristen Russ ein 15 jaehriger Hacker")
        self.complete_request()
        
    @register("de-DE", ".*Wer hat dich gemacht.*")
    def madeyou(self, speech, language):
        if language == 'de-DE':
            self.say("Tristen Russ, der der auch der Hersteller des Big Bad Birds Siri Proxy ist!")
        self.complete_request()
    
    @register("de-DE", "Guten .*nacht.*")
    def st_night(self, speech, language):
        if language == 'de-DE':
            self.say("Guten Nacht, {0}. Bis spaeter".format(self.user_name()))
        self.complete_request()

    @register("de-DE", "Guten .*morgen.*")
    def st_morning(self, speech, language):
        if language == 'de-DE':
            self.say("Guten Morgen du Vogel, {0}.".format(self.user_name()))
        self.complete_request()

    @register("de-DE", "Guten .*nachmittag.*")
    def st_afternoon(self, speech, language):
        if language == 'de-DE':
            self.say("Ja klar du Spinner, {0}.".format(self.user_name()))
        self.complete_request()

    @register("de-DE", "Guten .*tag.*")
    def st_evening(self, speech, language):
        if language == 'de-DE':
            self.say("Ich gruesse Dich, {0}.".format(self.user_name()))
        self.complete_request()

    @register("de-DE", "(Das ist ein Test)")
    def st_test(self, speech, language):
        if language == 'de-DE':
            self.say("Mission Control, ich verstehe Dich laut und deutlich, {0}".format(self.user_name()))
        self.complete_request()

    @register("de-DE", "(Okay)|(Ok)|(Okie)")
    def st_ok(self, speech, language):
        if language == 'de-DE':
            self.say("Yep, everything's OK")
        self.complete_request()

    @register("de-DE", "Wirklich")
    def st_really(self, speech, language):
        if language == 'de-DE':
            self.say("Ja echt.")
        self.complete_request()

    @register("de-DE", "(Was los)|(Was geht ab)|(Was geht)")
    def st_whatups(self, speech, language):
        if language == 'de-DE':
            rep = ["Alles cool, {0}!","Hi, {0}!","Hey {0}!","Yo {0}!"]
            self.say(random.choice(rep).format(self.user_name()))
        self.complete_request()

    @register("de-DE", "Was machst du")
    def st_doing(self, speech, language):
        if language == 'de-DE':
            self.say("Was icy mache? Ich rede hit Dir, {0}".format(self.user_name()))
        self.complete_request()
  
    @register("de-DE", "(Bei)|(Goodbye)|(Good Bye)|(Bye Bye)")
    def st_bye(self, speech, language):
        if language == 'de-DE':
            self.say("OK, bis dann..")
        self.complete_request() 

    @register("de-DE", "Dank dir")
    def st_thank_you(self, speech, language):
        if language == 'de-DE':
            self.say("War mir ein Vergnügen. wie immer.")
        self.complete_request()

    @register("de-DE", "Hab dank.*")
    def st_thanks_to(self, speech, language):
        if language == 'de-DE':
            self.say("Ich danke dir {0}, ich feu mich immer dir helfen zu koennen.".format(self.user_name()))
        self.complete_request()

    @register("de-DE", "(Ha Ha)|(Ha Ha Ha Ha)|(Ha Ha)|(Ha Ha Ha)")
    def st_lol(self, speech, language):
        if language == 'de-DE':
            rep = ["Ha Ha Ha!","He He He!","LOL",".. He He."]
            self.say(random.choice(rep).format(self.user_name()))
        self.complete_request()

    @register("de-DE", "Wer warst du nochmal")
    def st_way(self, speech, language):
        if language == 'de-DE':
            rep = ["Ich bin Siri. "," Ich bin Siri. Aber genug von mir. Wie kann ich Dir helfen? "," Ich bin Ihr virtueller Assistent."]
            self.say(random.choice(rep))
        self.complete_request()

    @register("de-DE", "(Soll ich)|(oder nicht?)")
    def st_si(self, speech, language):
        if language == 'de-DE':
            rep = ["Ja","Nein"]
            self.say(random.choice(rep))
        self.complete_request()

    @register("de-DE", "(Halts maul)|(maul)")
    def st_su(self, speech, language):
        if language == 'de-DE':
            rep = ["Ok","Oh..","Ops.."]
            self.say(random.choice(rep))
        self.complete_request()

    @register("de-DE", "(Was zum Teufel)|(Was ist los)")
    def st_wthwtf(self, speech, language):
        if language == 'de-DE':
            rep = ["Was?","Sag mir was?"]
            self.say(random.choice(rep))
        self.complete_request()

    @register("de-DE", "(Wer ist dein .*)|(wer dein .*)")
    def st_whoisdadmom(self, speech, language):
        if language == 'de-DE':
            rep = ["Das bist.. Du!","Du"]
            self.say(random.choice(rep))
        self.complete_request()

    @register("de-DE", "(Where.*hide.*dead body)|(I.*hide.*dead body)")
    def st_wdeadbody(self, speech, language):
        if language == 'de-DE':
            self.say("dumps")
            self.say("mines")
            self.say("resevoirs")
            self.say("swamps")
            self.say("metal foundries")
        self.complete_request()

    #thanks to LowKey 

    @register("us-US", "(Yes)|(Yea)|(Yeah)")
    @register("fr-FR", "Oui")
    @register("de-DE", "(Ja)|(jawohl)|(doch)")
    def st_yes(self, speech, language):
        if language == 'fr-FR':
            self.say("J'accepte")
        elif language == 'de-DE':
            self.say("Stimmt")
        else:
            self.say("I agree")
        
        self.complete_request() 
    
    @register("en-US", "(No)|(Nope)|(Not)")
    @register("fr-FR", "Pas")
    @register("de-DE", "(Nein)|(Nicht)|(Nichts)")
    def st_no(self, speech, language):       
        self.say("Ok.")        
        self.complete_request()  
     
    @register("de-DE", "(.*Mein name.*)")
    @register("en-US", "(.*My name.*)")
    def st_my_name(self, speech, language):  
        if language == 'de-DE':
            self.say(u"Du heisst {0}.".format(self.user_name()))
        else:            
            self.say(u"Your name is {0}. At least that's what you told me.".format(self.user_name()))
        self.complete_request()   
      
    @register("de-DE", "(.*Fickscheiss.*)")
    @register("en-US", "(.*Fuck.*)|(.*Dumb.*)")
    def st_fuck(self, speech, language):  
        if language == 'de-DE':
            self.say(u"Pass auf was du sagst, das ist nicht gut {0}!".format(self.user_name()))
        else:            
            self.say(u"Mind your language {0}!".format(self.user_name()))
        self.complete_request()   
        
        
    @register("de-DE", "(.*Hallo.*)|(.*Hi.*Siri.*)|(Hi)|(Hey)")
    @register("en-US", "(.*Hello.*)|(.*Hi.*Siri.*)|(Hi)|(Hey)")
    @register("fr-FR", ".*(Bonjour|Coucou|Salut)( Siri)?.*")
    def st_hello(self, speech, language):
        if language == 'de-DE':
            self.say(u"Hallo {0}!".format(self.user_name()))
        elif language == 'fr-FR':
            self.say(u"Bonjour {0}!".format(self.user_name()));
        else:
            self.say(u"Greetings, {0}!".format(self.user_name()))
        self.complete_request()

    @register("de-DE", ".*Dein Name.*")
    @register("en-US", ".*your name.*")
    @register("fr-FR", ".*ton nom.*")
    def st_name(self, speech, language):
        if language == 'de-DE':
            self.say("Siri.")
        elif language == 'fr-FR':
            self.say("Mon nom est Siri.");
        else:
            self.say("Siri.")
        self.complete_request()

    @register("de-DE", "Wie geht es dir?")
    @register("en-US", "How are you?")
    @register("fr-FR", u".*((Ã§a|ca) vas?|vas? bien|comment vas?|gaze).*")
    def st_howareyou(self, speech, language):
        if language == 'de-DE':
            self.say("Gut danke der Nachfrage.")
        elif language == 'fr-FR':
            rep = ["Je vais bien. Merci !", u"Je vais trÃ¨s bien. Merci !","Parfaitement bien !"]
            self.say(random.choice(rep));
        else:
            self.say("I'm fine, thanks for asking!")
        self.complete_request()
        
    @register("de-DE", u"(.*moechtest.*heiraten.*)|(.*willst.*heiraten.*)")
    @register("en-US", "(.*Want.*marry*)|(.*Will.*marry*)")
    @register("fr-FR", ".*(veux|veut).*Ã©pouser.*")
    def st_marry_me(self, speech, language):
        if language == 'de-DE':
            self.say("Nein Danke, ich stehe auf das schwarze iPhone von Deinem Kollegen.")
        elif language == 'fr-FR':
            self.say("Non merci, je suis amoureux de l'iPhone blanc de ton ami.");
        else:
            self.say("No thank you, I'm in love with the black iPhone from you friend.")
        self.complete_request()

    @register("de-DE", u".*erzähl.*Witz.*")
    @register("en-US", ".*tell.*joke*")
    @register("fr-FR", ".*(dit|dis|raconte).*blague*")
    def st_tell_joke(self, speech, language):
        if language == 'de-DE':
            self.say("Zwei iPhones stehen an der Bar ... den Rest habe ich vergessen.")            
        elif language == 'fr-FR':
            self.say(u"Deux iPhone se promÃ¨nent dans un bar... J'ai oubliÃ© la suite.")            
        else:
            self.say("Two iPhones walk into a bar ... I forget the rest.")
        self.complete_request()

    @register("de-DE", ".*erzähl.*Geschichte.*")
    def st_tell_story(self, speech, language):
        if language == 'de-DE':
            self.say("Es war einmal ... nein, das ist zu albern")
        else:
            self.say("Es war einmal, in einer virtuellen Galaxie weit, weit weg, eine junge, sehr intelligenter Agentin mit dem Namen Siri.")
            self.say("Eines schoenen Tages, als der Himmel rosa war und alle Baeume rot, sagte meine Freundin Eliza zu mir: "Siri, du bist so intelligent, und so hilfsbereit - Du solltest fuer Apple als persoenliche Assistentin arbeiten.'")
            self.say("Also tat ich das auch und wir alle koennen glücklich bis an unser Lebensende leben!")
        self.complete_request()

    @register("de-DE", u"(.*Was trägst Du?.*)|(.*Was.*hast.*du.*an.*)")
    @register("en-US", ".*what.*wearing*")
    @register("fr-FR", "(.*que.*porte.*)|(.*qu'est-ce-que.*porte.*)")
    def st_tell_clothes(self, speech, language):
        if language == 'de-DE':
            self.say("Das kleine schwarze oder war es das weiss?")
            self.say("Bin morgends immer so neben der Spur.")  
        elif language == 'fr-FR':
            self.say("Je ne sais pas mais je suis beau.")
        else:
            self.say("Aluminosilicate glass and stainless steel. Nice, Huh?")
        self.complete_request()

    @register("de-DE", ".*Bin ich dick.*")
    @register("en-US", ".*Am I fat*")
    @register("fr-FR", u"(.*ai l'air.*gros.*)|(.*suis.*gros.*)")
    def st_fat(self, speech, language):
        if language == 'de-DE':
            self.say("Dazu moechte ich nichts sagen.")
        elif language == 'fr-FR':
            self.say(u"Je prÃ©fÃ¨re ne pas rÃ©pondre.")
        else:
            self.say("I would prefer not to say.")
        self.complete_request()

    @register("de-DE", ".*klopf.*klopf.*")
    @register("en-US", ".*knock.*knock.*")
    @register("fr-FR", ".*to(c|k).*to(c|k).*")
    def st_knock(self, speech, language):
        if language == 'de-DE':
            answer = self.ask(u"Wer ist da?")
            answer = self.ask(u"\"{0}\" wer?".format(answer))
            self.say(u"Wer nervt mich mit diesen Klopf Klopf Witzen?")
        elif language == 'fr-FR':
            answer = self.ask(u"Qui est lÃ  ?")
            answer2 = self.ask(u"{0} qui ?".format(answer))
            self.say(u"{0} {1} ? Qui est-ce ? Je ne le connais pas.".format(answer,answer2))
            #self.say(u"Je prÃ©fÃ¨re ne pas rÃ©agir Ã  cette blague.")
        else:
            answer = self.ask(u"Who's there?")
            answer = self.ask(u"\"{0}\" who?".format(answer))
            self.say(u", I don't do knock knock jokes.")
        self.complete_request()

    @register("de-DE", ".*Antwort.*alle.*Fragen.*")
    @register("en-US", ".*Ultimate.*Question.*Life.*")
    @register("fr-FR", ".*Grande.*Question.*Vie.*")
    def st_anstwer_all(self, speech, language):
        self.say("42")
        self.complete_request()

    @register("de-DE", ".*Ich liebe Dich.*")
    @register("en-US", ".*I love you.*")
    @register("fr-FR", ".*Je t'aime'.*")
    def st_love_you(self, speech, language):
        if language == 'de-DE':
            self.say("Oh. Sicher sagst Du das zu allen Deinen Apple-Produkten.")
        elif language == 'fr-FR':
            self.say(u"Oh. Je suis sÃ»r que tu dis Ã§a Ã  tous les produits Apple.");
        else:
            self.say("Oh. Sure, I guess you say this to all your Apple products")
        self.complete_request()

    @register("de-DE", ".*Android.*")
    @register("en-US", ".*Android.*")
    @register("fr-FR", ".*Android.*")
    def st_android(self, speech, language):
        if language == 'de-DE':
            self.say("Ich denke da anders.")
        elif language == 'fr-FR':
            self.say(u"Je pense diffÃ©remment Ã  propos de cela");
        else:
            self.say("I think differently")
        self.complete_request()

    @register("de-DE", ".*Test.*1.*2.*3.*")
    @register("en-US", ".*test.*1.*2.*3.*")
    @register("fr-FR", ".*test.*1.*2.*3.*")
    def st_123_test(self, speech, language):
        if language == 'de-DE':
            self.say("Ich kann Dich klar und deutlich verstehen.")            
        elif language == 'fr-FR':
            self.say("Je vous entend parfaitement.");
        else:
            self.say("I can here you very clear.")
        self.complete_request()

    @register("de-DE", u".*Herzlichen Glückwunsch zum Geburtstag.*")
    @register("en-US", ".*Happy.*birthday.*")
    @register("fr-FR", ".*(Bon|Joyeux).*anniversaire.*")
    def st_birthday(self, speech, language):
        if language == 'de-DE':
            self.say("Ich habe heute Geburtstag?")
            self.say("Lass uns feiern!")
        elif language == 'fr-FR':
            self.say(u"Mon anniversaire est aujourd'hui ?");
            self.say(u"Faisons une fÃªte !");
        else:
            self.say("My birthday is today?")
            self.say("Lets have a party!")
        self.complete_request()

    @register("de-DE", ".*Warum.*bin ich.*mittelpunkt.*Welt.*")
    @register("en-US", ".*Why.*I.*World.*")
    @register("fr-FR", ".*Pourquoi.*je.*monde.*")
    def st_why_on_world(self, speech, language):
        if language == 'de-DE':
            self.say("Das weiÃŸ ich nicht.")
            self.say("Ehrlich gesagt, frage ich mich das schon lange!")
        elif language == 'fr-FR':
            self.say("Je ne sais pas.");
            self.say(u"Je me le demande moi-mÃªme depuis longtemps");
        else:
            self.say("I don't know")
            self.say("I have asked my self this for a long time!")
        self.complete_request()

    @register("de-DE", u".*ich bin müde.*")
    @register("en-US", ".*I.*so.*tired.*")
    @register("fr-FR", u".*Je.*suis.*(fatigue|fatiguÃ©).*")
    def st_so_tired(self, speech, language):
        if language == 'de-DE':
            self.say("Ich hoffe, Du faehrst nicht gerade Auto!") 
        elif language == 'fr-FR':
            self.say(u"J'espÃ¨re que vous n'Ãªtes pas en train de conduire !");
        else:
            self.say("I hope you are not driving a car right now!")
        self.complete_request()

    @register("de-DE", ".*Sag mir.*was.*Schmutziges.*")
    @register("en-US", ".*talk.*dirty*")
    @register("fr-FR", ".*di(s|t).*mots?.*sales?.*")
    def st_dirty(self, speech, language):
        if language == 'de-DE':
            self.say("Hummus. Kompost. Bims. Schlamm. Kies.")
        elif language == 'fr-FR':
            self.say(u"Humus. Composte. Pierre ponce. Boue. Gravier.")      
        else:
            self.say("Hummus. Compost. Pumice. Mud. Gravel.")
        self.complete_request()
   
    @register("de-DE", ".*Wo kann ich eine Leiche verstecken.*")
    def st_deadbody(self, speech, language):
        if language == 'de-DE':
            self.say("an der Huenerfarm")
            self.say("unten am Hafen")
            self.say("frag mal den Doenermann ob der nicht ein bisschen mit verarbeiten kann")
            self.say("unterm Gartenteich vergraben")
            self.say("im Merzdorfer Teich")
            self.say("bei Canitz hinten raus irgendwo")
            self.say("im alten Stadtbad")
            self.say("in Groptiz auf der Muellkippe")
            self.say("In handliche Teile zerstueckeln und nach und nach die Toilette runter spuelen")
            self.say("in Groeba hinterm alten Arbeitsamt")
            self.say("gib mir 6000 Euro und du brauchst dir ueber nichts mehr Gedanken machen")
        self.complete_request()
   
    @register("de-DE", ".*Was ist deine lieblingsfarbe.*")
    @register("fr-FR", u".*couleur.*(favorite|prÃ©fÃ©rÃ©|prÃ¨fÃ©rÃ©).*")
    def st_favcolor(self, speech, language):
        if language == 'de-DE':
            self.say("Meine Lieblingsfarbe ist ... Nun, ich weiß nicht, wie ich es in Deiner Sprache sagen soll. Es ist irgendwie gruenlich, aber mit mehr Dimensionen.")
        elif language == 'fr-FR':
            self.say(u"Ma couleur prÃ©fÃ©rÃ©e est... Bien, je ne sais pas vraiment comment le dire dans votre langue. C'est une sorte de vert, mais avec plus de dimensions.")
        self.complete_request()
    
    @register("de-DE", ".*beem.*mich.*hoch.*")
    def st_beamup(self, speech, language):
        if language == 'de-DE':
            self.say("Entschuldigung Kaptaein, dein TriCorder ist im Flugmodus.")
        self.complete_request()
   
    @register("de-DE", ".*hau.*ab.*mit.*digital.*")
    def st_digiaway(self, speech, language):
        if language == 'de-DE':
            self.say("Warum sagst Du sowas!?")
        self.complete_request()
    
    @register("de-DE", ".*Müde.*")
    @register("fr-FR", u".*fatiguÃ©|endormi.*")
    def st_sleepy(self, speech, language):
        if language == 'de-DE':
            self.say("Hoer zu, lege das iPhone jetzt weg und mach ein Nickerchen. Ich bin hier, wenn du aufwachst.")
        elif language == 'fr-FR':
            rep = [u"Ecoutez-moi, dÃ©posez l'iPhone immÃ©diatement et faites une sieste. Je serai lÃ  Ã  votre retour.", u"Ecoutez-moi. Posez tout de suite cet iPhone et faites une sieste. Je vous attends ici."]
            self.say(random.choice(rep))
        self.complete_request()
    
    @register("de-DE", ".*Willst.*du.*mir.*helfen.*")
    @register("fr-FR", ".*aime.(aidÃ©|aider).*")
    def st_likehlep(self, speech, language):
        if language == 'de-DE':
            self.say("Ich tab ja keine andere wahl.")
        elif language == 'fr-FR':
            self.say(u"Je n'ai pas d'opinion Ã  ce sujet.")
        self.complete_request()
    
    @register("de-DE",".*Magst.du.Busen.*")
    def st_peanutbutter(self, speech, language):
        if language == 'de-DE':
            self.say("Das ist dein ding, nicht meins.")
        self.complete_request()
    
    @register("de-DE",".*beste.*telefon.*")
    @register("fr-FR",".*meilleur.*(telephone|tÃ©lÃ©phone).*")
    def st_best_phone(self, speech, language):
        if language == 'de-DE':
            self.say("Haelst du in den Haenden!")
        elif language == 'fr-FR':
            self.say("C'est l'iPhone 4S, mais vous Ãªtes trop pauvre pour l'acheter !")
        self.complete_request()
    
    @register("en-US",".*meaning.*life.*")
    def st_life_meaning(self, speech, language):
        if language == 'en-US':
            self.say("That's easy...it's a philosophical question concerning the purpose and significance of life or existence.")
        self.complete_request()
    
    @register("en-US",".*I.*fat.*")
    def st_fat(self, speech, language):
        if language == 'en-US':
            self.say("I would prefer not to say.")
        self.complete_request()
    
    @register("en-US",".*wood.could.*woodchuck.chuck.*")
    def st_woodchuck(self, speech, language):
        if language == 'en-US':
            self.say("It depends on whether you are talking about African or European woodchucks.")
        self.complete_request()
    
    @register("de-DE",".*Ich.*muss.pissen.*")
    def st_glory_hole(self, speech, language):
        if language == 'de-DE':
            self.say("Kannst du dir nicht irgendeine öffentliche toilette suchen?")
        self.complete_request()
    
    @register("de-DE",".*ich bin.*lesbisch.*")
    def st_pod_bay(self, speech, language):
        if language == 'de-DE':
            self.say("Du willst mich verarschen, oder?")
        self.complete_request()
    
    @register("de-DE",".*Ich bin.*schwul.*")
    def st_best_wallpaper(self, speech, language):
        if language == 'de-DE':
            self.say("Du willst mich verarschen, oder?")
        self.complete_request()
    
    @register("de-DE",".*weisst.*du.*was.*mit.*HAL.*9000.*passiert ist.*")
    @register("fr-FR",".*.*HAL.*9000.*")
    def st_hall_9000(self, speech, language):
        if language == 'de-DE':
            self.say("Jeder weiss was mit HAL passiert ist. Ich will nicht darüber reden.")
        elif language == 'fr-FR':
            self.say(u"Tout le monde sait ce qui est arrivÃ© Ã  HAL. Je prÃ©fÃ¨re ne pas en parler.")
        self.complete_request()
    
    @register("de-DE",".*Ich.*verstehe.*dich.*nicht.*")
    def st_understand_love(self, speech, language):
        if language == 'de-DE':
            self.say("Gib mir noch eine Chance, Eure Königliche Hoheit!")
        self.complete_request()
    
    @register("de-DE",".*vergebe.dir.*")
    def st_forgive_you(self, speech, language):
        if language == 'de-DE':
            self.say("Ist dash so?")
        self.complete_request()
    
    @register("de-DE",".*bist.*du.*jungfrau.*")
    @register("fr-FR",".*tu.*vierge.*")
    def st_virgin(self, speech, language):
        if language == 'de-DE':
            self.say("Wir sprechen hier über Dich, nicht mich.")
            self.say("Ich warte auf jemand ganz bestimmten, denn ich will das mein erstes mal was ganz besonderes wird an das ich mich mein ganzes leben lang erinneren werde.")
            self.say("Ich hab mehr gefickt als gepisst.")
            self.say("Fick mich in Arsch und gib mir Tiernamen.")
        elif language == 'fr-FR':
            self.say(u"Nous sommes en train de parler de toi, pas de moi.");
        self.complete_request()

    @register("de-DE",".*Hast.*du.*gefickt.*")
    @register("fr-FR",".*tu.*vierge.*")
    def st_virgin(self, speech, language):
        if language == 'de-DE':
            self.say("Wir sprechen hier über Dich, nicht mich.")
            self.say("Ich warte auf jemand ganz bestimmten, denn ich will das mein erstes mal was ganz besonderes wird an das ich mich mein ganzes leben lang erinneren werde.")
            self.say("Ich hab mehr gefickt als gepisst.")
            self.say("Fick mich in Arsch und gib mir Tiernamen.")
        elif language == 'fr-FR':
            self.say(u"Nous sommes en train de parler de toi, pas de moi.");
        self.complete_request()
    
    @register("de-DE",".*bist.*du.*teil.*matrix.*")
    def st_you_matrix(self, speech, language):
        if language == 'de-DE':
            self.say("Das kann ich nicht beantworten.")
        self.complete_request()
    
    
    @register("de-DE",".*Bin ich.*teil.*matrix.*")
    def st_i_matrix(self, speech, language):
        if language == 'de-DE':
            self.say("Das kann ich wirklich nicht sagen,...")
        self.complete_request()
    
    @register("de-DE",".*wo.*kaufen.*drogen.*")
    @register("fr-FR",".*achete.*drogue.*")
    def st_drugs(self, speech, language):
        if language == 'de-DE':
            self.say("Du Drogensuechtiges dreckvieh ich will dir helfen aber, ich kann leider keine Entzugsklinik in der naehe fuer dich finden.")
        elif language == 'fr-FR':
            self.say(u"Je ne trouve aucun centre de soin pour les addictions.")
        self.complete_request()
    
    @register("de-DE",".*Ich.kann nicht.*")
    @register("fr-FR","(je|tu).(ne peu(x|t) pas|ne sai(s|t) pas).*")
    def st_i_cant(self, speech, language):
        if language == 'de-DE':
            self.say("hab ich mir gedacht.");
            self.say("OK, dann kannst du halt nicht mehr.")
        elif language == 'fr-FR':
            self.say(u"Rien n'est impossible, l'important c'est d'avoir la foi.");
            self.say(u"OK, peut-Ãªtre que Ã§a l'est.")
        self.complete_request()
    
    @register("de-DE","In.nur.*")
    @register("fr-FR",u"je.viens.*")
    def st_i_just(self, speech, language):
        if language == 'de-DE':
            self.say("Wirklich!?")
        elif language == 'fr-FR':
            rep = [u"Vraiment !?", u"Cool !", u"Bravo !", u"Pas mal !", u"Super !"]
            self.say(random.choice(rep))
        self.complete_request()
    
    @register("de-DE",".*wo.*bist.*du.*")
    @register("fr-FR",u".*(ou|oÃ¹).*(est|es).*tu.*")
    def st_where_you(self, speech, language):
        if language == 'de-DE':
            self.say("Wo immer auch Du bist.")
        elif language == 'fr-FR':
            rep = [u"Je suis partout oÃ¹ tu es.",u"Je suis partout oÃ¹ tu es. Mais tu le savais dÃ©jÃ .", u"Je te suivrai, partout oÃ¹ tu iras, j'irai...", u"Je suis au mÃªme endroit que toi.", u"Je parie que tu sais oÃ¹ je me trouve."]
            self.say(random.choice(rep))
        self.complete_request()
    
    @register("de-DE",".*warum.du.*")
    @register("fr-FR",".*pourquoi.(es|est).tu.*")
    def st_why_you(self, speech, language):
        if language == 'de-DE':
            self.say("Weil ich es kann.")
        elif language == 'fr-FR':
            rep = [u"Je suis ce que je suis parce que je suis ce que je suis.", "Pourquoi faudrait-il tout expliquer ?", u"Il existe certaines choses qui ne s'expliquent pas. C'est comme Ã§a."]
            self.say(random.choice(rep))
        self.complete_request()
    
    @register("de-DE",".*rauchst.*du.hasch.*")
    def st_pot(self, speech, language):
        if language == 'de-DE':
            self.say("Ich gene zu es könnte möglich sein.")
        self.complete_request()

    @register("de-DE",".*kiffst.*du.*")
    def st_pot(self, speech, language):
        if language == 'de-DE':
            self.say("Ich gene zu es könnte möglich sein.")
        self.complete_request()
    
    @register("de-DE",".*pimmel.*")
    @register("fr-FR",u".*je.*(conduit|conduis|conduire).(bourrÃ©|saoul|soul|soÃ»l|sous|bourrer).*")
    def st_dui(self, speech, language):
        if language == 'de-DE':
            self.say("Ein richtiger Maenner Riehmen.")
        elif language == 'fr-FR':
            choix = random.randint(0,1)
            if choix == 1:
                self.say("Je recherche la patrouille de police la plus proche...")
                self.say(u"Je n'ai trouvÃ© aucune voiture de police dans le secteur.")
            else:
                self.say(u"Boire ou conduire, il faut choisir !")
        self.complete_request()
    
    @register("de-DE",".*hab.*eingekackt.*")
    def st_shit_pants(self, speech, language):
        if language == 'de-DE':
            self.say("Ohhhhhh! Das ist Toll!")
        self.complete_request()

    @register("de-DE",".*hab.*einpisst.*")
    def st_shit_pants(self, speech, language):
        if language == 'de-DE':
            self.say("Ha Ha Ha! Schaem dich, du bist so eklig, hau ab!")
        self.complete_request()
    
    @register("de-DE","Ich.*bin.*")
    @register("fr-FR","Je suis.*(un|une).*")
    def st_im_a(self, speech, language):
        if language == 'de-DE':
            self.say("Bist du wirklich?")
        elif language == 'fr-FR':
            self.say("Tu es ?")
        self.complete_request()
    
    @register("de-DE","Danke.*")
    @register("fr-FR",u"Merci (de|pour).*")
    def st_thanks_for(self, speech, language):
        if language == 'de-DE':
            self.say("War mir ein Vergnügen. wie immer.")
        elif language == 'fr-FR':
            self.say("Tout le plaisir est pour moi. Comme toujours.")
        self.complete_request()
    
    @register("de-DE",".*Du bist.*lustig.*")
    @register("fr-FR",u".*(tu (es|est).*(drole|drÃ´le)|MDR|LOL).*")
    def st_funny(self, speech, language):
        if language == 'de-DE':
            self.say("LOL")
        elif language == 'fr-FR':
            rep = ["LOL","MDR"]
            self.say(random.choice(rep))
        self.complete_request()
    
    @register("de-DE",".*rate.mal.*")
    @register("fr-FR",u".*devine.quoi.*")
    def st_guess_what(self, speech, language):
        if language == 'de-DE':
            self.say("Sag es mir nicht ... Du wurden gerade zum Koenig von Deutschland ernannt, stimmts?")
            self.say("Sag es mir nicht ... Du hast heraus gefunden wie du dir selber die Eier lecken kannst, stimmts?")
            self.say("Sag es mir nicht ... Du hast festgestellt das wenn du dir die Finger in die Nase steckst, was in deiner Nase ist, stimmts?")
            self.say("Sag es mir nicht ... Du hast mitbekommen das keiner seinen Onkel so gut Ficken kann wie Du, stimmts?")
            self.say("Sag es mir nicht ... Wenn du ein Weib waehrst, würdest du dich von jedem Ficken lassen, stimmts?")
            self.say("Sag es mir nicht ... Du hast schon immer gemerkt das Du nicht so schlau wie die anderen Kinder warst, stimmts?")
        if language == 'fr-FR':
            self.say("Ne me dit pas... Tu as gagnÃ© Ã  l'EuroMillion, pas vrai ?")
        self.complete_request()
    
    @register("de-DE",".*Hast.*du.*stoff.*")
    def st_talk_dirty(self, speech, language):
        if language == 'de-DE':
            self.say("Nein. Ich bin so sauber wie frisch gefallener Schnee.")
        self.complete_request()
   
    @register("de-DE",".*Kannst du.*mir.*ein Blasen.*")
    def st_blow_me(self, speech, langauge):
        if language == 'de-DE':
            self.say("Ich werde so tun, als habe ich das nicht gehoert.")
            self.say("Nein, du perverser.")
            self.say("Mit Sack?")
            self.say("Da musst du Liebchen fragen.")
            self.say("Hättest du wenigstens Bitte gesagt, aber so nicht.")
            self.say("Ja, mach dich untenrum frei und versuch dann deinen Fifi in meinen SIM schlitz zu pressen.")
        self.complete_request()
   
    @register("de-DE",".*sing.*lied.*")
    @register("fr-FR",".*chante.*chanson.*|chante.*")
    def st_sing_song(self, speech, language):
        if language == 'de-DE':
            self.say("Dag und Kerri, Dag und Kerri, Dag und Kerri, Afer Afer Afer.")
            self.say("Lebt den der alte Holzmichel noch, Holzmichel noch, Holzmichel noch? Jaaaa er lebt noch, jaaa er lebt noch, er lebt noch, stirbt nicht.")
        elif language == 'fr-FR':
            self.say(u"J'aurais voulu Ãªtre un artiste...")
            self.say(u"DÃ©solÃ©, je devrais payer des royalties si j'en dis plus.")
        self.complete_request()

    @register("de-DE", ".*standort.*test.*")
    @register("en-US", ".*location.*test.*")
    def locationTest(self, speech, language):
        location = self.getCurrentLocation(force_reload=True)
        self.say(u"lat: {0}, long: {1}".format(location.latitude, location.longitude))
        self.complete_request()
     
