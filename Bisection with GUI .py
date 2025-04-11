import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class BisectionMethodApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bisection Method Calculator")
        self.root.geometry("900x700")
        self.root.resizable(False, False)

        # Set theme colors
        self.bg_color = "#f0f0f0"
        self.frame_color = "#ffffff"
        self.button_color = "#4CAF50"
        self.text_color = "#333333"
        self.accent_color = "#2196F3"

        self.root.configure(bg=self.bg_color)

        # Create main container
        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title
        self.title_label = tk.Label(
            self.main_frame,
            text="Bisection Method Solver",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.title_label.pack(pady=(0, 20))

        # Input Frame
        self.input_frame = tk.LabelFrame(
            self.main_frame,
            text="Parameters",
            font=("Helvetica", 12),
            bg=self.frame_color,
            fg=self.text_color,
            padx=15,
            pady=15
        )
        self.input_frame.pack(fill=tk.X, padx=5, pady=5)

        # Function input
        tk.Label(
            self.input_frame,
            text="Function f(x):",
            bg=self.frame_color,
            fg=self.text_color
        ).grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.function_entry = ttk.Entry(
            self.input_frame,
            width=40,
            font=("Helvetica", 10)
        )
        self.function_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.function_entry.insert(0, "x**3 - x - 2")

        # Interval inputs
        tk.Label(
            self.input_frame,
            text="Interval [a, b]:",
            bg=self.frame_color,
            fg=self.text_color
        ).grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.a_entry = ttk.Entry(self.input_frame, width=10, font=("Helvetica", 10))
        self.a_entry.grid(row=1, column=1, padx=(5, 2), pady=5, sticky="w")
        self.a_entry.insert(0, "1")

        tk.Label(
            self.input_frame,
            text="to",
            bg=self.frame_color,
            fg=self.text_color
        ).grid(row=1, column=2, padx=2, pady=5)

        self.b_entry = ttk.Entry(self.input_frame, width=10, font=("Helvetica", 10))
        self.b_entry.grid(row=1, column=3, padx=(2, 5), pady=5, sticky="w")
        self.b_entry.insert(0, "2")

        # Tolerance input
        tk.Label(
            self.input_frame,
            text="Tolerance (E):",
            bg=self.frame_color,
            fg=self.text_color
        ).grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.tolerance_entry = ttk.Entry(self.input_frame, width=10, font=("Helvetica", 10))
        self.tolerance_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.tolerance_entry.insert(0, "0.000001")

        # Buttons
        self.button_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.button_frame.pack(fill=tk.X, padx=5, pady=10)

        self.calculate_button = tk.Button(
            self.button_frame,
            text="Calculate Root",
            command=self.calculate_root,
            bg=self.button_color,
            fg="white",
            font=("Helvetica", 12, "bold"),
            padx=15,
            pady=5,
            bd=0
        )
        self.calculate_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(
            self.button_frame,
            text="Clear",
            command=self.clear_fields,
            bg="#f44336",
            fg="white",
            font=("Helvetica", 12),
            padx=15,
            pady=5,
            bd=0
        )
        self.clear_button.pack(side=tk.RIGHT, padx=5)

        # Results Frame
        self.results_frame = tk.LabelFrame(
            self.main_frame,
            text="Results",
            font=("Helvetica", 12),
            bg=self.frame_color,
            fg=self.text_color,
            padx=15,
            pady=15
        )
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.results_text = tk.Text(
            self.results_frame,
            height=8,
            width=80,
            font=("Helvetica", 10),
            bg="#f9f9f9",
            fg=self.text_color,
            padx=10,
            pady=10,
            wrap=tk.WORD
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)

        # Graph Frame
        self.graph_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.graph_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=(10, 0))

        # Initialize matplotlib figure
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def f(self, x):
        try:
            # Safely evaluate the function
            return eval(self.function_entry.get(), {'x': x, 'np': np})
        except:
            messagebox.showerror("Error", "Invalid function expression")
            return None

    def bisection_method(self, a, b, E=0.000001):
        if self.f(a) * self.f(b) > 0:
            return None, "No root exists in the given interval [a, b] (f(a) and f(b) have the same sign)"

        counter = 0
        iterations = []

        while abs(b - a) > E:
            counter += 1
            mid = (a + b) / 2
            iterations.append((counter, a, b, mid, self.f(mid), abs(b - a)))

            if self.f(mid) == 0:
                return mid, iterations
            elif self.f(a) * self.f(mid) < 0:
                b = mid
            else:
                a = mid

        return mid, iterations

    def calculate_root(self):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            E = float(self.tolerance_entry.get())

            root, iterations = self.bisection_method(a, b, E)

            self.results_text.config(state=tk.NORMAL)
            self.results_text.delete(1.0, tk.END)

            if root is None:
                self.results_text.insert(tk.END, iterations)
            else:
                self.results_text.insert(tk.END, f"Root found at: x ≈ {root:.8f}\n\n")
                self.results_text.insert(tk.END, "Iteration details:\n")
                self.results_text.insert(tk.END, "{:<10} {:<12} {:<12} {:<12} {:<15} {:<15}\n".format(
                    "Step", "a", "b", "mid", "f(mid)", "Error"
                ))
                self.results_text.insert(tk.END, "-" * 80 + "\n")

                for step in iterations:
                    self.results_text.insert(tk.END,
                                             "{:<10} {:<12.6f} {:<12.6f} {:<12.6f} {:<15.6f} {:<15.6f}\n".format(
                                                 step[0], step[1], step[2], step[3], step[4], step[5]
                                             ))

            self.results_text.config(state=tk.DISABLED)
            self.plot_function(a, b, root)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def plot_function(self, a, b, root):
        self.plot.clear()

        # Generate x values
        x = np.linspace(a - 1, b + 1, 400)
        y = [self.f(xi) for xi in x]

        # Plot the function
        self.plot.plot(x, y, 'b-', label='f(x)')
        self.plot.axhline(0, color='black', linewidth=0.5)
        self.plot.axvline(0, color='black', linewidth=0.5)

        # Plot the root if found
        if root is not None:
            self.plot.plot(root, self.f(root), 'ro', label=f'Root at x≈{root:.6f}')

        # Plot the interval
        self.plot.axvline(a, color='green', linestyle='--', alpha=0.5, label='Interval [a, b]')
        self.plot.axvline(b, color='green', linestyle='--', alpha=0.5)

        self.plot.set_title(f"Plot of f(x) = {self.function_entry.get()}")
        self.plot.set_xlabel("x")
        self.plot.set_ylabel("f(x)")
        self.plot.legend()
        self.plot.grid(True, alpha=0.3)

        self.canvas.draw()

    def clear_fields(self):
        self.function_entry.delete(0, tk.END)
        self.function_entry.insert(0, "x**3 - x - 2")
        self.a_entry.delete(0, tk.END)
        self.a_entry.insert(0, "1")
        self.b_entry.delete(0, tk.END)
        self.b_entry.insert(0, "2")
        self.tolerance_entry.delete(0, tk.END)
        self.tolerance_entry.insert(0, "0.000001")

        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state=tk.DISABLED)

        self.plot.clear()
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = BisectionMethodApp(root)
    root.mainloop()