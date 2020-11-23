from tkinter import Tk, Canvas, Frame, BOTH

class Simulation(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Elasticity Simulation")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        #canvas.create_oval(10, 10, 80, 80, outline="#f11", fill="#1f1", width=2)
        canvas.create_rectangle(0, 100, 800, 60, outline="#f11", fill="#1f1", width=2)

        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Simulation()
    root.geometry("800x800+100+100")
    root.mainloop()


if __name__ == '__main__':
    main()