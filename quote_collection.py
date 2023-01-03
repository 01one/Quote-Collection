from warren_buffett_quotes import  warren_buffett_quotes
from confucius_quotes import confucius_quotes 
from seneca_quotes import seneca_quotes
from lao_tzu_quotes import lao_tzu_quotes
from aristotle_quotes import aristotle_quotes
from text_view import TextView
from pygame.locals import*
import pygame,sys,time
import glob
pygame.init()

background_list=glob.glob("backgrounds/*.jpg")
li=len(background_list)-1
background=[]
for item in background_list:
	i=pygame.image.load(item)
	background.append(i)

clock=pygame.time.Clock()
w=800
h=600
screen=pygame.display.set_mode((800,600))
then=time.time()
#color=(144, 238,144)
color=(0,0,0)
n_w=0
n_c=0
n_s=0
n_l=0
n_a=0

ln_w=len(warren_buffett_quotes)-1
ln_c=len(confucius_quotes)-1
ln_s=len(seneca_quotes)-1
ln_l=len(lao_tzu_quotes)-1
ln_a=len(aristotle_quotes)-1

n=0

x=0
y=0
nxt=False

s1=100
s2=100
nx=True
nxt_s=0
game_running=True
while game_running:
	quote_surface=pygame.Surface((w,100),pygame.SRCALPHA)
	quote_surface1=pygame.Surface((w,100),pygame.SRCALPHA)
	quote_surface2=pygame.Surface((w,100),pygame.SRCALPHA)
	quote_surface3=pygame.Surface((w,100),pygame.SRCALPHA)
	quote_surface4=pygame.Surface((w,100),pygame.SRCALPHA)
	

	

	clock.tick(60)
	screen.fill(color)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	now=time.time()
	d=now-then
	if d>=9 and d<=10:
		then=now
		#n+=1
		if nxt:
			if x<=1:
				nxt=False
				#n+=1
				#s1=60
				#s2=70
				
		else:
			n+=1
			nxt=True
			nx=True
	#quote_surface1.set_alpha(50)
	nxt_i=n+1
	if n+1>li:
		nxt_1=0
	if nxt:
		if nx:
			x=x+((x+.1)*.1)
			s1-=.5
			s2-=.5
			#nxt_s+=.1
			#quote_surface.set_alpha(s1)
			#quote_surface1.set_alpha(s2)
			#quote_surface2.set_alpha(s1)
			#quote_surface3.set_alpha(s2)
			#quote_surface4.set_alpha(s1)
			if x>=w:
				nx=False
				if n_w<ln_w:
					n_w+=1
				else:
					n_w=0
				if n_c<ln_c:
					n_c+=1
				else:
					n_c=0
				if n_s<ln_s:
					n_s+=1
				else:
					n_s=0
				if n_l<ln_l:
					n_l+=1
				else:
					n_l=0
				if n_a<ln_a:
					n_a+=1
				else:
					n_a=0

		elif x>0:
			x-=(x*.2)
			#nxt_s-=.1

	
	
	#screen.blit(background[nxt_i],(0,0))
	screen.blit(background[5],(0,0))
	#quote_surface.fill((0,0,0))
	#quote_surface1.fill((0,0,0))
	#quote_surface2.fill((0,0,0))
	#quote_surface3.fill((0,0,0))
	#quote_surface4.fill((0,0,0))
	
	
	quote_surface.set_alpha(90)
	quote_surface1.set_alpha(80)
	quote_surface2.set_alpha(90)
	quote_surface3.set_alpha(80)
	quote_surface4.set_alpha(90)
	
	
	
	
	
	TextView(quote_surface,text=warren_buffett_quotes[n_w],t_x=0,t_y=20,t_w=w,t_h=100,text_color='#000000')
	TextView(quote_surface1,text=confucius_quotes[n_c],t_x=0,t_y=20,t_w=w,t_h=100,text_color='#000000')
	TextView(quote_surface2,text=seneca_quotes[n_s],t_x=0,t_y=20,t_w=w,t_h=100,text_color='#000000')
	TextView(quote_surface3,text=lao_tzu_quotes[n_l],t_x=0,t_y=20,t_w=w,t_h=100,text_color='#000000')
	TextView(quote_surface4,text=aristotle_quotes[n_a],t_x=0,t_y=20,t_w=w,t_h=100,text_color='#000000')
	
	screen.blit(quote_surface,(x,0))
	screen.blit(quote_surface1,(-x,100))
	screen.blit(quote_surface2,(x,200))
	screen.blit(quote_surface3,(-x,300))
	screen.blit(quote_surface4,(x,400))
	
	
	pygame.display.update()
