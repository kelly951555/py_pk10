from tkinter import *
from tkinter import ttk
from PK10_lottery import *
import sqlite3
# import pymysql
# from env import *
# lottery list
pk10 = {'30秒PK10 #111': 111,
        '1分PK10 #107': 107,
        '澳洲幸运10 #257': 257
        }

# select code by lottery and issue (pymysql)
# def sqlexe(lottery, issue):
#     db = pymysql.connect(host=gsdb()[0], port=gsdb()[1],
#                          user=gsdb()[2], passwd=gsdb()[3],
#                          db=gsdb()[4], charset=gsdb()[5])
#     cur = db.cursor()
#     sql = "SELECT `code` FROM issue_info WHERE lottery_id = {} AND issue = '{}'" \
#         .format(lottery, issue)
#     cur.execute(sql)
#     result = cur.fetchone()
#     cur.close()
#     db.close()
#     return result

# select code by lottery and issue (sqlite3)
def sqlexe(lottery, issue):
    conn = sqlite3.connect('issue.db')
    sql = "SELECT `code` FROM issue_info WHERE lottery_id = {} AND issue = '{}'" \
        .format(lottery, issue)
    result = conn.execute(sql).fetchone()
    conn.close()
    return result


class GUIDemo(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):

        self.lotterylabel = Label(self)
        self.lotterylabel["text"] = "選擇彩種:"
        self.lotterylabel.grid(row=0, column=0, sticky=W)

        self.lottery = ttk.Combobox(self)
        lpk10 = sorted(list(pk10.keys()))
        self.lottery['values'] = (lpk10)
        # self.lottery["width"] = 16
        self.lottery.current(0)
        self.lottery.grid(row=0, column=1, sticky=W, padx=10, pady=10)

        self.issuelabel = Label(self)
        self.issuelabel["text"] = "輸入獎期:"
        self.issuelabel.grid(row=1, column=0, sticky=W)

        self.issue = Entry(self)
        self.issue["width"] = 16
        self.issue.grid(row=1, column=1, sticky=W, padx=10, pady=10)

        self.fantanb = Button(self)
        self.fantanb["text"] = "番攤"
        self.fantanb.grid(row=2, column=0)
        self.fantanb["command"] = self.fantanr

        self.mishib = Button(self)
        self.mishib["text"] = "密拾"
        self.mishib.grid(row=2, column=1)
        self.mishib["command"] = self.mishir

        self.bjlb = Button(self)
        self.bjlb["text"] = "百家樂"
        self.bjlb.grid(row=2, column=2)
        self.bjlb["command"] = self.bjlr

        self.displayText = Label(self)
        self.displayText["text"] = ""
        self.displayText['font'] = 'Microsoft JhengHei', 15
        # self.displayText.grid(row=3, column=0, columnspan=2)
        self.displayText.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.statusbar = Label(self, text="開獎號碼...", bd=1, relief=SUNKEN, anchor=W)
        self.statusbar['font'] = 'Microsoft JhengHei', 15
        self.statusbar.grid(sticky=W+E, columnspan=3)
    # 番攤
    def fantanr(self):
        result = sqlexe(pk10[self.lottery.get()], self.issue.get())
        self.displayText["text"] = ''
        self.statusbar["text"] = result[0]
        self.displayText["text"] = fantan(result[0])
    # 密拾
    def mishir(self):
        result = sqlexe(pk10[self.lottery.get()], self.issue.get())
        self.displayText["text"] = ''
        self.statusbar["text"] = result[0]
        self.displayText["text"] = mishi(result[0])
    # 百家樂
    def bjlr(self):
        result = sqlexe(pk10[self.lottery.get()], self.issue.get())
        self.displayText["text"] = ''
        self.statusbar["text"] = result[0]
        self.displayText["text"] = bjl(result[0])


if __name__ == '__main__':
    root = Tk()
    root.title("PK10")
    app = GUIDemo(master=root)
    app.mainloop()
