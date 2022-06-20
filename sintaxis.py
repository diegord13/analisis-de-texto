from PyDictionary import PyDictionary
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def sintaxis():
    from google.cloud import language_v1

    client = language_v1.LanguageServiceClient.from_service_account_json("indigo-bazaar-352022-1274d9f32ee1.json")

    text = u"""En informática, Hola mundo es un programa que muestra el texto «¡Hola, mundo!» en un dispositivo de visualización, en la mayoría de los casos la pantalla de un monitor. Este programa suele ser usado como introducción al estudio de un lenguaje de programación, siendo un primer ejercicio típico, y se considera fundamental desde el punto de vista didáctico.
    
    En algunos lenguajes, configurar un conjunto de herramientas básicas completo desde cero hasta el punto en que los programas triviales puedan ser compilados y ejecutados involucra una cantidad de trabajo sustancial. Por esta razón, generalmente es usado un programa muy simple para probar un nuevo conjunto de herramientas. 
    asdfkjl kjl """

    document = language_v1.Document(
        content=text, type= language_v1.Document.Type.PLAIN_TEXT
    )
    response = client.analyze_syntax(document=document)

    fmts = "{:10}: {}"
    print(fmts.format("sentences", len(response.sentences)))
    print(fmts.format("tokens", len(response.tokens)))
    dictionary = PyDictionary()
    for token in response.tokens:
            #print(fmts.format(token.part_of_speech.tag.name, token.text.content))
            dictionary = PyDictionary()
            print((dictionary.meaning(token.text.content,"es")),token.text.content )
    return True

text = u""" "En los sistemas basados en microcontroladores empleados para el aprendizaje, se suele considerar Hola mundo el programa que permite poner en modo intermitente un led.1​ El programa consiste en mandar alternativamente un nivel alto y uno bajo por uno de los puertos del sistema, dando a cada uno de dichos niveles un valor de retardo. "
 """
from google.cloud import language_v1

def classify_text(text):
    client = language_v1.LanguageServiceClient.from_service_account_json("indigo-bazaar-352022-1274d9f32ee1.json")
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    response = client.classify_text(document=document)

    for category in response.categories:
        print("=" * 80)
        print(f"category  : {category.name}")
        print(f"confidence: {category.confidence:.0%}")


#classify_text(text)
sintaxis()
