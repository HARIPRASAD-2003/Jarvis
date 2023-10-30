import pygame
from email_sender import EmailSend

class EmailSenderUI:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.PURPLE = (128, 0, 128)
        self.font = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        self.recipient_input = ""
        self.subject_input = ""
        self.body_input = ""
        self.recipient_active = False
        self.subject_active = False
        self.body_active = False
        self.gui = EmailSend()

    def draw_text(self, surface, text, font, rect, color, active):
        if active:
            pygame.draw.rect(surface, self.PURPLE, rect, 0)
        else:
            pygame.draw.rect(surface, self.WHITE, rect, 0)
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, (rect.x + 5, rect.y + 5))

    def send_email(self):
        # Replace this with your email sending logic using pyautogui
        print("Recipient:", self.recipient_input)
        print("Subject:", self.subject_input)
        print("Body:", self.body_input)
        self.gui.send_email(self.recipient_input, self.subject_input, self.body_input)

    def run(self):
        screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Email Sender")

        recipient_rect = pygame.Rect(200, 100, 400, 50)
        subject_rect = pygame.Rect(200, 200, 400, 50)
        body_rect = pygame.Rect(200, 300, 400, 200)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if recipient_rect.collidepoint(event.pos):
                        self.recipient_active = not self.recipient_active
                    else:
                        self.recipient_active = False
                    if subject_rect.collidepoint(event.pos):
                        self.subject_active = not self.subject_active
                    else:
                        self.subject_active = False
                    if body_rect.collidepoint(event.pos):
                        self.body_active = not self.body_active
                    else:
                        self.body_active = False
                if event.type == pygame.KEYDOWN:
                    if self.recipient_active:
                        if event.key == pygame.K_RETURN:
                            self.recipient_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.recipient_input = self.recipient_input[:-1]
                        else:
                            self.recipient_input += event.unicode
                    if self.subject_active:
                        if event.key == pygame.K_RETURN:
                            self.subject_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.subject_input = self.subject_input[:-1]
                        else:
                            self.subject_input += event.unicode
                    if self.body_active:
                        if event.key == pygame.K_RETURN:
                            self.body_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.body_input = self.body_input[:-1]
                        else:
                            self.body_input += event.unicode

            screen.fill(self.WHITE)

            self.draw_text(screen, "Recipient:", self.font_small, pygame.Rect(100, 100, 100, 50), self.BLACK, False)
            self.draw_text(screen, "Subject:", self.font_small, pygame.Rect(100, 200, 100, 50), self.BLACK, False)
            self.draw_text(screen, "Body:", self.font_small, pygame.Rect(100, 300, 100, 50), self.BLACK, False)

            self.draw_text(screen, self.recipient_input, self.font_small, recipient_rect, self.BLACK, self.recipient_active)
            self.draw_text(screen, self.subject_input, self.font_small, subject_rect, self.BLACK, self.subject_active)
            self.draw_text(screen, self.body_input, self.font_small, body_rect, self.BLACK, self.body_active)

            send_button_rect = pygame.Rect(200, 520, 400, 50)
            pygame.draw.rect(screen, self.PURPLE, send_button_rect, 0)
            self.draw_text(screen, "Send Email", self.font, send_button_rect, self.BLACK, False)

            if send_button_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    self.send_email()
                    running = False
            pygame.display.flip()

        pygame.quit()

# if __name__ == '__main__':
#     email_sender_ui = EmailSenderUI()
#     email_sender_ui.run()
