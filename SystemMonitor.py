import tkinter as tk
import cpuinfo
import psutil


class Win(tk.Tk):
    def __init__(self):
        super(Win, self).__init__()

        self.title("System Monitor")
        self.geometry("550x210""+500+500")
        self.resizable(True, True)
        self.label2 = tk.Label()
        self.label3 = tk.Label()
        self.label4 = tk.Label()

    def labels(self):
        label1 = tk.Label(self, text=cpuinfo.get_cpu_info()['brand_raw'], bg="grey", fg='white',
                          font=('BooKMan', 14, 'bold'), width=55, height=2)
        self.label2.configure(bg="grey", fg='white',
                              font=('BooKMan', 14, 'bold'), width=55, height=2)
        self.label3.configure(bg="grey", fg='white',
                              font=('BooKMan', 14, 'bold'), width=55, height=2)
        self.label4.configure(bg="grey", fg='white',
                              font=('BooKMan', 14, 'bold'), width=55, height=2)

        label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()

    def cpu_info(self):
        self.label2.configure(text=f'CPU Frequency: {int(psutil.cpu_freq()[0])}Mhz  '
                                   f'Temp:{round(psutil.sensors_temperatures().get("k10temp")[0].current, 1)}°C')
        self.label3.configure(text=F'Processor is loaded on: {psutil.cpu_percent()}%')
        self.after(1000, self.cpu_info)

    def ram_info(self):
        self.label4.configure(
            text=F'RAM used: {round(psutil.virtual_memory()[3] / 10e+8, 1)}gb ({psutil.virtual_memory()[2]}%) out of '
                 F'{round(psutil.virtual_memory()[0] / 10e+8, 1)}gb')
        self.after(1000, self.ram_info)

    def start(self):
        self.labels()
        self.cpu_info()
        self.ram_info()
        self.mainloop()


if __name__ == "__main__":
    app = Win()
    app.start()

