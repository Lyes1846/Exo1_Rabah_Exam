import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://videotron.com/")
###-2-Trouver le nombre d'images sur le site :
images=driver.find_elements(By.TAG_NAME,("img"))

nombre_images = len(images)

print("le site contient ",nombre_images,"images.")

###-3-Afficher la valeur de l'attribut "alt" des images dans la console
for image in images:
    alt_text = image.get_attribute("alt")

print("Alt text:", alt_text)



###-4 T-rouver le nombre de liens sur le site
liens = driver.find_elements(By.TAG_NAME,("a"))

nombre_liens = len(liens)



print("Le site contient", nombre_liens, "liens.")

###-5- Trouver le nombre de liens dans la section "footer"
footer=driver.find_element(By.TAG_NAME,("footer"))
liens_footer=footer.find_elements(By.TAG_NAME,("a"))
nombre_liens_footer=len(liens_footer)

print("Dans la partie footer du site,on à :", nombre_liens_footer, "liens.")

###-6- # Récupérer la valeur de l'attribut "href" de chaque lien dans la section "footer" et l'afficher dans la console
for lien_footer in liens_footer:
    href_value = lien_footer.get_attribute("href")
    print("Href value:", href_value)


time.sleep(4)

driver.quit()