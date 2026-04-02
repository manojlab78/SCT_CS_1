import tkinter as tk
from cipher import encrypt, decrypt, brute_force


def encrypt_text():
    text = input_box.get("1.0", tk.END)
    shift = int(shift_box.get())

    result = encrypt(text, shift)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)


def decrypt_text():
    text = input_box.get("1.0", tk.END)
    shift = int(shift_box.get())

    result = decrypt(text, shift)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)


def brute_force_text():
    text = input_box.get("1.0", tk.END)

    results = brute_force(text)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "\n".join(results))


# WINDOW
root = tk.Tk()
root.title("Caesar Cipher Tool - Manoj")

# INPUT
tk.Label(root, text="Enter Text").pack()
input_box = tk.Text(root, height=5, width=50)
input_box.pack()

# SHIFT
tk.Label(root, text="Shift Value").pack()
shift_box = tk.Entry(root)
shift_box.pack()

# BUTTONS
tk.Button(root, text="Encrypt", command=encrypt_text).pack()
tk.Button(root, text="Decrypt", command=decrypt_text).pack()
tk.Button(root, text="Brute Force", command=brute_force_text).pack()

# OUTPUT
tk.Label(root, text="Output").pack()
output_box = tk.Text(root, height=10, width=50)
output_box.pack()

# SECURITY NOTE
tk.Label(root, text="⚠️ Caesar Cipher is NOT secure", fg="red").pack()

root.mainloop()