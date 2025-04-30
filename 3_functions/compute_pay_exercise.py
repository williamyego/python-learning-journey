#Rewrite your pay computation with time-and-a-half for overtime
# and create a function called computepay which takes two parameters (hours and rate).
from tarfile import tar_filter


def computepay(h, r):
    try:
        h = float(h)
        r = float(r)

        if h <= 0 or r <= 0:
            return "Invalid working hours or pay rate!"

        if h <= 40:
            pay = h * r
        else:
            pay = (40 * r) + (h - 40) * (r * 1.5)

        return f"Your pay is {pay}"

    except Exception as e:
        return f"Error: {e}"


