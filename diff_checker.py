#-*- encoding:utf-8 -*-

import datetime
import os
from time import sleep
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import filedialog
import compare_process

DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M:%S'
DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

TEST_MODE = 1

EXECUTE_PATH = os.path.abspath(os.path.dirname(__file__)) + '/'
FILE_TYPE = [('text files', '*.txt*')]

class DiffChecker(tk.Tk):

    def __init__(self):

        # Basic initial
        super().__init__()
        self.resizable(0, 0)
        self.protocol('WM_DELETE_WINDOW', self.close_window)

        # UI initial
        self.initial_user_interface()

        # Test mode
        self.test_mode()

    def initial_user_interface(self):
        # Window
        self.geometry('{0}x{1}+{2}+{3}'.format(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
            int((self.winfo_screenwidth() - WINDOW_WIDTH) / 2),
            int((self.winfo_screenheight() - WINDOW_HEIGHT) / 2)
        ))
        self.title('RO Diff Checker')

        # Text input and output
        self.ResultText = ScrolledText(self)
        self.ResultText.place(x=10, y=130, width=780, height=460)

        # Label
        self.Label_Old = tk.Label(self, text='舊版文字')
        self.Label_Old.place(x=10, y=10, width=80, height=30)
        self.Label_New = tk.Label(self, text='新版文字')
        self.Label_New.place(x=10, y=50, width=80, height=30)
        self.Label_Result = tk.Label(self, text='比對結果')
        self.Label_Result.place(x=10, y=90, width=80, height=30)
        
        self.Label_Notice = tk.Label(self, text='95 製作的 0 優化糞程式')
        self.Label_Notice.place(x=210, y=90, width=580, height=30)
        
        self.Label_Old = tk.Label(self, text='未選擇檔案')
        self.Label_Old.place(x=210, y=10, width=580, height=30)
        self.Label_New = tk.Label(self, text='未選擇檔案')
        self.Label_New.place(x=210, y=50, width=580, height=30)

        # Button
        self.Btn_SelectOld = tk.Button(self, text='選擇檔案 →', command=self.btn_select_old)
        self.Btn_SelectOld.place(x=100, y=10, width=100, height=30)
        self.Btn_SelectNew = tk.Button(self, text='選擇檔案 →', command=self.btn_select_new)
        self.Btn_SelectNew.place(x=100, y=50, width=100, height=30)
        self.Btn_Execute = tk.Button(self, text='執行比對 ▼', command=self.btn_execute)
        self.Btn_Execute.place(x=100, y=90, width=100, height=30)

    def test_mode(self):
        if TEST_MODE == 1:
            self.Label_Old['text'] = 'C:/Users/Username/Desktop/Code/ROItemInfoDiff/old.txt'
            self.Label_New['text'] = 'C:/Users/Username/Desktop/Code/ROItemInfoDiff/new.txt'

    def close_window(self):
        if messagebox.askyesno('操作詢問', '您確定要關掉 RO Diff Checker 了嗎？'):
            sleep(0.5)
            self.destroy()

    def btn_select_old(self):
        select_result = filedialog.askopenfilename(
            title='開啟檔案（舊）',
            initialdir=EXECUTE_PATH,
            filetypes=FILE_TYPE
        )

        if select_result == '':
            messagebox.showinfo('操作提示', '您未選擇檔案。')
        
        else:
            self.Label_Old['text'] = select_result

    def btn_select_new(self):
        select_result = filedialog.askopenfilename(
            title='開啟檔案（新）',
            initialdir=EXECUTE_PATH,
            filetypes=FILE_TYPE
        )

        if select_result == '':
            messagebox.showinfo('操作提示', '您未選擇檔案。')
        
        else:
            self.Label_New['text'] = select_result

    def btn_execute(self):
        if self.Label_Old['text'] == '未選擇檔案' or self.Label_New['text'] == '未選擇檔案':
            messagebox.showinfo('操作提示', '尚未選擇比對的檔案。')
        
        elif self.Label_Old['text'] == self.Label_New['text']:
            messagebox.showinfo('操作提示', '選擇的檔案相同，無法比對。')

        else:
            compare_process.diff_compare(self.Label_Old['text'], self.Label_New['text'], self.ResultText)