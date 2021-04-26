import pyautogui,time
time.sleep(10)
f=open("story.txt",'r',encoding="utf8")
for word in f:
    pyautogui.typewrite(word)  
    pyautogui.press("enter")
