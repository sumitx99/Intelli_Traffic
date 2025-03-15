def adjust_signal_time(vehicle_count):
    """
    Adjusts traffic light duration based on the number of detected vehicles.
    """
    if vehicle_count > 20:
        return 60  # Increase green light duration to 60s
    elif 10 < vehicle_count <= 20:
        return 40  # Moderate traffic, keep green light for 40s
    else:
        return 20  # Low traffic, reduce green light to 20s
