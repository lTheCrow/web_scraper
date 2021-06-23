from core.Controller import Controller
import tkinter

class MainView(tkinter.Frame):
        bg_color = "black"
        sizeX = 500
        sizeY = 200
        title = 'Simple Web Scraper'

        url_input: tkinter.Entry = None
        log_area: tkinter.Text = None

        controller: Controller = None

        """
        GUI Settings
        ---
                init root components and GUI widgets
        """
        def __init__(self, master=None):
                super().__init__(master)
                self.master = master
                self.master.title(self.title)
                self.master.geometry(self.get_root_size())
                self.master.configure(bg=self.bg_color)
                self.pack()
                self.create_controls(self.master)

        """
        GUI Settings
        ---
                Create widget objects and give GUI properties
        """
        def create_controls(self, master):
                self.heading = tkinter.Label(master, text=self.title, fg="red", bg=self.bg_color, font=('Courier', 18))
                self.heading.pack()

                self.log_area = tkinter.Text(master, width=50, height=7)
                self.log_area.pack()

                self.heading = tkinter.Label(master, text="URL", fg="red", bg=self.bg_color, font=('Arial', 11))
                self.heading.pack(padx=11, side=tkinter.LEFT)

                self.url_input = tkinter.Entry(master)
                self.url_input.pack(padx=5, ipadx=self.sizeX/4, side=tkinter.LEFT)

                self.click_me = tkinter.Button(master, text="Extract", width=5, command=self.get_url)
                self.click_me.pack(padx=10, side=tkinter.RIGHT)

        """
        GUI Settings
        ---
                get main window size in str format
        """
        def get_root_size(self) -> str:
                return f"{self.sizeX}x{self.sizeY}"


        """
        Controller Settings
        ---
                If the button clicked, get the url and set into DOM module
        """
        def get_url(self):
                self.log_area.insert(tkinter.END, "Scraping data...\n")
                controller.url = self.url_input.get()
                controller.set_dom_url()
                self.log_area.insert(tkinter.END, "Scrap success!\n")
                self.log_area.insert(tkinter.END, f"Saving email list in {controller.url}.txt\n")
                emails = controller.get_email_list()
                if len(emails) > 0:
                        self.log_area.insert(tkinter.END, f"Emails found!\n")
                        for email in emails:
                                self.log_area.insert(tkinter.END, f"Email found: {email}\n")
                        controller.save_email_list()
                else:
                        self.log_area.insert(tkinter.END, f"No Email found.\n")
                self.log_area.insert(tkinter.END, f"Saving heading list in {controller.url}.txt\n")
                controller.save_headings()

        

if __name__ == "__main__":
        root = tkinter.Tk()
        root.resizable(False, False)
        controller = Controller()
        icon = tkinter.PhotoImage(file="resources/spider.png")
        root.iconphoto(False, icon)

        view = MainView(master=root)
        view.controller = controller
        view.mainloop()