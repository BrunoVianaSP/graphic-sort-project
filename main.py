import simplegui
import random

WIDTH = 500
HEIGHT = 500

vec = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99]

random.shuffle(vec)

def random_color():
    # colors = ["White", "Blue", "Green", "Yellow"]
    colors = ["White"]
    random.shuffle(colors)
    return colors[0]

def need_swap(array, cur_index, bef_index):
    return array[cur_index] > array[bef_index]

def swap(array, cur_index, bef_index):
    swap = array[cur_index]
    array[cur_index] = array[bef_index]
    array[bef_index] = swap 

### Normal ###
def selection_sort(array):            
    for marker in range(0, len(array) - 1):                
        small = array[marker]                    
        for index in range(marker + 1, len(array)):            
            if need_swap(array, index, marker):                
                swap(array, index, marker)
                return

def insertion_sort(array):
    for marker in range(1, len(array)):                
        for index in range(marker, 0, -1):                    
            bef_index = index - 1
            if need_swap(array, index, bef_index):
                swap(array, index, bef_index)                        
                return
    
def shell_sort(array):    
    stop = False
    h = 1
    while h < len(array) / 3: 
        h = 3 * h + 1		
    while h >= 1:        
        for i in range(h, len(array)):                        
            if stop:
                break
            for j in range(i, h - 1, -h):
                bef_index = j - h                
                if need_swap(array, j, bef_index):				
                    swap(array, j, bef_index)
                    stop = True                                                                
        h = h / 3		
        
### By Step ###
def selection_sort_by_step(array):        
    stop = False    
    for marker in range(0, len(array) - 1):                
        small = array[marker]                           
        for index in range(marker + 1, len(array)):            
            if stop:
                break        
            if need_swap(array, index, marker):                
                swap(array, index, marker)
                stop = True

def insertion_sort_by_step(array):    
    swap = 0
    stop = False        
    for marker in range(1, len(array)):                
        for index in range(marker, 0, -1):                    
            if stop:
                break        
            if array[index] > array[index - 1]:
                swap = array[index]
                array[index] = array[index - 1]
                array[index - 1] = swap                        
                stop = True
            

def shell_sort_by_step(array):    
    stop = False
    swap = 0
    
    h = 1
    while h < len(array) / 3: 
        h = 3 * h + 1		
    while h >= 1:        
        for i in range(h, len(array)):                                    
            for j in range(i, h - 1, -h):                
                if stop:                    
                    break        
                if array[j] > array[j - h]:				
                    swap = array[j]
                    array[j] = array[j - h]
                    array[j - h] = swap
                    stop = True                                                                
        h = h / 3

        
        
# Handler to draw on canvas
def draw(canvas):
    i = 0.01
    j = 0
    while i < 0.99:
        canvas.draw_line([WIDTH * i, HEIGHT * 0.99], 
                            [WIDTH * i, HEIGHT * vec[j]], 
                            1, random_color())                
        i += 0.01
        j += 1 
           
 
        
### Fast Sort ###
def selection_tick():
    selection_sort(vec)
    stop_if_sorted(vec, selection_timer)
        
def insertion_tick():
    insertion_sort(vec)
    stop_if_sorted(vec, insertion_timer) 
    
def shell_tick():
    shell_sort(vec)
    stop_if_sorted(vec, shell_timer) 
        
### Step by Step Sort ###        
def selection_tick_by_step():
    selection_sort_by_step(vec)
    stop_if_sorted(vec, selection_timer_by_step)
        
def insertion_tick_by_step():
    insertion_sort_by_step(vec)
    stop_if_sorted(vec, insertion_timer_by_step)
        
def shell_tick_by_step():
    shell_sort_by_step(vec)
    stop_if_sorted(vec, shell_timer_by_step)

def stop_if_sorted(vec, ticker):
    if isSorted(vec):
        print "Sorted"      
        ticker.stop()

def isSorted(array):    
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            return False
    return True
    
### Normal ###
def run_selection():
    random.shuffle(vec)
    selection_timer.start()

def run_insertion():
    random.shuffle(vec)
    insertion_timer.start()
    
def run_shell():
    random.shuffle(vec)
    shell_timer.start()

### By Step ###
def run_selection_by_step():
    random.shuffle(vec)
    selection_timer_by_step.start()

def run_insertion_by_step():
    random.shuffle(vec)
    insertion_timer_by_step.start()
    
def run_shell_by_step():
    random.shuffle(vec)
    shell_timer_by_step.start()
    
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Graphic Sort Suit", WIDTH, HEIGHT)
frame.add_button("Selection Sort", run_selection, 200)
frame.add_button("Insertion Sort", run_insertion, 200)
frame.add_button("Shell Sort", run_shell, 200)

frame.add_button("Selection Sort By One", run_selection_by_step, 200)
frame.add_button("Insertion Sort By One", run_insertion_by_step, 200)
frame.add_button("Shell Sort By One", run_shell_by_step, 200)

frame.set_draw_handler(draw)

selection_timer = simplegui.create_timer(10, selection_tick)
insertion_timer = simplegui.create_timer(40, insertion_tick)
shell_timer = simplegui.create_timer(40, shell_tick)

selection_timer_by_step = simplegui.create_timer(5, selection_tick_by_step)
insertion_timer_by_step = simplegui.create_timer(5, insertion_tick_by_step)
shell_timer_by_step = simplegui.create_timer(25, shell_tick_by_step)

# Start the frame animation
frame.start()











