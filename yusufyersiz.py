import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from datetime import datetime
import pandas as pd
import os

class BurgerApp:
    def __init__(self, root):
        # Uygulama başlatılıyor, temel ayarlar yapılıyor
        self.root = root
        self.root.title("Burger Menü Uygulaması")
        self.root.geometry("1000x800")
        self.root.configure(bg="#f8f8f8")  # Arka plan rengi

        # Görsellerin bulunduğu dizin
        self.image_path = "images"  
        
        # Menü fiyatları
        self.menu = {
            "Classic Burger": 50,
            "Cheese Burger": 60,
            "Double Burger": 75,
            "Chicken Burger": 55,
            "Veggie Burger": 50,
            "Fish Burger": 70,
            "BBQ Burger": 65,
            "Mushroom Burger": 60,
            "Spicy Burger": 70,
            "Bacon Burger": 80
        }

        # Yan ürün fiyatları
        self.sides = {
            "Small Fries": 20,
            "Medium Fries": 25,
            "Large Fries": 30
        }

        # İçecek fiyatları
        self.drinks = {
            "Coke": 15,
            "Water": 10,
            "Sarıkola": 20,
            "Milkshake": 25
        }

        # Siparişlerin saklanacağı liste
        self.orders = []  

        # Başlangıç arayüzü oluşturuluyor
        self.create_start_widgets()

    def create_start_widgets(self):
        # Başlangıç ekranını oluşturur
        self.clear_widgets()

        frame = tk.Frame(self.root, bg="#ffffff", relief="raised", borderwidth=2)
        frame.place(relx=0.5, rely=0.5, anchor="center", width=600, height=400)

        # Başlangıç ekranı metinleri ve giriş alanları
        self.date_label = ttk.Label(frame, text="Restoran Günü Başlat", font=("Arial", 20), background="#ffffff")
        self.date_label.pack(pady=20)

        self.date_entry_label = ttk.Label(frame, text="Tarih (YYYY-MM-DD):", font=("Arial", 16), background="#ffffff")
        self.date_entry_label.pack(pady=10)

        self.date_entry = ttk.Entry(frame, font=("Arial", 16))
        self.date_entry.pack(pady=10)

        # Günü başlat ve bitir düğmeleri
        self.start_day_btn = ttk.Button(frame, text="Restoran Gününü Başlat", command=self.start_day)
        self.start_day_btn.pack(pady=20)

        self.finish_day_btn = ttk.Button(frame, text="Restoran Gününü Bitir", command=self.finish_day)
        self.finish_day_btn.pack(pady=10)

    def create_burger_selection_widgets(self):
        # Burger seçim ekranını oluşturur
        self.clear_widgets()

        self.burger_label = ttk.Label(self.root, text="Burger Seçin", font=("Arial", 22), background="#f8f8f8")
        self.burger_label.pack(pady=20)

        self.burger_var = tk.StringVar()  # Seçilen burgerin kaydedileceği değişken

        menu_frame = tk.Frame(self.root, bg="#f8f8f8")
        menu_frame.pack(pady=20)

        for burger, price in self.menu.items():
            # Her burger için bir çerçeve ve görsel
            frame = tk.Frame(menu_frame, bg="#f8f8f8", padx=10, pady=10)
            frame.pack(side="left", padx=10, pady=10)

            try:
                # Görsel dosyasını yükler
                image_file = os.path.join(self.image_path, f"{burger.lower().replace(' ', '_')}.jpg")
                image = Image.open(image_file)
                image = image.resize((100, 100), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                label = tk.Label(frame, image=photo, bg="#f8f8f8")
                label.image = photo  # Görsel referansını tutar
                label.pack()
            except FileNotFoundError:
                # Görsel bulunamazsa uyarı
                label = tk.Label(frame, text="Image not found", bg="#f8f8f8")
                label.pack()

            # Seçenek düğmesi ekler
            ttk.Radiobutton(frame, text=f"{burger} - {price} TL", variable=self.burger_var, value=burger).pack()

        # Geri ve sonraki düğmeleri
        button_frame = tk.Frame(self.root, bg="#f8f8f8")
        button_frame.pack(pady=20)

        self.back_btn = ttk.Button(button_frame, text="Geri", command=self.create_start_widgets)
        self.back_btn.pack(side="left", padx=10)

        self.next_btn = ttk.Button(button_frame, text="Sonraki", command=self.create_drink_selection_widgets)
        self.next_btn.pack(side="right", padx=10)

    def create_drink_selection_widgets(self):
        # İçecek seçim ekranını oluşturur
        self.clear_widgets()

        self.drink_label = ttk.Label(self.root, text="İçecek Seçin", font=("Arial", 22), background="#f8f8f8")
        self.drink_label.pack(pady=20)

        self.drink_var = tk.StringVar()  # Seçilen içeceğin kaydedileceği değişken

        menu_frame = tk.Frame(self.root, bg="#f8f8f8")
        menu_frame.pack(pady=20)

        for drink, price in self.drinks.items():
            # Her içecek için bir çerçeve ve görsel
            frame = tk.Frame(menu_frame, bg="#f8f8f8", padx=10, pady=10)
            frame.pack(side="left", padx=10, pady=10)

            try:
                # Görsel dosyasını yükler
                image_file = os.path.join(self.image_path, f"{drink.lower().replace(' ', '_')}.jpg")
                image = Image.open(image_file)
                image = image.resize((100, 100), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                label = tk.Label(frame, image=photo, bg="#f8f8f8")
                label.image = photo
                label.pack()
            except FileNotFoundError:
                # Görsel bulunamazsa uyarı
                label = tk.Label(frame, text="Image not found", bg="#f8f8f8")
                label.pack()

            # Seçenek düğmesi ekler
            ttk.Radiobutton(frame, text=f"{drink} - {price} TL", variable=self.drink_var, value=drink).pack()

        # Geri ve sonraki düğmeleri
        button_frame = tk.Frame(self.root, bg="#f8f8f8")
        button_frame.pack(pady=20)

        self.back_btn = ttk.Button(button_frame, text="Geri", command=self.create_burger_selection_widgets)
        self.back_btn.pack(side="left", padx=10)

        self.next_btn = ttk.Button(button_frame, text="Sonraki", command=self.create_side_selection_widgets)
        self.next_btn.pack(side="right", padx=10)

# Kod karakter limitine ulaşıldı. Tamamını almak için devamını ekleyebilirim.
    def create_side_selection_widgets(self):
        # Patates boyutu seçim ekranını oluşturur
        self.clear_widgets()

        self.side_label = ttk.Label(self.root, text="Patates Boyutu Seçin", font=("Arial", 22), background="#f8f8f8")
        self.side_label.pack(pady=20)

        self.side_var = tk.StringVar()  # Seçilen patates boyutunun kaydedileceği değişken

        menu_frame = tk.Frame(self.root, bg="#f8f8f8")
        menu_frame.pack(pady=20)

        for side, price in self.sides.items():
            # Her patates boyutu için bir çerçeve ve görsel
            frame = tk.Frame(menu_frame, bg="#f8f8f8", padx=10, pady=10)
            frame.pack(side="top", anchor="w", padx=20, pady=10)

            try:
                # Görsel dosyasını yükler
                image_file = os.path.join(self.image_path, f"{side.lower().replace(' ', '_')}.jpg")
                image = Image.open(image_file)
                image = image.resize((100, 100), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)

                # Görseli bir etiket içinde gösterir
                label = tk.Label(frame, image=photo, bg="#f8f8f8")
                label.image = photo  # Referans tutmak için
                label.pack(side="left", padx=10)
            except FileNotFoundError:
                # Görsel bulunamazsa mesaj gösterir
                label = tk.Label(frame, text=f"{side} görseli bulunamadı", bg="#f8f8f8")
                label.pack(side="left", padx=10)

            # Radyo düğmesi ekler
            ttk.Radiobutton(frame, text=f"{side} - {price} TL", variable=self.side_var, value=side).pack(side="left", padx=10)

        # Geri ve Sonraki düğmeleri için çerçeve
        button_frame = tk.Frame(self.root, bg="#f8f8f8")
        button_frame.pack(pady=20)

        self.back_btn = ttk.Button(button_frame, text="Geri", command=self.create_drink_selection_widgets)
        self.back_btn.pack(side="left", padx=10)

        self.next_btn = ttk.Button(button_frame, text="Sonraki", command=self.create_payment_widgets)
        self.next_btn.pack(side="right", padx=10)

    def create_payment_widgets(self):
        # Ödeme yöntemi seçim ekranını oluşturur
        self.clear_widgets()

        self.payment_label = ttk.Label(self.root, text="Ödeme Yöntemi Seçin", font=("Arial", 22), background="#f8f8f8")
        self.payment_label.pack(pady=20)

        self.payment_var = tk.StringVar()  # Seçilen ödeme yönteminin kaydedileceği değişken

        # Ödeme seçeneklerini ekler
        ttk.Radiobutton(self.root, text="Nakit", variable=self.payment_var, value="Nakit").pack(anchor="w", padx=20, pady=5)
        ttk.Radiobutton(self.root, text="Kart", variable=self.payment_var, value="Kart").pack(anchor="w", padx=20, pady=5)

        # Geri ve Siparişi Tamamla düğmeleri için çerçeve
        button_frame = tk.Frame(self.root, bg="#f8f8f8")
        button_frame.pack(pady=20)

        self.back_btn = ttk.Button(button_frame, text="Geri", command=self.create_side_selection_widgets)
        self.back_btn.pack(side="left", padx=10)

        self.finish_btn = ttk.Button(button_frame, text="Siparişi Tamamla", command=self.add_order)
        self.finish_btn.pack(side="right", padx=10)

    def clear_widgets(self):
        # Mevcut tüm widget'ları temizler
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_day(self):
        # Restoran gününü başlatır
        self.date = self.date_entry.get()
        try:
            self.date = datetime.strptime(self.date, "%Y-%m-%d").date()  # Tarihi doğrular
            messagebox.showinfo("Başarılı", f"Restoran günü {self.date} için başlatıldı.")
            self.create_burger_selection_widgets()  # Burger seçim ekranına geçer
        except ValueError:
            # Geçersiz tarih formatı
            messagebox.showerror("Hata", "Lütfen geçerli bir tarih formatı girin (YYYY-MM-DD).")

    def add_order(self):
        # Siparişi tamamlar ve listeye ekler
        burger = self.burger_var.get()
        drink = self.drink_var.get()
        side = self.side_var.get()
        payment = self.payment_var.get()

        if not burger or not drink or not side or not payment:
            # Eksik seçim yapılmışsa uyarı
            messagebox.showerror("Hata", "Lütfen tüm seçimleri yapın.")
            return

        total_price = self.menu[burger] + self.drinks[drink] + self.sides[side]

        order = {
            "Tarih": self.date,
            "Burger": burger,
            "İçecek": drink,
            "Patates": side,
            "Ödeme Yöntemi": payment,
            "Toplam Tutar": total_price
        }

        self.orders.append(order)  # Siparişi listeye ekler
        messagebox.showinfo("Sipariş Tamamlandı", f"Sipariş başarıyla eklendi! Toplam: {total_price} TL")
        self.create_burger_selection_widgets()  # Yeni sipariş için ekranı sıfırlar

    def finish_day(self):
        # Restoran gününü bitirir ve satışları kaydeder
        if not self.orders:
            messagebox.showinfo("Bilgi", "Bugün için herhangi bir satış yapılmadı.")
            return

        # Dosya seçici ile kayıt yeri belirlenir
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

        if not file_path:
            return

        # Siparişleri Excel dosyasına yazar
        df = pd.DataFrame(self.orders)
        df.to_excel(file_path, index=False)

        # Günlük toplam ciro hesaplanır
        total_revenue = sum(order["Toplam Tutar"] for order in self.orders)
        messagebox.showinfo("Gün Sonu", f"Satışlar kaydedildi. Toplam Ciro: {total_revenue} TL")
        self.orders = []  # Sipariş listesini sıfırlar

# Ana döngüyü başlatır
if __name__ == "__main__":
    root = tk.Tk()
    app = BurgerApp(root)
    root.mainloop()
