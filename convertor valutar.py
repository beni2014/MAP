import tkinter as tk

#create the window
window = tk.Tk()

#set window title
window.title("Currency Converter")

# Create labels for currency exchange
usdLabel = tk.Label(window, text="USD")
usdLabel.grid(row=0, column=0)

euroLabel = tk.Label(window, text="EURO")
euroLabel.grid(row=0, column=1)

euroLabel = tk.Label(window, text="RO")
euroLabel.grid(row=1, column=1)

# Create entry field
usdEntry = tk.Entry(window)
usdEntry.grid(row=2, column=0)

euroEntry = tk.Entry(window)
euroEntry.grid(row=2, column=1)

roEntry = tk.Entry(window)
roEntry.grid(row=3, column=1)

# Create convert button
convertButton = tk.Button(window, text="Convert", command= lambda: convert())
convertButton.grid(row=4, column=1)

# Set conversion rate
conversionRateeuro = 0.89
conversionRatero=4.53

# Create conversion function
def convert():
    usdAmount = float(usdEntry.get())
    euroAmount = usdAmount * conversionRateeuro
    euroEntry.delete(0, tk.END)
    euroEntry.insert(0, euroAmount)
    
    roAmount = usdAmount * conversionRatero
    roEntry.delete(0, tk.END)
    roEntry.insert(0, roAmount)

window.mainloop()