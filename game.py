from pygame import *

class GameSprite(sprite.Sprite): 
    def __init__(self, filename, x, y, width, height, speed = 0):
        super().__init__()   
        self.image = image.load(filename)
        self.image = transform.scale(self.image, (width, height)) 
        self.rect = Rect(x, y, width, height) 
        self.speed = speed 
    def draw(self, surface): 
        surface.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_a]: 
            self.rect.x -= self.speed 
        if keys [K_d]: 
            self.rect.x += self.speed 
    
game_is_running = True 
while game_is_running: 
    for e in event.get(): 
        if e.type == QUIT: 
            game_is_running = False 
        if e.type == KEYDOWN and e.key == K_SPACE:
            player.shoot()  

    background.draw(window) 

    if not death: 
        enemies.update()
        enemies.draw(window)
        bullets.update()
        bullets.draw(window) 

        player.update() 
        player.draw(window) 

        points_image = f.render(str(points), True, (255, 255, 255)) 
        window.blit(points_image, (30, 30)) 

    hits = sprite.groupcollide(enemies, bullets, True, True) 
    for hit in hits: 
        create_enemy() 
        points += 1 

    death = sprite.spritecollide(player, enemies, False) 
    if death: 
        game_over.draw(window)

    display.update()
    clock.tick(60) 