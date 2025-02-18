import socket
from tkinter import Tk, Label, Entry, Button, Text, END, messagebox

class PortScanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Port Scanner")

        # Target IP Address
        self.label_ip = Label(root, text="Target IP Address:")
        self.label_ip.grid(row=0, column=0, padx=10, pady=10)
        self.entry_ip = Entry(root, width=30)
        self.entry_ip.grid(row=0, column=1, padx=10, pady=10)

        # Port to Scan
        self.label_port = Label(root, text="Port to Scan:")
        self.label_port.grid(row=1, column=0, padx=10, pady=10)
        self.entry_port = Entry(root, width=30)
        self.entry_port.grid(row=1, column=1, padx=10, pady=10)

        # Scan Button
        self.scan_button = Button(root, text="Scan Port", command=self.scan_port)
        self.scan_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Results Text Area
        self.results_text = Text(root, height=5, width=50)
        self.results_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def scan_port(self):
        target_ip = self.entry_ip.get()
        port = self.entry_port.get()

        if not target_ip or not port:
            messagebox.showwarning("Warning", "Please fill in both fields.")
            return

        try:
            port = int(port)
        except ValueError:
            messagebox.showwarning("Warning", "Port must be an integer.")
            return

        self.results_text.delete(1.0, END)
        self.results_text.insert(END, f"Scanning port {port} on {target_ip}...\n")

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    self.results_text.insert(END, f"Port {port} is open.\n")
                else:
                    self.results_text.insert(END, f"Port {port} is closed.\n")
        except Exception as e:
            self.results_text.insert(END, f"Error scanning port {port}: {e}\n")

if __name__ == "__main__":
    root = Tk()
    port_scanner = PortScanner(root)
    root.mainloop()