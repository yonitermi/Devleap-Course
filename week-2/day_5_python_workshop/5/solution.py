def main(seconds):
    # Handle the sign of the number separately
    sign = "-" if seconds < 0 else ""
    seconds = abs(seconds)

    # Calculate hours, minutes, and seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format the result
    result = "{}{:d}:{:02d}:{:02d}".format(sign, hours, minutes, seconds)
    return result


