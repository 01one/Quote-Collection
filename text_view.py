import pygame
pygame.init()
font=pygame.font.Font(pygame.font.get_default_font(),22)
class TextView():
	def __init__(self,screen,text='',t_x=0,t_y=0,t_w=0,t_h=0,text_color="#666666",font=font):
		self.screen=screen
		self.t_x=t_x
		self.t_y=t_y
		self.t_w=t_w
		self.t_h=t_h
		self.text_color=text_color
		self.text=text
		self.text_font=font
		self.text_lines=[]
		self.splitted_lines=self.text.splitlines()
		for splitted_line in self.splitted_lines:
			if self.text_font.size(splitted_line)[0] > self.t_w:
				words = splitted_line.split(' ')
				fitted_line=""
				for word in words:
					test_line = fitted_line + word + " "
					if self.text_font.size(test_line)[0] < self.t_w:
						fitted_line = test_line
					else:
						self.text_lines.append(fitted_line)
						fitted_line = word + " "
				self.text_lines.append(fitted_line)
			else:
				self.text_lines.append(splitted_line)
		
		text_row=self.t_y

		for line in self.text_lines:
			if line != "":
				text_surface = self.text_font.render(line, 1, self.text_color)
				self.screen.blit(text_surface, (self.t_x, self.t_y))
			self.t_y +=self.text_font.size(line)[1]
