# create a GUI

from tkinter import *
import tkinter as tk
import os
import struct


class Interface:
    def __init__(self, root):
        """
        this is the init form
        """
        self.root = root
        self.create_frame_top()
        self.create_frame_bottom()

    def create_frame_top(self):
        """
        create Top Frame
        """
        self.frm_top_label = tk.Label(self.root, text="NPIC", fg="blue", bg="yellow", font=('Times New Roman', 20))
        self.frm_top_label.grid(row=0, column=0, padx=15, pady=2)

    def create_frame_bottom(self):
        """
        create bottom frame
        :return:
        """
        self.frm_bottom = tk.LabelFrame(self.root)
        self.frm_bottom.grid(row=1, column=0, padx=15, pady=2)

        self.frm_bottom_label_0 = tk.Label(self.frm_bottom, text="测点索引: ", font=('Times New Roman', 15))
        self.frm_bottom_label_0.grid(row=0, column=0, padx=15, pady=2, sticky="e")

        self.frm_bottom_btn_0 = tk.Button(self.frm_bottom, text="确  定", relief=RIDGE, bd=4, width=10,
                                          font=('Times New Roman', 12), command=self.show_info)
        self.frm_bottom_btn_0.grid(row=3, column=1, padx=15, pady=2)

        self.frm_bottom_entry_var_0 = StringVar()
        self.frm_bottom_entry_0 = tk.Entry(self.frm_bottom, textvariable=self.frm_bottom_entry_var_0)
        self.frm_bottom_entry_0.grid(row=0, column=1, padx=15, pady=2)

    def show_info(self):
        """
        btn callback
        :return:
        """
        try:
            k = int(self.frm_bottom_entry_var_0.get())

            file_path = os.path.abspath('/Users/zhangqiushui/Desktop/1号机历史数据文件20170417/ANAHIST0.dat[SUCCESS]')
            f = open(file_path, 'rb')

            f.seek(342368 + 600 * 5 * k)
            fs = f.read(600 * 5)

            f.close()

            data = bytearray(fs)

            try:
                desktop_path = '/Users/zhangqiushui/Desktop/'
                full_path = desktop_path + 'data' + str(k) + '.txt'
                file = open(full_path, 'w')
                file.writelines(str(k) + '\n')

            except IOError:
                self.frm_top_label = tk.Label(self.root, text="FIND THE CORRECT PATH FOR THE FILE", fg="red",
                                              bg="yellow",
                                              font=('Times New Roman', 30))
                self.frm_top_label.grid(row=0, column=0, padx=15, pady=2)

            # reshape the data
            for i in range(0, len(data), 5):
                b = data[i:i + 5]
                c = b[0:4]
                d = struct.unpack('f', c)[0]
                e = str(d)
                try:
                    file.writelines(e + '\n')
                except IOError:
                    self.frm_top_label = tk.Label(self.root, text="WRITE LINES ERROR", fg="red", bg="yellow",
                                                  font=('Times New Roman', 30))
                    self.frm_top_label.grid(row=0, column=0, padx=15, pady=2)

            file.close()

        except ValueError:
            self.frm_top_label = tk.Label(self.root, text="INPUT SOMETHING", fg="red", bg="yellow",
                                          font=('Times New Roman', 30))
            self.frm_top_label.grid(row=0, column=0, padx=15, pady=2)

        else:
            self.frm_top_label = tk.Label(self.root, text="CHECK YOUR DESKTOP", fg="blue", bg="yellow",
                                          font=('Times New Roman', 30))
            self.frm_top_label.grid(row=0, column=0, padx=15, pady=2)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("INPUT")
    Interface(root)
    root.mainloop()
