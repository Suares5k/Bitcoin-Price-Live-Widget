import requests
import tkinter as tk
from tkinter import font
from threading import Thread
from ttkthemes import ThemedTk
import time

class BitcoinPriceApp:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # Remove a barra de título e bordas
        self.root.title("Preço do Bitcoin - Mercado Bitcoin")
        
        # Definir o tamanho da janela
        self.window_width = 400
        self.window_height = 200
        
        # Obter as dimensões da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calcular a posição central
        position_top = int(screen_height / 2 - self.window_height / 2)
        position_left = int(screen_width / 2 - self.window_width / 2)
        
        # Definir a geometria da janela
        self.root.geometry(f"{self.window_width}x{self.window_height}+{position_left}+{position_top}")
        self.root.configure(bg="#1E1E1E")

        # Fontes personalizadas
        self.custom_font = font.Font(family="Poppins", size=18, weight="bold")
        self.percentage_font = font.Font(family="Poppins", size=14)
        self.title_font = font.Font(family="Poppins", size=12, weight="bold")

        # Estado inicial da moeda
        self.show_in_usd = False  # Inicia exibindo o preço em Real

        # Frame para o conteúdo principal
        self.main_frame = tk.Frame(root, bg="#1E1E1E")
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Título "Preço BTC"
        self.title_label_btc = tk.Label(self.main_frame, text="Preço BTC", font=self.title_font, bg="#1E1E1E", fg="#FFFFFF")
        self.title_label_btc.pack(pady=(20, 5))

        # Price Label
        self.price_label = tk.Label(self.main_frame, text="Carregando...", font=self.custom_font, bg="#1E1E1E", fg="#FFFFFF")
        self.price_label.pack(pady=10)

        # Percentage Change Label
        self.percentage_label = tk.Label(self.main_frame, text="", font=self.percentage_font, bg="#1E1E1E", fg="#FFFFFF")
        self.percentage_label.pack(pady=5)

        # Botão de troca de moeda
        self.currency_button = tk.Button(self.main_frame, text="USD", command=self.toggle_currency, bg="#1E1E1E", fg="#FFFFFF", borderwidth=0, font=self.title_font, activebackground="#1E1E1E", activeforeground="#FFFFFF")
        self.currency_button.pack(pady=(10, 5))  # Posicionado abaixo da porcentagem de valorização

        # Botão de fechar personalizado
        self.close_button = tk.Button(self.main_frame, text="✖", command=self.root.destroy, bg="#1E1E1E", fg="#FFFFFF", borderwidth=0, font=self.title_font, activebackground="#FF4C4C", activeforeground="#FFFFFF")
        self.close_button.place(x=self.window_width - 30, y=10, width=20, height=20)

        # Start the update loop in a separate thread
        self.update_thread = Thread(target=self.update_price)
        self.update_thread.daemon = True
        self.update_thread.start()

        # Habilitar a movimentação da janela com eventos de mouse
        self.main_frame.bind("<Button-1>", self.start_move)
        self.main_frame.bind("<B1-Motion>", self.move_window)

        # Agendar a atualização periódica do preço
        self.schedule_update()

    def toggle_currency(self):
        self.show_in_usd = not self.show_in_usd  # Alterna o estado entre Real e USD
        self.currency_button.config(text="REAL" if self.show_in_usd else "USD")  # Altera o texto do botão
        self.update_price_display()  # Atualiza a exibição do preço

    def start_move(self, event):
        self.x_offset = event.x
        self.y_offset = event.y

    def move_window(self, event):
        x = event.x_root - self.x_offset
        y = event.y_root - self.y_offset
        self.root.geometry(f"+{x}+{y}")

    def get_bitcoin_data(self):
        try:
            # Obtenha dados do preço do Bitcoin em BRL e USD
            url_brl = "https://www.mercadobitcoin.net/api/BTC/ticker/"
            url_usd = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"  # API para obter preço em USD

            response_brl = requests.get(url_brl)
            response_brl.raise_for_status()
            data_brl = response_brl.json()['ticker']
            price_brl = float(data_brl['last'])

            response_usd = requests.get(url_usd)
            response_usd.raise_for_status()
            data_usd = response_usd.json()
            price_usd = float(data_usd['bpi']['USD']['rate'].replace(",", ""))

            # Calcula a variação percentual com base nos dados da API
            opening_price = float(data_brl['open'])
            percentage_change = ((price_brl - opening_price) / opening_price) * 100
            percentage = f"{percentage_change:.2f}%"

            return price_brl, price_usd, percentage
        except requests.exceptions.RequestException as e:
            print("Erro ao conectar com a API:", e)
            return None, None, None
        except Exception as e:
            print("Erro ao processar os dados:", e)
            return None, None, None

    def update_price(self):
        price_brl, price_usd, percentage = self.get_bitcoin_data()
        if price_brl and price_usd and percentage:
            self.price_brl = price_brl
            self.price_usd = price_usd
            self.percentage = percentage
            self.update_price_display()
        else:
            self.price_label.config(text="Erro ao obter dados")
            self.percentage_label.config(text="Verifique a conexão ou a API", fg="#FFFFFF")

    def update_price_display(self):
        # Atualiza a exibição do preço conforme a moeda selecionada
        price = f"R$ {self.price_brl:,.2f}" if not self.show_in_usd else f"$ {self.price_usd:,.2f}"
        self.price_label.config(text=price.replace(",", "X").replace(".", ",").replace("X", "."))
        
        if self.percentage.startswith("-"):
            self.percentage_label.config(text=f"{self.percentage} 1 Dia", fg="#FF4C4C")  # Vermelho para queda
        else:
            self.percentage_label.config(text=f"+{self.percentage} 1 Dia", fg="#4CAF50")  # Verde para aumento

    def schedule_update(self):
        # Atualiza o preço e agenda a próxima atualização para daqui a 10 segundos
        self.update_price()
        self.root.after(10000, self.schedule_update)

# Run the app using ThemedTk to apply a dark theme
root = ThemedTk(theme="black")  # O tema "black" aplica uma aparência mais escura
app = BitcoinPriceApp(root)
root.mainloop()
