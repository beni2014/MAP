from operator import le
import pyautogui
import keyboard
class PianoTitles:
    
    def __init__(self):
        print("APASA TASTA ESC PENTRU A INCHIDE PROGRAMUL")
        x1=self._mouse_pos('STANGA')[0]
        while keyboard.is_pressed('enter'): pass
        x2=self._mouse_pos('DRAPTA')[0]
        self.left_x, self.right_x = min(x1,x2), max(x1,x2)
        self.center_y=pyautogui.sizw()[1] // 2
        self.tiles=self._tiels_pos()
        print("Coordonatele jocului sunt", self.left_x, self.right_x, self.center_y)
        

    def _mouse_pos(self, border):
        print(f'Pune cursosul in {border} ,arogomoo ferstreo kpci;io so a[asa enter')
        x,y=0,0
        while not keyboard.is_pressed('enter') and not keyboard.is_pressed('esc'):
            x,y=pyautogui.position()
            position='x: '+ str(x).rjust(4) + 'y= '+ str(y).rjust(4)
            print('\b' * len[position], end='', flush=True)
        print(f'{border} border {x,y}')
        return x,y
    def _titel_pos(self):
        lenght=self.right_x - self.left_x
        step=leng //4
        return[(self.left_x +i,self.center_y ) for i in range(step//2,lenght,step) ]
    def _is_title(self,pixel,threshold):
        color=pyautogui.pixel(*pixel)
        return True if color[0]<=threshold else False
    def run(self,*, tile_rgb=10):
        while not keyboard.is_pressed('esc'):
            for pos in self.tiles:
                if self._is_tile(pos, tile_rgb):
                    pyautogui.click(*pos)
                    break
if __name__== '__main__':
    PianoTitles().run()        
        

