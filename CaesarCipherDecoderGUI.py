import tkinter as tk
from tkinter import ttk, scrolledtext
import CaesarDecoder  # Corrected import statement

class CaesarCipherGUI:
    def __init__(self, master):
        self.master = master
        master.title("Caesar Cipher Decoder")
        master.geometry("600x500")
        master.configure(bg='black')

        # Set style
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('TLabel', foreground='green', background='black')
        self.style.configure('TButton', foreground='green', background='black')
        self.style.configure('TCheckbutton', foreground='green', background='black')

        # Create and set up widgets
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        # Input area
        self.input_label = ttk.Label(self.master, text="Enter ciphertext:")
        self.input_text = scrolledtext.ScrolledText(self.master, height=5, bg='black', fg='green', insertbackground='green')

        # Buttons and options
        self.decode_button = ttk.Button(self.master, text="Decode", command=self.decode)
        self.clear_button = ttk.Button(self.master, text="Clear", command=self.clear_fields)
        self.show_all_var = tk.BooleanVar()
        self.show_all_check = ttk.Checkbutton(self.master, text="Show all decryptions", variable=self.show_all_var)

        # Output area
        self.output_label = ttk.Label(self.master, text="Decoding result:")
        self.output_text = scrolledtext.ScrolledText(self.master, height=15, bg='black', fg='green', state='disabled')

    def layout_widgets(self):
        # Use grid layout
        self.input_label.grid(row=0, column=0, columnspan=3, sticky="w", padx=5, pady=5)
        self.input_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        self.decode_button.grid(row=2, column=0, padx=5, pady=10, sticky="ew")
        self.clear_button.grid(row=2, column=1, padx=5, pady=10, sticky="ew")
        self.show_all_check.grid(row=2, column=2, padx=5, pady=10, sticky="ew")

        self.output_label.grid(row=3, column=0, columnspan=3, sticky="w", padx=5, pady=5)
        self.output_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        # Configure grid weights
        self.master.grid_columnconfigure((0, 1, 2), weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(4, weight=2)

    def decode(self):
        ciphertext = self.input_text.get("1.0", tk.END).strip()
        dictionary = CaesarDecoder.load_dictionary()
        best_shift, best_decryption, word_count, all_decryptions = CaesarDecoder.caesar_cipher_decoder(ciphertext, dictionary)
        
        self.display_results(best_shift, best_decryption, word_count, all_decryptions)

    def display_results(self, best_shift, best_decryption, word_count, all_decryptions):
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        
        if self.show_all_var.get():
            self.output_text.insert(tk.END, "All Decryptions:\n\n")
            for shift, plaintext in all_decryptions:
                self.output_text.insert(tk.END, f"Shift {shift}: {plaintext}\n")
            self.output_text.insert(tk.END, "\n")

        self.output_text.insert(tk.END, f"Best shift: {best_shift}\n")
        self.output_text.insert(tk.END, f"Decoded text: {best_decryption}\n")
        self.output_text.insert(tk.END, f"Words found: {word_count}\n")
        
        self.output_text.config(state='disabled')

    def clear_fields(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state='disabled')

def main():
    root = tk.Tk()
    gui = CaesarCipherGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
