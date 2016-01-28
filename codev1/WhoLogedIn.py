import Tkinter as tk
import getData as gD

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        data = gD.getData('*', 'customerPerformanceInfo')
        rowN = 1
        for n in data:
            rowN +=1
        t = SimpleTable(self, rowN,6)
        t.pack(side="top", fill="x")
        t.set(0,0,'SessionID')
        t.set(0,1,'CustomerID')
        t.set(0,2,'Start Session')
        t.set(0,3,'End Session')
        t.set(0,4,'fitness Device')
        t.set(0,5,'burnt calories')
        x=1
        y=0
        for i in data:
            for r in i:
                t.set(x,y,r)
                y+=1
                if y==6:
                    x=x+1
                    y=0

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=10, columns=6):
        # use black background so it "peeks through" to
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="%s/%s" % (row, column),
                                 borderwidth=0, width=30)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()