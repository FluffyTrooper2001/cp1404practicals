
def main():
    file_in = open("temps_input.txt",'r')
    file_out = open("temps_output.txt",'w')
    for line in file_in:
        result = farenheit_to_celsius(float(line))
        file_out.write("{:.15f}\n".format(result))
    file_in.close()
    file_out.close()

def celsius_to_farenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit
def farenheit_to_celsius(farenheit):
    celsius = 5 / 9 * (farenheit - 32)
    return celsius

main()
