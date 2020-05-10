import os
import time


os.system('clear')


def get_proxy():
	import os
	os.system("python parser.py") # надо встроить 
	

	


banner = '''
                                                                                     
8b           d8  88      a8P     888888888888                       88   ad88888ba   
`8b         d8'  88    ,88'           88                            88  d8"     "8b  
 `8b       d8'   88  ,88"             88                            88  Y8,          
  `8b     d8'    88,d88'              88   ,adPPYba,    ,adPPYba,   88  `Y8aaaaa,    
   `8b   d8'     8888"88,   aaaaaaaa  88  a8"     "8a  a8"     "8a  88    `"""""8b,  
    `8b d8'      88P   Y8b  """"""""  88  8b       d8  8b       d8  88          `8b  
     `888'       88     "88,          88  "8a,   ,a8"  "8a,   ,a8"  88  Y8a     a8P  
      `8'        88       Y8b         88   `"YbbdP"'    `"YbbdP"'   88   "Y88888P"   
                                                                                     
                                                                                           
                                                              
                                                              '''
print(banner)

text = '''
     
      [1]-VkBruteForceV1
      [2]-VkBruteForceV2
      [3]-Passwords-Generator 
      [4]-Vk_Comments
     
      '''
while True:
	print(text)
	v = int(input("Выберите номер:"))
	sword = input('Введите ключевые символы(слова)-->')
	def Vkpassgen():
		import os
		os.system("python passgen.py -f -o passwordlist.txt"+ " "+sword)

	def VkBruteForceV1():
		import os
		os.system("python vk.py")

	def VkBruteForceV2():
		import os
		os.system('python vk2.py')
	def VKcomments():
		import os
		os.system('python vk_comms.py')


	if v ==3:
		Vkpassgen()
		time.sleep(5)
	elif v ==1:
		VkBruteForceV1()
		time.sleep(5)
	elif v ==2:
		VkBruteForceV2()
		time.sleep(5)
	elif v == 4:
		VKcomments()
		time.sleep(5)
