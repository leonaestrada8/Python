"""
s = "12:01:00PM"
Retorne '12:01:00'.

s = "12:01:00AM"
Retorne '00:01:00'.

"""
def time(s):
    t = list(s)  # Convert string to list
    if t[-2] == "P":
        if t[0] == '1' and t[1] == '2':  # Check if time is 12 PM
            pass  # 12 PM in 24-hour is 12:00, so do nothing
        else:  # Convert other PM times to 24-hour format
            hours = int(t[0] + t[1]) + 12  # Convert hours part of time to integer and add 12
            t[0], t[1] = str(hours // 10), str(hours % 10)  # Replace hours in t with new hours in 24-hour format
    else:  # Handle 'AM'
        if t[0] == '1' and t[1] == '2':  # 12 AM in 24-hour is 00:00
            t[0], t[1] = '0', '0'
    
    return ''.join(t[:-2])  # Join the list back into a string, excluding 'AM'/'PM'

s = "12:01:00PM"
print(time(s))  # Should print "12:01:00"

s = "12:00:00AM"
print(time(s))
    
s = "12:00:00PM"
print(time(s))
    
s = "04:20:00PM"
print(time(s))

