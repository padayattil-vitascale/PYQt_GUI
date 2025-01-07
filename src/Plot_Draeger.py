##Show dräger readings in rectangular plot

from matplotlib.patches import Rectangle

def draeger_values(time, value_in_mgperl):
    convert_value_ppm = float(value_in_mgperl) * 543.5
    time = float(time)
    rect = Rectangle((time - 10, 5), 40, height = convert_value_ppm, color='orange', alpha=0.5, label=f"{round(convert_value_ppm,2)}ppm (Dräger)")
    return rect