import cv2
import numpy
import time,threading

state = 1
def control_thread():
	global state
	while(1):
		str = raw_input()
		if(str=='q'):
			break;
		state = int(str)
def video():
	global state
	cap = cv2.VideoCapture('C:\\comic.mp4')
	while(1):
		ret,frame = cap.read()
		frame = cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)
		fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
		cv2.imshow("window",frame)
		if(cv2.waitKey(state) & 0xff==ord('q')):
			break;
		
def mainfunc():
	t1 = threading.Thread(target = control_thread,name = 'control')
	t2 = threading.Thread(target = video,name = 'control')
	t1.start()
	print "t1 start"
	t2.start()
	print "t2 start"
	t1.join()
	print "t1 ok"
	t2.join()
	print "t2 ok"
	
		
if __name__ == '__main__':
	mainfunc()
