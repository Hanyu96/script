import datetime
import tkinter as tk
import akshare as ak
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="Initializing...\n")
        self.label.pack()
        self.root.after(1000, self.update_label)

    def update_label(self):
        split_list = self.label["text"].split('\n')
        last_lines = '\n'.join([line for line in split_list[-30:] if line])
        self.label.config(text=last_lines+"\n"+ self.get("MA2309" ) + self.get("FG2307")  + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"")
        self.root.after(2000, self.update_label)
    def get(self,code):
        futures_zh_spot_df = ak.futures_zh_spot(symbol=code, market="CF", adjust='0').iloc[0]['current_price']
        return code + ":\t" + str(futures_zh_spot_df)+"\n"
if __name__ == "__main__":
    app = App()
    app.root.mainloop()
