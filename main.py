from tkinter import *
from monte_carlo import MonteCarlo


def calc_pi(max_iteration):
    mc_object = MonteCarlo(0, 0, 50)
    circ_count = 0
    sqr_count = 0

    for iteration in range(max_iteration):
        x_coord = mc_object.next_drop_x()
        y_coord = mc_object.next_drop_y()

        inside_circle = mc_object.inside_circle(x_coord, y_coord)

        if inside_circle is True:
            circ_count += 1

        sqr_count += 1

    side = mc_object.r * 2
    radius = mc_object.r
    pi = (circ_count * (side ** 2)) / (sqr_count * (radius ** 2))
    return pi


def button_press():
    global display
    clear_output(display)

    calculated_pi = calc_pi(int(iteration_entry.get()))
    display = Label(text=calculated_pi)
    display.pack()


def clear_output(widget):
    widget.destroy()


root = Tk()
root.title("Pi")
root.iconbitmap("C:/Users/masterofdoom/Pictures/pi_character.ico")

iteration_entry = Entry(root)
iteration_entry.pack()

main_button = Button(root, text="Press this to calculate pi", command=button_press)
main_button.pack()

display = Label(root)

root.mainloop()
