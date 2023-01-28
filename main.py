objectName = "testObj"
props = []
columns = []

with open("rowmap.txt") as file:
    for line in file:
        props.append(line)

with open("columns.txt") as file:
    for line in file:
        columns.append(line)

output = open('output.txt', "w")

for (prop, column) in zip(props, columns):
    typeAndName = prop.split()
    dataType = typeAndName[0].strip()
    originalPropertyName = typeAndName[1].strip()
    propertyName = originalPropertyName[0].upper() + originalPropertyName[1:]

    if dataType == "String":
        outputString = objectName + ".set" + propertyName + \
            "(Utils.trimStr(rs.getString(" + column.strip() + ")));" + "\n"
        output.write(outputString)
    else:
        outputString = objectName + ".set" + propertyName + \
            "(rs.get" + dataType + "(" + column.strip() + "));"+"\n"
        output.write(outputString)

output.close()
print("success")
