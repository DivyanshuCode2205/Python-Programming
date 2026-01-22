def length_conversion(a):
    # 1 inch = 2.54 cms
    return (a * 2.54)

lenght = float(input("Enter length in inch(es): "))

print(f"{lenght} inch(es) length converted to {length_conversion(lenght)} cms")
