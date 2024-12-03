import tkinter as tk
from tkinter import messagebox

class Dinosaur:
    def __init__(self, name, attack, hp, speed) -> None:
        self.name = name
        self.attack = attack
        self.hp = hp
        self.speed = speed

    def __str__(self) -> str:
        return f"{self.name} | Ataque: {self.attack} | HP: {self.hp}"
    
    def ataque_basico(self, enemy):
        damage_dealt = self.attack
        enemy.hp -= damage_dealt
        if enemy.hp < 0:
            enemy.hp = 0
        return damage_dealt

class Teeths(Dinosaur):
    def __init__(self, name, attack, hp, speed) -> None:
        super().__init__(name, attack, hp, speed)
        
    def ataque_especial(self, enemy):
        damage_dealt = self.attack * 2
        enemy.hp -= damage_dealt  
        if enemy.hp < 0:
            enemy.hp = 0
        return damage_dealt

class Claws(Dinosaur):
    def __init__(self, name, attack, hp, speed) -> None:
        super().__init__(name, attack, hp, speed)

class Armor(Dinosaur):
    def __init__(self, name, attack, hp, speed) -> None:
        super().__init__(name, attack, hp, speed)

class Jogo:
    def __init__(self):
        self.dinos = self.create()
        self.tempo_restante = 15
        self.pause = False
        self.identifier = None
        self.root = tk.Tk()
        self.text_combate = None
        self.label_tempo = None
        self.btn_sair = None
        self.btn_ataque_basico = None
        self.btn_ataque_especial = None
        self.btn_iniciar = None
        self.dino_numero = 1

    def create(self):
        dino1 = Teeths("Tyrannosaurus Rex", 60, 100, 110)
        dino2 = Claws("Velociraptor", 40, 70, 120)
        dino3 = Armor("Triceratops", 20, 130, 100)
        return dino1, dino2, dino3

    def combate(self, enemy, ataque_escolhido):
        dano = ataque_escolhido(enemy)
        return dano

    def atualizar_combate(self):
        if self.dinos[self.dino_numero].hp <= 0:
            info_1 = f"{self.dinos[0].name} | HP: {self.dinos[0].hp}\n"
            info_2 = f"{self.dinos[self.dino_numero].name} | HP: {self.dinos[self.dino_numero].hp}\n"
            self.text_combate.delete(1.0, tk.END)  
            self.text_combate.insert(tk.END, info_1 + info_2)
            self.text_combate.insert(tk.END, "Inimigo derrotado!\n")

        info_1 = f"{self.dinos[0].name} | HP: {self.dinos[0].hp}\n"
        info_2 = f"{self.dinos[self.dino_numero].name} | HP: {self.dinos[self.dino_numero].hp}\n"
        self.text_combate.delete(1.0, tk.END)  
        self.text_combate.insert(1.0, "Batalha!\n")
        self.text_combate.insert(tk.END, info_1 + info_2)

    def derrotou(self):
        self.btn_ataque_basico.destroy()
        self.btn_ataque_especial.destroy()
        self.label_tempo.pack_forget()
        self.btn_sair.pack_forget()
        self.resetar_timer()
        self.btn_iniciar = tk.Button(self.root, text="Iniciar", command=self.criar_botoes)
        self.btn_iniciar.pack(pady=10)
        self.btn_sair.pack(pady=10)
        self.dino_numero = 2
        self.atualizar_combate()

    def atacar_basico(self):
        ataque_escolhido = self.dinos[0].ataque_basico
        dano = self.combate(self.dinos[self.dino_numero], ataque_escolhido)
        self.btn_ataque_especial.config(state="normal")
        if self.dinos[self.dino_numero].hp <= 0:
            self.pausar_timer()
            self.atualizar_combate()
            messagebox.showinfo("Ataque Básico", f"{self.dinos[0].name} atacou com dano: {dano}!\n{self.dinos[self.dino_numero].name} agora tem {self.dinos[self.dino_numero].hp} de HP.")
            messagebox.showinfo("Inimigo derrotado", f"{self.dinos[0]} derrotou {self.dinos[self.dino_numero]}!")
            self.derrotou()
            return
        self.atualizar_combate()
        self.resetar_timer()
        ok = messagebox.showinfo("Ataque Básico", f"{self.dinos[0].name} atacou com dano: {dano}!\n{self.dinos[self.dino_numero].name} agora tem {self.dinos[self.dino_numero].hp} de HP.")
        if ok:
            self.contagem_regressiva()

    def atacar_especial(self):
        ataque_escolhido = self.dinos[0].ataque_especial
        dano = self.combate(self.dinos[self.dino_numero], ataque_escolhido)
        self.btn_ataque_especial.config(state="disabled")
        if self.dinos[self.dino_numero].hp <= 0:
            self.pausar_timer()
            self.atualizar_combate()
            messagebox.showinfo("Ataque Especial", f"{self.dinos[0].name} usou um ataque especial com dano: {dano}!\n{self.dinos[self.dino_numero].name} agora tem {self.dinos[self.dino_numero].hp} de HP.")
            messagebox.showinfo("Inimigo derrotado", f"{self.dinos[0]} derrotou {self.dinos[self.dino_numero]}!")
            self.derrotou()
            return
        self.atualizar_combate()
        self.resetar_timer()
        ok = messagebox.showinfo("Ataque Especial", f"{self.dinos[0].name} usou um ataque especial com dano: {dano}!\n{self.dinos[self.dino_numero].name} agora tem {self.dinos[self.dino_numero].hp} de HP.")
        if ok:
            self.contagem_regressiva()

    def iniciar_timer(self):
        if not self.pause:
            self.tempo_restante = 15  
            self.atualizar_label_tempo()
            self.contagem_regressiva()
        else:
            self.contagem_regressiva()

    def pausar_timer(self):
        self.pause = True
        self.contagem_regressiva()

    def resetar_timer(self):
        if self.identifier is not None:
            self.root.after_cancel(self.identifier)
        self.tempo_restante = 15  
        self.atualizar_label_tempo()
        self.contagem_regressiva(stop=True)

    def atualizar_label_tempo(self):
        self.label_tempo.config(text=f"Tempo para atacar: {self.tempo_restante} segundos")

    def contagem_regressiva(self, stop=False):
        if stop:
            self.root.after_cancel(self.identifier)
        elif self.pause:
            self.root.after_cancel(self.identifier)
        elif self.tempo_restante > 0:
            self.tempo_restante -= 1
            self.atualizar_label_tempo()
            self.identifier = self.root.after(1000, self.contagem_regressiva)  
        else:
            self.tempo_esgotado_acao()

    def tempo_esgotado_acao(self):
        messagebox.showinfo("Tempo Esgotado", "O tempo esgotou! O ataque básico foi executado automaticamente.")
        self.atacar_basico()

    def sair_jogo(self):
        self.pausar_timer()
        resposta = messagebox.askyesno("Sair", "Você tem certeza que deseja sair?")
        if resposta:
            self.root.quit()  
        else:
            self.pause = False
            self.contagem_regressiva()

    def criar_botoes(self):
        
        if self.btn_sair is not None:
            self.btn_sair.pack_forget()
        
        self.label_tempo.pack(pady=10)
        
        self.btn_ataque_basico = tk.Button(self.root, text=f"Ataque Básico | {self.dinos[0].attack}", command=self.atacar_basico)
        self.btn_ataque_basico.pack(pady=10)

        self.btn_ataque_especial = tk.Button(self.root, text=f"Ataque Especial | {self.dinos[0].attack * 2}", command=self.atacar_especial, state="disabled")
        self.btn_ataque_especial.pack(pady=10)
        
        self.btn_sair = tk.Button(self.root, text="Sair", command=self.sair_jogo)
        self.btn_sair.pack(pady=10)
        
        self.btn_iniciar.pack_forget()  

        self.iniciar_timer()

    def iniciar(self):
        self.text_combate = tk.Text(self.root, height=10, width=50)
        self.text_combate.pack()

        self.label_tempo = tk.Label(self.root, font=("Helvetica", 14))
        self.atualizar_combate()

        self.btn_iniciar = tk.Button(self.root, text="Iniciar", command=self.criar_botoes)
        self.btn_iniciar.pack(pady=10)

        self.root.mainloop()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.iniciar()
