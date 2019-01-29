import pyautogui as pg
import time as t
import webbrowser as wb

"""
search = pg.prompt("What would you like to search for?")
pg.click(317,743)
pg.hotkey('ctrl','t')
pg.click(285,423)
pg.typewrite('www.youtube.com\n',.2)
pg.click(232,502)
pg.typewrite(search)
pg.press('enter')
pg.hotkey('ctrl','t')

yt = pg.confirm('Would you like to watch a video on YouTube?','YouTube Viewer',['yes', 'no'])
if yt == 'yes':
    search = pg.prompt("What would you like to search for?")
    pg.moveTo(317,743,2)
    pg.doubleClick()
    pg.moveTo(268, 384,2)
    pg.click()
    pg.click(285,423,4)
    pg.typewrite('www.youtube.com\n',.2)
    pg.moveTo(232,502,4)
    pg.click()
    pg.typewrite(search + '\n',.2)
elif yt == 'no':
    hw = pg.confirm('Would you like to do Homework?','Hw opener',['yes', 'no'])
    if hw == 'yes':


    pg.press('winleft')
    pg.typewrite('calculator\n', .2)
"""

yt = pg.confirm('Would you like to watch a video on YouTube?','YouTube Viewer',['yes', 'no'])
if yt == 'yes':
    search = pg.prompt("What would you like to search for?")
    pg.moveTo(317,743,2)
    pg.doubleClick()
    pg.moveTo(268, 384,2)
    pg.click()
    pg.click(285,423,4)
    pg.typewrite('www.youtube.com\n',.2)
    pg.moveTo(232,502,4)
    pg.click()
    pg.typewrite(search + '\n',.2)
elif yt == 'no':
    hw = pg.confirm('Would you like to do Homework?','Hw opener',['yes', 'no'])
    if hw == 'yes':
        subject = pg.confirm('What subject would you like to work on?','Subject Chooser',['Math', 'English', 'History'])
        if subject == 'Math':
            math = pg.confirm('Would you like to go to','Math Topics',['Google Classroom','Calculator','Homework Site'])
            if math == 'Google Classroom':
                wb.open('classroom.google.com')
            elif math == 'Calculator':
                problem = pg.prompt('What is your math problem?')
                pg.click(317,743)
                pg.hotkey('ctrl','t')
                pg.click(285,423)
                pg.typewrite(problem + '\n')
    
    elif hw == 'no':
        wb.open('www.netflix.com')
        t.sleep(2)
        pg.hotkey('winleft','up')
