import os


input_fil = r"C:\Users\spac-27\uge-2\opgave 2\app_log (logfil analyse) - random.txt"
error_fil = "error_logs.txt"
warning_fil = "warning_logs.txt"


with open(input_fil, "r", encoding="utf-8") as fil, \
    open(error_fil, "w", encoding="utf-8") as error_output, \
    open(warning_fil, "w", encoding="utf-8") as warning_output:

    for linje in fil:
        if "ERROR" in linje:
            error_output.write(linje)
        elif "WARNING" in linje:
            warning_output.write(linje)

print(f"Error logs er gemt i {error_fil}.")
print(f"Warning logs er gemt i {warning_fil}.")
