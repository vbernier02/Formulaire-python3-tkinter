import tkinter as tk
from tkinter import Label, messagebox, PhotoImage
import hashlib
import sqlite3
import os

DB_FILE = "data_user.db"

def init_database():

    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        '''
        )
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", ("test", hash_password("test")))
        conn.commit()
        conn.close()

def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()

def limit_text(var, max_length):

    if len(var.get()) > max_length:
        var.set(var.get()[:max_length])

def login():

    id = entry_id.get()
    password = entry_pass.get()
    
    if not password:
        messagebox.showerror("Erreur", "Veuillez entrer un mot de passe")
        return
    
    hashed = hash_password(password)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (id,))
    result = cursor.fetchone()
    conn.close()

    if result and result[0] == hashed:
        messagebox.showinfo("Connexion", "Profil valide")
    else:
        messagebox.showerror("Erreur", "Identifiant ou mot de passe incorrect")
        entry_pass.delete(0, tk.END)

def reset():

    entry_id.delete(0, tk.END)
    entry_pass.delete(0, tk.END)

def create_account():

    signup_window = tk.Toplevel(root)
    signup_window.title("Création de compte")
    signup_window.geometry("600x400")
    signup_window.resizable(False, False)
    signup_window.grab_set()
    
    frame_signup = tk.Frame(signup_window)
    frame_signup.pack(expand=True, anchor="center", padx=20, pady=20)
    
    tk.Label(frame_signup, text="Nouveau compte", font=("Arial", 14, "bold")).pack(pady=(0, 20), anchor="center")
    
    tk.Label(frame_signup, text="Identifiant").pack(pady=(0, 5), anchor="center")
    var_id_signup = tk.StringVar()
    var_id_signup.trace("w", lambda *args: limit_text(var_id_signup, 15))
    entry_id = tk.Entry(frame_signup, width=30, textvariable=var_id_signup)
    entry_id.pack(anchor="center", pady=(0, 15))
    
    tk.Label(frame_signup, text="Mot de passe").pack(pady=(0, 5), anchor="center")
    var_password = tk.StringVar()
    var_password.trace("w", lambda *args: limit_text(var_password, 15))
    entry_password = tk.Entry(frame_signup, show="*", width=30, textvariable=var_password)
    entry_password.pack(anchor="center", pady=(0, 15))
    
    tk.Label(frame_signup, text="Confirmer le mot de passe").pack(pady=(0, 5), anchor="center")
    var_confirm_pass = tk.StringVar()
    var_confirm_pass.trace("w", lambda *args: limit_text(var_confirm_pass, 15))
    entry_confirm_pass = tk.Entry(frame_signup, show="*", width=30, textvariable=var_confirm_pass)
    entry_confirm_pass.pack(anchor="center", pady=(0, 20))
    
    def register():

        id = var_id_signup.get()
        password = var_password.get()
        confirm_password = var_confirm_pass.get()
        
        if not id:
            messagebox.showerror("Erreur", "Veuillez entrer un identifiant")
            return
        
        if not password:
            messagebox.showerror("Erreur", "Veuillez entrer un mot de passe")
            return
        
        if password != confirm_password:
            messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas")
            return
        
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                          (id, hash_password(password)))
            conn.commit()
            conn.close()
            messagebox.showinfo("Succès", "Compte créer")
            signup_window.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "Cet identifiant existe déjà")

    frame_buttons = tk.Frame(frame_signup)
    frame_buttons.pack()
    
    tk.Button(frame_buttons, text="Créer le compte", command=register).pack(side=tk.LEFT, padx=10)
    tk.Button(frame_buttons, text="Retour", command=signup_window.destroy).pack(padx=10)


root = tk.Tk()
root.title("Formulaire d’identification sécurisé")
root.geometry("900x720")
root.resizable(False, False)
init_database()

frame_logo = tk.Frame(root)
frame_logo.pack(expand=True, anchor="center")

logo_origin = PhotoImage(file="logop8.png")
logo = logo_origin.subsample(2, 2)
image = Label(frame_logo, image=logo)
image.pack()

frame_main = tk.Frame(root)
frame_main.pack(pady=(80, 15), anchor="center")

tk.Label(frame_main, text="Connexion avec un compte", font=("Arial", 18, "bold")).pack(pady=(0, 30), anchor="n")

tk.Label(frame_main, text="Identifiant").pack(pady=(0, 5), anchor="center")
var_id_main = tk.StringVar()
var_id_main.trace("w", lambda *args: limit_text(var_id_main, 15))
entry_id = tk.Entry(frame_main, textvariable=var_id_main)
entry_id.pack(anchor="center", pady=(0, 15))
entry_id.bind("<Return>", lambda event: login())

tk.Label(frame_main, text="Mot de passe").pack(pady=(0, 5), anchor="center")
var_pass_main = tk.StringVar()
var_pass_main.trace("w", lambda *args: limit_text(var_pass_main, 15))
entry_pass = tk.Entry(frame_main, show="*", textvariable=var_pass_main)
entry_pass.pack(anchor="center", pady=(0, 15))
entry_pass.bind("<Return>", lambda event: login())


frame_buttons = tk.Frame(frame_main)
frame_buttons.pack(pady=(80, 15))

tk.Button(frame_buttons, text="Connexion", command=login).pack(pady=5)

frame_separator = tk.Frame(frame_buttons)
frame_separator.pack(pady=15, fill=tk.X, padx=20)

tk.Canvas(frame_separator, height=1, bg="black", highlightthickness=0).pack(side=tk.LEFT, fill=tk.X)
tk.Label(frame_separator, text=" ou ", bg=frame_separator.cget("bg")).pack(side=tk.LEFT)
tk.Canvas(frame_separator, height=1, bg="black", highlightthickness=0).pack(side=tk.LEFT, fill=tk.X)

tk.Button(frame_buttons, text="Créer un compte", command=create_account).pack(pady=5)
tk.Button(frame_buttons, text="Reset", command=reset).pack(pady=20)

root.mainloop()